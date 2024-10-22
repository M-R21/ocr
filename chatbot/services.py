from .models import FAQ
from difflib import SequenceMatcher

def match_question(client_question, threshold=0.6):
    """
    Tries to find the most similar FAQ question to the client's question.
    Uses a basic similarity check (you can improve this using more advanced NLP).
    """
    faqs = FAQ.objects.all()  # Get all FAQs from the database
    best_match = None
    best_ratio = 0.0

    for faq in faqs:
        # Calculate similarity ratio using SequenceMatcher from difflib
        ratio = SequenceMatcher(None, client_question.lower(), faq.question.lower()).ratio()

        if ratio > best_ratio and ratio >= threshold:
            best_ratio = ratio
            best_match = faq

    return best_match
