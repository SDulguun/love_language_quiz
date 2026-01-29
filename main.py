"""Main quiz flow and user interaction - Flask Web App."""

from flask import Flask, render_template, request, redirect, url_for, session
from questions import load_questions
from scoring import calculate_scores, get_dominant_language
from storage import save_result, get_recent_results
from display import (
    get_language_name,
    get_language_icon,
    get_language_description,
    get_language_image,
    get_what_this_means,
    get_tips,
    get_partner_tips,
    get_top_two,
    format_scores_for_display,
    get_all_languages
)
from themes import get_theme, get_all_themes

app = Flask(__name__)
app.secret_key = "love-language-quiz-secret-key"


@app.context_processor
def inject_globals():
    """Inject theme and user variables into all templates."""
    theme_name = session.get("theme", "peach")
    return {
        "current_theme": get_theme(theme_name),
        "all_themes": get_all_themes(),
        "theme_name": theme_name
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


@app.route("/start", methods=["POST"])
def start_quiz():
    """Start a new quiz."""
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
    save_result(name, language_name, scores=scores, icon=get_language_icon(dominant))

    # Clear quiz data but keep theme
    session.pop("answers", None)
    session.pop("current", None)
    session.pop("name", None)
    session.pop("context", None)
    session.pop("answer_counts", None)
    session["theme"] = theme

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
        context_label=context_labels.get(context, "Your Partner"),
        primary_name=get_language_name(primary_key),
        primary_icon=get_language_icon(primary_key),
        secondary_name=get_language_name(secondary_key) if secondary_key else "",
        secondary_icon=get_language_icon(secondary_key) if secondary_key else "",
        scores=format_scores_for_display(scores),
        total_answers=total_answers
    )


if __name__ == "__main__":
    app.run(debug=True)
