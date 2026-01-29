"""User authentication logic."""

import json
import os
import hashlib
from datetime import datetime

USERS_FILE = "data/users.json"


def hash_password(password):
    """Simple password hashing."""
    return hashlib.sha256(password.encode()).hexdigest()


def load_users():
    """Load users from JSON file."""
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r") as file:
        return json.load(file)


def save_users(users):
    """Save users to JSON file."""
    with open(USERS_FILE, "w") as file:
        json.dump(users, file, indent=2)


def register_user(username, password):
    """Register a new user. Returns (success, message)."""
    users = load_users()

    if username in users:
        return False, "Username already exists"
    if len(username) < 3:
        return False, "Username must be at least 3 characters"
    if len(password) < 4:
        return False, "Password must be at least 4 characters"

    users[username] = {
        "password": hash_password(password),
        "created": datetime.now().strftime("%Y-%m-%d"),
        "quiz_history": [],
        "theme_preference": "peach"
    }
    save_users(users)
    return True, "Registration successful"


def authenticate_user(username, password):
    """Check if username/password is valid."""
    users = load_users()
    if username not in users:
        return False
    return users[username]["password"] == hash_password(password)


def get_user(username):
    """Get user data."""
    users = load_users()
    return users.get(username)


def add_quiz_result(username, result, scores):
    """Add a quiz result to user's history."""
    users = load_users()
    if username in users:
        users[username]["quiz_history"].append({
            "result": result,
            "scores": scores,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M")
        })
        save_users(users)


def get_user_history(username):
    """Get user's quiz history."""
    user = get_user(username)
    return user.get("quiz_history", []) if user else []
