"""Command-line interface for the Love Language Quiz."""

from questions import load_questions
from scoring import calculate_scores, get_dominant_language
from storage import save_result
from display import get_language_name, get_language_description, LANGUAGE_INFO


def clear_screen():
    """Print some newlines to simulate clearing screen."""
    print("\n" * 2)


def show_welcome():
    """Display welcome message."""
    print("=" * 50)
    print("        LOVE LANGUAGE QUIZ")
    print("=" * 50)
    print("\nDiscover how you prefer to give and receive love!")
    print("Answer each question by typing A, B, or BOTH.\n")


def get_name():
    """Get the user's name."""
    while True:
        name = input("Enter your name: ").strip()
        if name:
            return name
        print("Please enter a valid name.")


def choose_context():
    """Let user choose relationship context."""
    print("\nWhat relationship are you thinking about?")
    print("  1. Romantic Partner")
    print("  2. Family Member")
    print("  3. Friend")
    print("  4. Self-Discovery")

    contexts = {"1": "romantic", "2": "family", "3": "friend", "4": "self"}

    while True:
        choice = input("\nYour choice (1-4): ").strip()
        if choice in contexts:
            return contexts[choice]
        print("Please enter 1, 2, 3, or 4.")


def ask_question(question, number, total):
    """Display a question and get the answer."""
    print(f"\n--- Question {number} of {total} ---")
    print(f"\n{question['question']}\n")
    print(f"  A) {question['options']['A']}")
    print(f"  B) {question['options']['B']}")
    print(f"  BOTH) Both apply to me equally")

    while True:
        answer = input("\nYour choice (A/B/BOTH): ").strip().upper()
        if answer in ["A", "B", "BOTH"]:
            return answer
        print("Please enter A, B, or BOTH.")


def show_results(name, scores, dominant):
    """Display the quiz results."""
    clear_screen()
    print("=" * 50)
    print("        YOUR RESULTS")
    print("=" * 50)

    language_name = get_language_name(dominant)
    description = get_language_description(dominant)

    print(f"\n{name}, your primary love language is:\n")
    print(f"  >>> {language_name} <<<\n")
    print(f"{description}\n")

    print("-" * 50)
    print("ALL YOUR SCORES:")
    print("-" * 50)

    # Sort scores by value (highest first)
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    for lang_key, score in sorted_scores:
        lang_name = get_language_name(lang_key)
        bar = "#" * score + "." * (10 - score)
        print(f"  {lang_name:25} [{bar}] {score}")

    print()


def run_quiz():
    """Main quiz flow."""
    clear_screen()
    show_welcome()

    # Get user info
    name = get_name()
    context = choose_context()

    # Load questions for chosen context
    questions = load_questions(context)
    total = len(questions)
    answers = []

    print(f"\nGreat! Let's start the quiz with {total} questions.\n")
    input("Press Enter to begin...")

    # Ask each question
    for i, question in enumerate(questions):
        clear_screen()
        choice = ask_question(question, i + 1, total)

        # Record answers
        if choice == "BOTH":
            answers.append({"language": question["scores"]["A"]})
            answers.append({"language": question["scores"]["B"]})
        else:
            answers.append({"language": question["scores"][choice]})

    # Calculate and show results
    scores = calculate_scores(answers)
    dominant = get_dominant_language(scores)

    show_results(name, scores, dominant)

    # Save result
    language_name = get_language_name(dominant)
    save_result(name, language_name)
    print(f"Your result has been saved!\n")

    # Ask to play again
    again = input("Take the quiz again? (y/n): ").strip().lower()
    if again == "y":
        run_quiz()
    else:
        print("\nThank you for taking the Love Language Quiz!")
        print("=" * 50)


if __name__ == "__main__":
    run_quiz()
