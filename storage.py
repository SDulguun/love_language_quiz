"""Save and load quiz results using JSON."""

import json
import os
from datetime import datetime

RESULTS_FILE = "data/results.json"


def save_result(name, result, scores=None, icon=None):
    """Save quiz result to JSON file."""
    results = load_results()

    entry = {
        "name": name,
        "result": result,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    if scores:
        entry["scores"] = scores
    if icon:
        entry["icon"] = icon

    results.append(entry)

    with open(RESULTS_FILE, "w") as file:
        json.dump(results, file, indent=2)


def load_results():
    """Load previous results from JSON file."""
    if not os.path.exists(RESULTS_FILE):
        return []

    with open(RESULTS_FILE, "r") as file:
        return json.load(file)


def get_recent_results(count=3):
    """Get the most recent quiz results."""
    results = load_results()
    return results[-count:] if results else []
