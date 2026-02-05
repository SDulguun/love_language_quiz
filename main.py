"""Main quiz flow and user interaction - Flask Web App."""

from flask import Flask, render_template, request, redirect, url_for, session
from questions import load_questions
from scoring import calculate_scores, get_dominant_language
from storage import save_result, get_recent_results, get_result_by_share_id
from display import (
    get_language_name,
    get_language_icon,
    get_language_description,
    get_language_image,
    get_what_this_means,
    get_tips,
    get_partner_tips,
    get_playlists,
    get_top_two,
    format_scores_for_display,
    get_all_languages
)
from themes import get_theme, get_all_themes
from auth import (
    register_user,
    authenticate_user,
    add_quiz_result,
    get_user_history
)

app = Flask(__name__)
app.secret_key = "love-language-quiz-secret-key"


@app.context_processor
def inject_globals():
    """Inject theme and user variables into all templates."""
    theme_name = session.get("theme", "peach")
    return {
        "current_theme": get_theme(theme_name),
        "all_themes": get_all_themes(),
        "theme_name": theme_name,
        "current_user": session.get("user")
    }


@app.route("/")
def home():
    """Display the home page."""
    history = get_recent_results(3)
    return render_template("home.html", history=history)


@app.route("/learn")
def learn():
    """Display love language definitions."""
    languages = get_all_languages()
    return render_template("learn.html", languages=languages)


@app.route("/theme/<theme_name>")
def set_theme(theme_name):
    """Set the color theme."""
    session["theme"] = theme_name
    return redirect(request.referrer or url_for("home"))


# Authentication routes
@app.route("/login", methods=["GET", "POST"])
def login():
    """Handle user login."""
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        if authenticate_user(username, password):
            session["user"] = username
            return redirect(url_for("home"))
        return render_template("login.html", error="Invalid username or password")

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Handle user registration."""
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        success, message = register_user(username, password)
        if success:
            session["user"] = username
            return redirect(url_for("home"))
        return render_template("register.html", error=message)

    return render_template("register.html")


@app.route("/logout")
def logout():
    """Log out the current user."""
    session.pop("user", None)
    return redirect(url_for("home"))


@app.route("/profile")
def profile():
    """Display user profile with quiz history."""
    if "user" not in session:
        return redirect(url_for("login"))

    username = session["user"]
    history = get_user_history(username)
    return render_template("profile.html", user=username, history=history)


# Quiz routes
@app.route("/start", methods=["POST"])
def start_quiz():
    """Start a new quiz."""
    # Use logged in username if available, otherwise use form input
    if "user" in session:
        session["name"] = session["user"]
    else:
        session["name"] = request.form.get("name", "Friend")

    session["context"] = request.form.get("context", "romantic")
    session["answers"] = []
    session["current"] = 0
    return redirect(url_for("quiz"))


@app.route("/quiz")
def quiz():
    """Display the current question."""
    context = session.get("context", "romantic")
    questions = load_questions(context)
    current = session.get("current", 0)

    if current >= len(questions):
        return redirect(url_for("result"))

    question = questions[current]
    progress = (current / len(questions)) * 100

    return render_template(
        "quiz.html",
        question=question,
        current=current,
        total=len(questions),
        progress=progress,
        context=context
    )


@app.route("/answer", methods=["POST"])
def answer():
    """Process an answer and move to next question."""
    context = session.get("context", "romantic")
    questions = load_questions(context)
    current = session.get("current", 0)
    choice = request.form.get("choice")

    if current < len(questions) and choice in ["A", "B", "BOTH"]:
        question = questions[current]
        answers = session.get("answers", [])
        answer_counts = session.get("answer_counts", [])

        if choice == "BOTH":
            answers.append({"language": question["scores"]["A"]})
            answers.append({"language": question["scores"]["B"]})
            answer_counts.append(2)
        else:
            language = question["scores"][choice]
            answers.append({"language": language})
            answer_counts.append(1)

        session["answers"] = answers
        session["answer_counts"] = answer_counts
        session["current"] = current + 1

    return redirect(url_for("quiz"))


@app.route("/back")
def go_back():
    """Go back to the previous question."""
    current = session.get("current", 0)
    answers = session.get("answers", [])
    answer_counts = session.get("answer_counts", [])

    if current > 0:
        count = answer_counts.pop() if answer_counts else 1
        answers = answers[:-count]
        session["answers"] = answers
        session["answer_counts"] = answer_counts
        session["current"] = current - 1

    return redirect(url_for("quiz"))


@app.route("/result")
def result():
    """Display the quiz results."""
    answers = session.get("answers", [])
    name = session.get("name", "Friend")
    user = session.get("user")
    theme = session.get("theme", "peach")

    if not answers:
        return redirect(url_for("home"))

    scores = calculate_scores(answers)
    dominant = get_dominant_language(scores)
    language_name = get_language_name(dominant)
    context = session.get("context", "romantic")

    # Get top two languages
    primary_key, secondary_key = get_top_two(scores)

    # Save to public results
    share_id = save_result(name, language_name, scores=scores, icon=get_language_icon(dominant))

    # Save to user history if logged in
    if user:
        add_quiz_result(user, language_name, scores)

    # Clear quiz data but keep user and theme
    session.pop("answers", None)
    session.pop("current", None)
    session.pop("name", None)
    session.pop("context", None)
    session.pop("answer_counts", None)
    session["theme"] = theme
    if user:
        session["user"] = user

    # Calculate total answers for percentage bars
    total_answers = sum(scores.values())

    # Context label for display
    context_labels = {
        "romantic": "Your Romantic Partner",
        "family": "Your Family",
        "friend": "Your Friend",
        "workplace": "Your Colleagues",
        "long_distance": "Your Long-Distance Relationship",
        "self": "Your Relationships"
    }

    return render_template(
        "result.html",
        name=name,
        language=language_name,
        icon=get_language_icon(dominant),
        image=get_language_image(dominant),
        description=get_language_description(dominant),
        what_this_means=get_what_this_means(dominant),
        tips=get_tips(dominant),
        partner_tips=get_partner_tips(dominant, context),
        playlists=get_playlists(dominant),
        context_label=context_labels.get(context, "Your Partner"),
        primary_name=get_language_name(primary_key),
        primary_icon=get_language_icon(primary_key),
        secondary_name=get_language_name(secondary_key) if secondary_key else "",
        secondary_icon=get_language_icon(secondary_key) if secondary_key else "",
        scores=format_scores_for_display(scores),
        total_answers=total_answers,
        share_id=share_id
    )


@app.route("/share/<share_id>")
def share(share_id):
    """Display a public shareable results card."""
    entry = get_result_by_share_id(share_id)
    if not entry:
        return redirect(url_for("home"))

    scores = entry.get("scores", {})
    total = sum(scores.values()) if scores else 1
    display_scores = format_scores_for_display(scores) if scores else []

    return render_template(
        "share.html",
        name=entry["name"],
        language=entry["result"],
        icon=entry.get("icon", "heart"),
        scores=display_scores,
        total_answers=total,
        date=entry.get("date", ""),
        share_id=share_id
    )


@app.route("/compatibility", methods=["GET", "POST"])
def compatibility():
    """Compare love languages with another user."""
    if "user" not in session:
        return redirect(url_for("login"))

    username = session["user"]
    my_result = get_user_latest_result(username)

    if request.method == "POST":
        partner = request.form.get("partner", "").strip()

        if not partner:
            return render_template("compatibility.html", error="Please enter a username.", my_result=my_result)
        if partner == username:
            return render_template("compatibility.html", error="You can't compare with yourself!", my_result=my_result)
        if not user_exists(partner):
            return render_template("compatibility.html", error=f"User '{partner}' not found.", my_result=my_result)

        partner_result = get_user_latest_result(partner)
        if not partner_result:
            return render_template("compatibility.html", error=f"'{partner}' hasn't taken any quizzes yet.", my_result=my_result)
        if not my_result:
            return render_template("compatibility.html", error="You haven't taken a quiz yet! Take one first.", my_result=my_result)

        # Calculate compatibility score using cosine similarity
        my_scores = my_result["scores"]
        partner_scores = partner_result["scores"]
        languages = ["words_of_affirmation", "quality_time", "receiving_gifts", "acts_of_service", "physical_touch"]

        my_vec = [my_scores.get(l, 0) for l in languages]
        p_vec = [partner_scores.get(l, 0) for l in languages]

        dot = sum(a * b for a, b in zip(my_vec, p_vec))
        mag_a = sum(a * a for a in my_vec) ** 0.5
        mag_b = sum(b * b for b in p_vec) ** 0.5
        cosine_sim = dot / (mag_a * mag_b) if mag_a and mag_b else 0
        compat_score = round(cosine_sim * 100)

        # Get dominant languages
        my_dominant = max(my_scores, key=my_scores.get)
        partner_dominant = max(partner_scores, key=partner_scores.get)

        # Get compatibility insight
        compat_tip = get_compatibility_tip(my_dominant, partner_dominant)

        # Format scores for radar chart
        my_display = format_scores_for_display(my_scores)
        partner_display = format_scores_for_display(partner_scores)

        return render_template(
            "compatibility.html",
            my_result=my_result,
            partner_result=partner_result,
            partner_name=partner,
            my_name=username,
            compat_score=compat_score,
            compat_tip=compat_tip,
            my_dominant=my_dominant,
            partner_dominant=partner_dominant,
            my_lang_name=get_language_name(my_dominant),
            partner_lang_name=get_language_name(partner_dominant),
            my_lang_icon=get_language_icon(my_dominant),
            partner_lang_icon=get_language_icon(partner_dominant),
            my_display=my_display,
            partner_display=partner_display,
            languages=[get_language_name(l) for l in languages],
            my_values=[my_scores.get(l, 0) for l in languages],
            partner_values=[partner_scores.get(l, 0) for l in languages],
            compared=True
        )

    return render_template("compatibility.html", my_result=my_result)


if __name__ == "__main__":
    app.run(debug=True)
