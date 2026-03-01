import random

def generate_confidence(components):
    scores = {}
    for category, items in components.items():
        scores[category] = {}
        for item in items:
            scores[category][item] = str(random.randint(75, 95)) + "%"
    return scores
