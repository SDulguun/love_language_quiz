"""Main quiz flow and user interaction."""

from questions import load_questions, get_next_question
from scoring import calculate_scores, get_dominant_language
from storage import save_result, load_results
from display import show_welcome, show_question, show_result


def run_quiz():
    """Run the love language quiz."""
    print("Love Language Quiz")
    print("------------------")
    print("Coming soon!")


if __name__ == "__main__":
    run_quiz()
