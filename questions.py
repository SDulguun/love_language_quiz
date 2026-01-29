"""Question bank and quiz logic."""

import json


def load_questions(context="romantic"):
    """Load questions from JSON file based on relationship context."""
    with open("data/questions.json", "r") as file:
        all_questions = json.load(file)

    # Return questions for the specified context, default to romantic
    return all_questions.get(context, all_questions.get("romantic", []))


def get_next_question(questions, index):
    """Get question at given index."""
    if index < len(questions):
        return questions[index]
    return None
