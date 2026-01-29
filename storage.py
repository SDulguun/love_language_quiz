"""Save and load quiz results using JSON."""

import json
import os
import uuid
from datetime import datetime

RESULTS_FILE = "data/results.json"


def save_result(name, result, scores=None, icon=None):
    """Save quiz result to JSON file. Returns the share_id."""
    results = load_results()

    share_id = uuid.uuid4().hex[:8]

    entry = {
        "name": name,
        "result": result,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "share_id": share_id
    }

    if scores:
        entry["scores"] = scores
    if icon:
        entry["icon"] = icon

    results.append(entry)

    with open(RESULTS_FILE, "w") as file:
        json.dump(results, file, indent=2)

    return share_id


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


def get_result_by_share_id(share_id):
    """Look up a result by its share ID."""
    results = load_results()
    for entry in results:
        if entry.get("share_id") == share_id:
            return entry
    return None
