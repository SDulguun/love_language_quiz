"""Output formatting and result display."""

import json
import os
import random


# Load love language data from JSON file
def _load_data():
    """Load love language data from the JSON file."""
    data_path = os.path.join(os.path.dirname(__file__), "data", "love_languages.json")
    with open(data_path, "r", encoding="utf-8") as f:
        return json.load(f)


_DATA = _load_data()
LANGUAGE_INFO = _DATA["languages"]
CONTEXT_COMPARISONS = _DATA["context_comparisons"]
_COMPATIBILITY_TIPS_RAW = _DATA["compatibility_tips"]

# Convert string keys to frozenset for compatibility lookup
COMPATIBILITY_TIPS = {}
for key, value in _COMPATIBILITY_TIPS_RAW.items():
    lang1, lang2 = key.split("+")
    COMPATIBILITY_TIPS[frozenset([lang1, lang2])] = value


def get_context_comparison(language_key, current_context):
    """Get context-based comparison text for a love language."""
    language_name = get_language_name(language_key)
    current_insight = CONTEXT_COMPARISONS.get(language_key, {}).get(current_context, "")

    # Get a contrasting context for comparison
    context_order = ["romantic", "workplace", "family", "friend", "long_distance"]
    other_contexts = [c for c in context_order if c != current_context]

    # Pick a contrasting context (workplace vs romantic, etc.)
    if current_context == "romantic":
        contrast_context = "workplace"
    elif current_context == "workplace":
        contrast_context = "romantic"
    elif current_context == "family":
        contrast_context = "friend"
    else:
        contrast_context = "romantic"

    contrast_insight = CONTEXT_COMPARISONS.get(language_key, {}).get(contrast_context, "")

    context_labels = {
        "romantic": "romantic relationships",
        "family": "family connections",
        "friend": "friendships",
        "workplace": "the workplace",
        "long_distance": "long-distance relationships"
    }

    return {
        "current_context": context_labels.get(current_context, current_context),
        "current_insight": current_insight,
        "contrast_context": context_labels.get(contrast_context, contrast_context),
        "contrast_insight": contrast_insight,
        "language_name": language_name
    }


def get_compatibility_tip(lang1, lang2):
    """Get compatibility insight for a pair of love languages."""
    key = frozenset([lang1, lang2])
    return COMPATIBILITY_TIPS.get(key, {
        "title": "A Unique Combination",
        "insight": "Every combination of love languages has its own strengths. The key is understanding and respecting how the other person gives and receives love.",
        "tip": "Take time to learn what makes the other person feel most appreciated."
    })


def get_language_name(key):
    """Get display name for a love language."""
    return LANGUAGE_INFO.get(key, {}).get("name", key)


def get_language_icon(key):
    """Get icon for a love language."""
    return LANGUAGE_INFO.get(key, {}).get("icon", "heart")


def get_language_description(key):
    """Get description for a love language."""
    return LANGUAGE_INFO.get(key, {}).get("description", "")


def get_language_image(key):
    """Get image path for a love language."""
    return LANGUAGE_INFO.get(key, {}).get("image", "")


def get_what_this_means(key):
    """Get 'what this means' explanation for a love language."""
    return LANGUAGE_INFO.get(key, {}).get("what_this_means", "")


def get_tips(key, count=3):
    """Get a random selection of practical tips for a love language."""
    tips = LANGUAGE_INFO.get(key, {}).get("tips", [])
    if len(tips) <= count:
        return tips
    return random.sample(tips, count)


def get_partner_tips(key, context):
    """Get partner tips based on love language and relationship context."""
    tips = LANGUAGE_INFO.get(key, {}).get("partner_tips", {})
    return tips.get(context, tips.get("romantic", []))


def get_playlists(key):
    """Get Spotify playlist recommendations for a love language."""
    return LANGUAGE_INFO.get(key, {}).get("playlists", [])


def get_all_languages():
    """Get all love language info for the learn page."""
    return LANGUAGE_INFO


def get_top_two(scores):
    """Get the top two love languages from scores."""
    sorted_langs = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    primary = sorted_langs[0][0] if len(sorted_langs) > 0 else None
    secondary = sorted_langs[1][0] if len(sorted_langs) > 1 else None
    return primary, secondary


def format_scores_for_display(scores):
    """Format scores for template display."""
    total = sum(scores.values())
    result = []
    for key, score in sorted(scores.items(), key=lambda x: x[1], reverse=True):
        pct = round((score / total * 100)) if total > 0 else 0
        result.append({
            "key": key,
            "name": get_language_name(key),
            "icon": get_language_icon(key),
            "score": score,
            "percent": pct
        })
    return result
