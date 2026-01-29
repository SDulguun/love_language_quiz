"""Theme definitions for the quiz."""

THEMES = {
    "peach": {
        "name": "Peach Sunset",
        "icon": "sun",
        "gradient_start": "#ffecd2",
        "gradient_end": "#fcb69f",
        "primary": "#ff6b8a",
        "primary_end": "#ff8e72"
    },
    "rose": {
        "name": "Rose Garden",
        "icon": "spa",
        "gradient_start": "#fce4ec",
        "gradient_end": "#f8bbd0",
        "primary": "#e91e63",
        "primary_end": "#f06292"
    },
    "lavender": {
        "name": "Lavender Dreams",
        "icon": "moon",
        "gradient_start": "#e8eaf6",
        "gradient_end": "#c5cae9",
        "primary": "#7c4dff",
        "primary_end": "#b388ff"
    },
    "mint": {
        "name": "Mint Fresh",
        "icon": "leaf",
        "gradient_start": "#e0f2f1",
        "gradient_end": "#b2dfdb",
        "primary": "#26a69a",
        "primary_end": "#80cbc4"
    }
}


def get_theme(name):
    """Get theme by name, default to peach."""
    return THEMES.get(name, THEMES["peach"])


def get_all_themes():
    """Get all available themes."""
    return THEMES
