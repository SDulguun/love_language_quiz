# Love Language Quiz

A Flask web app that helps you discover your love language through an interactive quiz. Answer 15 questions to find out how you prefer to give and receive love, then share your results or compare with others.

## Features

- **Interactive Quiz** — 15 questions with A/B/Both options and back navigation
- **6 Relationship Contexts** — Romantic, Family, Friend, Workplace, Long-Distance, Self-Discovery
- **Detailed Results** — Primary and secondary love languages with doughnut chart, personalized tips, and confetti celebration
- **Shareable Results** — Unique share links, downloadable PNG cards, and Twitter sharing
- **User Accounts** — Register/login to save quiz history and track results over time
- **Compatibility Checker** — Compare your love language with another user using cosine similarity scoring and radar chart
- **4 Color Themes** — Peach Sunset, Rose Garden, Lavender Dreams, Mint Fresh

## Project Structure

```
love_language_quiz/
├── main.py           # Flask routes and app configuration
├── questions.py      # Question loading from JSON by context
├── scoring.py        # Love language score calculation
├── display.py        # Language info, tips, formatting, compatibility tips
├── storage.py        # JSON-based result storage with shareable links
├── auth.py           # User registration, login, and quiz history
├── themes.py         # Color theme definitions
├── templates/        # Jinja2 HTML templates
│   ├── base.html     # Base layout with nav and theme support
│   ├── home.html     # Landing page
│   ├── quiz.html     # Quiz question page
│   ├── result.html   # Results with charts and share buttons
│   ├── share.html    # Public shareable results card
│   ├── learn.html    # Love language definitions
│   ├── compatibility.html  # Side-by-side comparison
│   ├── login.html    # Login form
│   ├── register.html # Registration form
│   └── profile.html  # User quiz history
├── static/
│   ├── style.css     # All styling
│   └── images/       # SVG illustrations
└── data/
    ├── questions.json # 90 questions (15 per context)
    ├── results.json   # Saved quiz results
    └── users.json     # User accounts
```

## How to Run

```bash
pip install flask
python main.py
```

Then open http://localhost:5000 in your browser.

## The 5 Love Languages

| Language | Description |
|----------|-------------|
| Words of Affirmation | Verbal compliments, encouragement, and appreciation |
| Quality Time | Undivided attention and shared activities |
| Receiving Gifts | Thoughtful presents that show someone was thinking of you |
| Acts of Service | Helpful actions that ease responsibilities |
| Physical Touch | Hugs, holding hands, and physical closeness |

## Built With

- Python / Flask
- Jinja2 templates
- Chart.js (doughnut and radar charts)
- Canvas Confetti
- html2canvas (image export)
- Font Awesome icons
