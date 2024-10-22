from .models import FAQ

def match_question(input_question):
    keywords = input_question.lower().split()  # simple keyword extraction
    possible_faqs = FAQ.objects.filter(question__icontains=keywords[0])  # search with the first keyword as an example
    for faq in possible_faqs:
        if all(keyword in faq.question.lower() for keyword in keywords):
            return faq
    return None
