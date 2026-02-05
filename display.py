"""Output formatting and result display."""

import random


LANGUAGE_INFO = {
    "words_of_affirmation": {
        "name": "Words of Affirmation",
        "icon": "comment-dots",
        "image": "images/languages/words.svg",
        "description": "You feel most loved when people express their feelings through words. Compliments, encouragement, and verbal appreciation make you feel truly valued and connected.",
        "extended": "People with Words of Affirmation as their love language thrive on verbal expressions of love and appreciation. Hearing 'I love you,' receiving compliments, and getting words of encouragement mean the world to them. Criticism or harsh words can be particularly hurtful.",
        "what_this_means": "You connect deepest through spoken and written words. A sincere compliment or heartfelt note can make your entire day, while harsh criticism can linger for weeks.",
        "tips": [
            "Start a daily habit of writing down one thing you appreciate about someone and sharing it with them.",
            "When someone does something you value, tell them specifically why it mattered to you.",
            "Keep a small journal of kind words you receive so you can revisit them on difficult days.",
            "Record a short voice message instead of texting — hearing your voice adds emotional depth.",
            "Write a list of ten things you admire about someone close to you and share it with them.",
            "Before criticizing, pause and reframe your feedback with encouragement first."
        ],
        "partner_tips": {
            "romantic": [
                "Leave surprise love notes in their bag, on the mirror, or on their pillow.",
                "Send a mid-day text telling them exactly what you love about them.",
                "Before bed, share one thing they did that day that made you feel grateful."
            ],
            "family": [
                "Tell them specifically why you are proud of them, not just 'good job.'",
                "Write a heartfelt birthday or holiday card with personal memories.",
                "Call or text them encouragement before a big day or challenge."
            ],
            "friend": [
                "Compliment them genuinely in front of others.",
                "Send an unexpected message telling them why they are a great friend.",
                "After spending time together, follow up with a note about how much you enjoyed it."
            ],
            "workplace": [
                "Give specific praise in team meetings — say exactly what they did well.",
                "Send a quick Slack or email recognizing their contribution after a project wraps.",
                "Write a thoughtful recommendation or endorsement highlighting their strengths."
            ],
            "long_distance": [
                "Send good morning and good night voice messages so they hear your voice daily.",
                "Write a long, heartfelt message about what you love about them — not just 'miss you.'",
                "Leave encouraging notes in their suitcase before they leave so they find them later."
            ]
        },
        "examples": [
            "Saying 'I love you' often",
            "Giving genuine compliments",
            "Writing love letters or notes",
            "Verbal encouragement and support",
            "Expressing gratitude out loud"
        ],
        "playlists": [
            {"name": "Love Songs with Lyrics", "url": "https://open.spotify.com/playlist/37i9dQZF1DX50QitC6Oqtn", "description": "Romantic lyrics to speak to your heart"},
            {"name": "Acoustic Love", "url": "https://open.spotify.com/playlist/37i9dQZF1DWTvNyxOwkztu", "description": "Gentle words of love and affirmation"},
            {"name": "All Out Love", "url": "https://open.spotify.com/playlist/37i9dQZF1DX6mvEU1S6INL", "description": "Classic love songs with meaningful lyrics"}
        ]
    },
    "quality_time": {
        "name": "Quality Time",
        "icon": "clock",
        "image": "images/languages/time.svg",
        "description": "You feel most loved when someone gives you their undivided attention. Meaningful conversations and shared activities make you feel deeply connected.",
        "extended": "For those whose love language is Quality Time, nothing says 'I love you' like full, undivided attention. Being truly present with them, putting down phones, and engaging in meaningful activities together makes them feel cherished. Distractions or cancelled plans can be deeply hurtful.",
        "what_this_means": "Presence matters more than presents for you. You feel closest to people when they set aside distractions and focus entirely on being with you.",
        "tips": [
            "Schedule dedicated, phone-free time with people who matter to you each week.",
            "Practice active listening: maintain eye contact and ask follow-up questions.",
            "Suggest shared activities like cooking, walking, or a hobby to deepen connections.",
            "Try a new experience together — novelty strengthens bonds and creates lasting memories.",
            "Set a 'no screens at the table' rule during meals to protect your together time.",
            "Create a shared playlist, book list, or watchlist so you always have something to enjoy together."
        ],
        "partner_tips": {
            "romantic": [
                "Create a weekly ritual like a date night or evening walk together, phone-free.",
                "When they talk, put everything down and give your full attention.",
                "Plan a surprise activity around something they love doing."
            ],
            "family": [
                "Set up a regular family meal where everyone puts their phones away.",
                "Show up at events that matter to them, even if they seem small.",
                "Ask open-ended questions about their life and genuinely listen."
            ],
            "friend": [
                "Initiate plans rather than waiting for them to suggest hanging out.",
                "Be fully present when you are together instead of checking your phone.",
                "Remember details from past conversations and bring them up later."
            ],
            "workplace": [
                "Schedule regular one-on-one check-ins where you give them your full attention.",
                "Invite them to lunch or coffee and put your phone away during the conversation.",
                "Collaborate side by side on tasks rather than dividing everything up."
            ],
            "long_distance": [
                "Schedule regular video call dates and treat them as unmissable commitments.",
                "Do activities together remotely — watch a movie, cook the same recipe, or play a game.",
                "Stay on the call even during quiet moments; companionable silence counts as quality time."
            ]
        },
        "examples": [
            "Having meaningful conversations",
            "Going on walks together",
            "Sharing hobbies and activities",
            "Making eye contact when talking",
            "Planning dedicated date nights"
        ],
        "playlists": [
            {"name": "Cozy Coffeehouse", "url": "https://open.spotify.com/playlist/37i9dQZF1DX6ziVCWnEVZM", "description": "Perfect background for quality time together"},
            {"name": "Date Night", "url": "https://open.spotify.com/playlist/37i9dQZF1DX4xuWVBs4FgJ", "description": "Set the mood for your special moments"},
            {"name": "Evening Acoustic", "url": "https://open.spotify.com/playlist/37i9dQZF1DXbJmiEZs5p2i", "description": "Relaxing tunes for togetherness"}
        ]
    },
    "receiving_gifts": {
        "name": "Receiving Gifts",
        "icon": "gift",
        "image": "images/languages/gifts.svg",
        "description": "You feel most loved through thoughtful presents. It's not about the cost, but the thought and effort behind the gift that makes you feel special.",
        "extended": "For people with Receiving Gifts as their love language, a thoughtful present is a visual symbol of love. It's not about materialism; it's about the thought, effort, and love behind the gift. Missing special occasions or giving thoughtless gifts can be particularly painful.",
        "what_this_means": "For you, a gift is a tangible reminder that someone was thinking about you. The effort and thought behind it matter far more than the price tag.",
        "tips": [
            "Keep a small wish list so people who want to show love know what resonates with you.",
            "When you receive a meaningful gift, display or keep it somewhere visible as a reminder.",
            "Pay attention to what others mention wanting so you can return the thoughtfulness.",
            "Take a photo of gifts you love and create a digital album to revisit when you need a boost.",
            "Remember that handmade gifts often carry more meaning than expensive ones — try making one.",
            "Start a tradition of exchanging small meaningful gifts on ordinary days, not just holidays."
        ],
        "partner_tips": {
            "romantic": [
                "Keep a running list of things they mention wanting and surprise them later.",
                "It does not have to be expensive: their favorite snack or a single flower counts.",
                "Mark important dates and never let an anniversary or birthday pass unnoticed."
            ],
            "family": [
                "Bring a small souvenir when you travel, even if it is something tiny.",
                "Give them something that shows you remember a specific shared memory.",
                "Wrap gifts thoughtfully because the presentation shows extra care."
            ],
            "friend": [
                "Surprise them with their favorite coffee or treat when you meet up.",
                "Pick up a small 'thinking of you' gift when you see something they would like.",
                "On their birthday, choose something personal rather than generic."
            ],
            "workplace": [
                "Bring back a small souvenir from business trips or vacations for them.",
                "Remember their coffee order and surprise them with it on a busy day.",
                "Give a thoughtful gift on their work anniversary that reflects their personality."
            ],
            "long_distance": [
                "Send surprise care packages with their favorite snacks, a handwritten note, and small comforts.",
                "Order food delivery to their door on a day you know is tough for them.",
                "Mail them something that connects you — matching items, a photo album, or a playlist on a USB."
            ]
        },
        "examples": [
            "Bringing home their favorite treat",
            "Remembering special occasions",
            "Picking up small 'thinking of you' gifts",
            "Creating handmade presents",
            "Keeping meaningful mementos"
        ],
        "playlists": [
            {"name": "Feel Good Pop", "url": "https://open.spotify.com/playlist/37i9dQZF1DX3rxVfibe1L0", "description": "Upbeat celebration vibes"},
            {"name": "Happy Hits", "url": "https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC", "description": "Songs that make you smile"},
            {"name": "Good Vibes", "url": "https://open.spotify.com/playlist/37i9dQZF1DX0UrRvztWcAU", "description": "Feel-good tracks for special moments"}
        ]
    },
    "acts_of_service": {
        "name": "Acts of Service",
        "icon": "hands-helping",
        "image": "images/languages/service.svg",
        "description": "You feel most loved when someone helps you with tasks or does things for you. Actions truly speak louder than words for you.",
        "extended": "For those whose love language is Acts of Service, actions speak louder than words. They feel loved when someone eases their responsibilities by helping with tasks, chores, or projects. Laziness, broken promises, or making more work for them can be hurtful.",
        "what_this_means": "Actions prove love for you. When someone takes something off your plate without being asked, it tells you they truly care about your well-being.",
        "tips": [
            "Do not be afraid to ask for help; people who love you want to support you.",
            "Notice when others are overwhelmed and offer specific help instead of a vague 'let me know.'",
            "Acknowledge and appreciate when someone does something helpful for you.",
            "Create a shared task list with someone you care about so helping feels collaborative, not one-sided.",
            "When you see something that needs doing, just do it — do not wait to be asked.",
            "Finish tasks completely rather than halfway; follow-through is what makes service feel like love."
        ],
        "partner_tips": {
            "romantic": [
                "Do a chore they dislike without being asked, like dishes or laundry.",
                "When they are stressed, take something off their plate instead of just offering words.",
                "Follow through on every promise you make, no matter how small."
            ],
            "family": [
                "Offer to help with a task you know they have been putting off.",
                "Cook a meal or handle an errand to lighten their load.",
                "Show up when they need a hand, even if it is inconvenient for you."
            ],
            "friend": [
                "Help them move, fix something, or tackle a project without being asked twice.",
                "Offer a ride, drop off food, or run an errand when they are having a hard week.",
                "When they mention a problem, look for a way to help solve it, not just sympathize."
            ],
            "workplace": [
                "Offer to take on a task when you see a colleague struggling with their workload.",
                "Proactively prepare materials or notes before a meeting to make their job easier.",
                "Stay late to help them finish a deadline even when it is not your responsibility."
            ],
            "long_distance": [
                "Help coordinate things in their life from afar — book appointments, research options, plan logistics.",
                "Order groceries or essentials to be delivered when you know they are too busy.",
                "Take care of shared responsibilities so they have one less thing to worry about."
            ]
        },
        "examples": [
            "Cooking a meal for them",
            "Helping with household chores",
            "Running errands without being asked",
            "Taking care of car maintenance",
            "Helping with a difficult project"
        ],
        "playlists": [
            {"name": "Motivation Mix", "url": "https://open.spotify.com/playlist/37i9dQZF1DXdxcBWuJkbcy", "description": "Energizing tracks to power through tasks"},
            {"name": "Songs to Sing in the Car", "url": "https://open.spotify.com/playlist/37i9dQZF1DWWMOmoXKqHTD", "description": "Uplifting music for errands and chores"},
            {"name": "Productive Morning", "url": "https://open.spotify.com/playlist/37i9dQZF1DX0SM0LYsmbMT", "description": "Start your day of service right"}
        ]
    },
    "physical_touch": {
        "name": "Physical Touch",
        "icon": "hand-holding-heart",
        "image": "images/languages/touch.svg",
        "description": "You feel most loved through physical affection. Hugs, holding hands, and other forms of touch make you feel secure and cared for.",
        "extended": "People with Physical Touch as their love language feel most connected through physical expressions of love. Hugs, holding hands, pats on the back, and thoughtful touches communicate warmth, safety, and love. Physical neglect or abuse can be especially devastating.",
        "what_this_means": "Physical closeness is your emotional anchor. A warm hug can calm you faster than any words, and a lack of touch can leave you feeling disconnected.",
        "tips": [
            "Let people know that physical affection matters to you so they understand your needs.",
            "Initiate the touch you want to receive: offer hugs, sit close, or reach for a hand.",
            "Find appropriate ways to incorporate touch in daily routines, like greeting with a hug.",
            "Try activities that naturally involve closeness, like dancing, partner yoga, or team sports.",
            "When comforting someone, sometimes a silent hug says more than any words could.",
            "Pay attention to others' comfort levels — always respect personal boundaries with touch."
        ],
        "partner_tips": {
            "romantic": [
                "Greet them and say goodbye with a meaningful hug or kiss every single day.",
                "Reach for their hand when walking, driving, or sitting together.",
                "Offer a shoulder rub or gentle touch when they seem stressed."
            ],
            "family": [
                "Give warm, genuine hugs when greeting and leaving.",
                "A pat on the back or hand on the shoulder shows support during tough moments.",
                "Sit close during family time instead of across the room."
            ],
            "friend": [
                "Greet them with a hug instead of just a wave.",
                "A high-five, fist bump, or side hug after good news shows you care.",
                "Be physically present during hard times: sitting next to them matters."
            ],
            "workplace": [
                "Offer a firm handshake or friendly fist bump when greeting colleagues.",
                "Celebrate team wins with high-fives to build camaraderie.",
                "A pat on the shoulder after a tough presentation shows quiet support."
            ],
            "long_distance": [
                "Send a piece of clothing that smells like you so they have something physical to hold.",
                "Make reunion hugs long and intentional — do not rush through them.",
                "During visits, prioritize physical closeness: hold hands, sit close, and make up for lost time."
            ]
        },
        "examples": [
            "Holding hands while walking",
            "Giving warm hugs",
            "Cuddling on the couch",
            "A gentle touch on the arm",
            "Back rubs after a long day"
        ],
        "playlists": [
            {"name": "Slow Dance", "url": "https://open.spotify.com/playlist/37i9dQZF1DX7rOY2tZUw1k", "description": "Intimate slow dance classics"},
            {"name": "Chill R&B", "url": "https://open.spotify.com/playlist/37i9dQZF1DX2UgsUIg75Vg", "description": "Smooth vibes for closeness"},
            {"name": "Bedroom Pop", "url": "https://open.spotify.com/playlist/37i9dQZF1DXcxvFzl58uP7", "description": "Cozy intimate atmosphere"}
        ]
    }
}


COMPATIBILITY_TIPS = {
    frozenset(["words_of_affirmation", "words_of_affirmation"]): {
        "title": "A Symphony of Words",
        "insight": "You both thrive on verbal expression. Your relationship can be incredibly affirming since you naturally speak the same language. Be mindful that harsh words can cut twice as deep when both partners are sensitive to them.",
        "tip": "Make it a daily ritual to share specific compliments with each other."
    },
    frozenset(["words_of_affirmation", "quality_time"]): {
        "title": "Deep Conversations Await",
        "insight": "One of you loves hearing heartfelt words while the other craves undivided attention. The great news is that meaningful conversations satisfy both needs at once.",
        "tip": "Set aside phone-free time for genuine, expressive conversations."
    },
    frozenset(["words_of_affirmation", "receiving_gifts"]): {
        "title": "Thoughtful Expressions",
        "insight": "Words and gifts are both ways of showing someone you thought of them. Pairing a heartfelt note with a small gift can make both of you feel deeply loved.",
        "tip": "Write personal notes to accompany gifts — the words make the gift more meaningful."
    },
    frozenset(["words_of_affirmation", "acts_of_service"]): {
        "title": "Say It and Show It",
        "insight": "One speaks love, the other shows it through action. Together you cover both sides of the coin. The key is recognizing that both forms of expression carry equal weight.",
        "tip": "When you do something helpful, explain why you did it. When you appreciate an action, say it out loud."
    },
    frozenset(["words_of_affirmation", "physical_touch"]): {
        "title": "Words Meet Warmth",
        "insight": "Verbal affirmation paired with physical closeness creates a powerful emotional bond. A hug combined with 'I love you' can be the ultimate expression of care.",
        "tip": "Whisper words of appreciation during embraces to connect on both levels."
    },
    frozenset(["quality_time", "quality_time"]): {
        "title": "Fully Present Together",
        "insight": "You both value undivided attention above all else. Your connection deepens naturally when you are together. Just make sure you also maintain healthy independence.",
        "tip": "Create a weekly tradition that belongs to just the two of you."
    },
    frozenset(["quality_time", "receiving_gifts"]): {
        "title": "Moments and Mementos",
        "insight": "One values shared experiences while the other treasures tangible reminders of love. Creating memories together and bringing home small souvenirs satisfies both.",
        "tip": "Plan experiences together and keep small keepsakes from your shared adventures."
    },
    frozenset(["quality_time", "acts_of_service"]): {
        "title": "Together in Action",
        "insight": "One craves presence, the other appreciates helpful deeds. Doing tasks together — cooking, cleaning, or running errands side by side — beautifully merges both languages.",
        "tip": "Turn everyday chores into quality time by doing them as a team."
    },
    frozenset(["quality_time", "physical_touch"]): {
        "title": "Close and Connected",
        "insight": "Presence and touch naturally complement each other. Simply being physically close while spending time together fulfills both of your deepest needs.",
        "tip": "Cuddle during movies, hold hands on walks — physical closeness during shared time is your sweet spot."
    },
    frozenset(["receiving_gifts", "receiving_gifts"]): {
        "title": "Thoughtful Gift Givers",
        "insight": "You both understand the power of a well-chosen gift. You naturally know how to make each other feel special through thoughtful presents and surprises.",
        "tip": "Keep running lists of things you each mention wanting so you always have ideas ready."
    },
    frozenset(["receiving_gifts", "acts_of_service"]): {
        "title": "Giving in Every Way",
        "insight": "One shows love through thoughtful gifts, the other through helpful actions. Both are generous at heart. Recognizing that a cooked meal is as meaningful as a wrapped present is key.",
        "tip": "Appreciate each other's unique way of giving — a helpful deed is their version of a gift."
    },
    frozenset(["receiving_gifts", "physical_touch"]): {
        "title": "Tangible Love",
        "insight": "Both of you appreciate concrete, tangible expressions of love — whether a gift in hand or a hand to hold. You both need love you can feel and see.",
        "tip": "Hand-deliver gifts personally with a warm embrace for maximum impact."
    },
    frozenset(["acts_of_service", "acts_of_service"]): {
        "title": "Actions Speak Loudest",
        "insight": "You both believe that love is a verb. Your relationship runs smoothly when you share the load and show care through helpful deeds. Just be careful not to keep score.",
        "tip": "Focus on helping each other willingly rather than tracking who did what."
    },
    frozenset(["acts_of_service", "physical_touch"]): {
        "title": "Caring Hands",
        "insight": "One feels loved through helpful actions, the other through physical affection. A back rub after a long day or holding their hand while helping with a task bridges both beautifully.",
        "tip": "Add a physical touch element to acts of service — a hug after cooking dinner, a pat on the back while helping."
    },
    frozenset(["physical_touch", "physical_touch"]): {
        "title": "The Power of Touch",
        "insight": "You both feel most connected through physical closeness. Your relationship is naturally warm and affectionate. Physical distance can be especially challenging for you both.",
        "tip": "Establish daily touch rituals — greeting hugs, goodnight embraces, and casual physical closeness throughout the day."
    }
}


CONTEXT_COMPARISONS = {
    "words_of_affirmation": {
        "romantic": "In romantic relationships, you crave verbal expressions of love — hearing 'I love you' and receiving heartfelt compliments.",
        "family": "With family, you value words of pride and encouragement — knowing they believe in you matters deeply.",
        "friend": "Among friends, you appreciate genuine compliments and messages that affirm your importance in their life.",
        "workplace": "At work, you thrive on specific praise and recognition — verbal acknowledgment of your contributions motivates you.",
        "long_distance": "In long-distance relationships, voice messages and heartfelt texts help you feel connected across the miles."
    },
    "quality_time": {
        "romantic": "In romantic relationships, you treasure undivided attention — date nights and phone-free moments together.",
        "family": "With family, you value shared meals and being truly present at important events.",
        "friend": "Among friends, you appreciate when they initiate plans and give you their full attention.",
        "workplace": "At work, you value one-on-one meetings and collaborative time working side by side.",
        "long_distance": "In long-distance relationships, scheduled video calls and doing activities together remotely keep you connected."
    },
    "receiving_gifts": {
        "romantic": "In romantic relationships, thoughtful surprises and remembered anniversaries make you feel cherished.",
        "family": "With family, meaningful souvenirs and personalized presents show they were thinking of you.",
        "friend": "Among friends, small 'thinking of you' gifts and remembered favorites warm your heart.",
        "workplace": "At work, you appreciate tokens of appreciation and colleagues who remember your preferences.",
        "long_distance": "In long-distance relationships, care packages and surprise deliveries bridge the physical gap."
    },
    "acts_of_service": {
        "romantic": "In romantic relationships, you feel loved when your partner handles tasks without being asked.",
        "family": "With family, helping hands during busy times and shared responsibilities show care.",
        "friend": "Among friends, you value those who show up to help — actions speak louder than words.",
        "workplace": "At work, colleagues who pitch in during crunch time and follow through on commitments earn your trust.",
        "long_distance": "In long-distance relationships, coordinating things from afar and handling shared tasks shows dedication."
    },
    "physical_touch": {
        "romantic": "In romantic relationships, holding hands, hugs, and physical closeness make you feel secure and loved.",
        "family": "With family, warm embraces and sitting close during gatherings strengthen your bond.",
        "friend": "Among friends, greeting hugs and high-fives show affection and celebration.",
        "workplace": "At work, appropriate gestures like handshakes and celebratory high-fives build connection.",
        "long_distance": "In long-distance relationships, reunion hugs and physical presence during visits are precious moments."
    }
}


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
