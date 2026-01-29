"""Love language scoring logic."""


def calculate_scores(answers):
    """Calculate scores for each love language."""
    scores = {
        "words_of_affirmation": 0,
        "quality_time": 0,
        "receiving_gifts": 0,
        "acts_of_service": 0,
        "physical_touch": 0
    }

    for answer in answers:
        language = answer["language"]
        scores[language] += 1

    return scores


def get_dominant_language(scores):
    """Determine the dominant love language."""
    return max(scores, key=scores.get)
