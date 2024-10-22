from .services import match_question  # Ensure this import is present

def chatbot_view(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            client_question = form.cleaned_data['question']
            
            # Find the closest matching FAQ
            faq_match = match_question(client_question)
            
            if faq_match:
                # FAQ match found, show suggestion to user
                return render(request, 'chatbot/faq_suggestion.html', {
                    'faq': faq_match,  # Pass the matched FAQ to the template
                    'client_question': client_question
                })
            else:
                # No match, ask for new question submission
                client = request.user if request.user.is_authenticated else None
                new_question = ClientQuestion.objects.create(
                    question=client_question,
                    client=client  # Can be None for anonymous users
                )
                
                # Notify admins about the new question
                admins = User.objects.filter(is_staff=True)
                for admin in admins:
                    send_mail(
                        'New Question Submitted',
                        f'A new question has been submitted: {new_question.question}',
                        'mr21dpl@gmail.com',
                        [admin.email]
                    )
                
                return render(request, 'chatbot/question_submitted.html', {
                    'question': new_question
                })
    else:
        form = QuestionForm()

    return render(request, 'chatbot/chat.html', {'form': form})
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .models import FAQ, ClientQuestion
from .services import match_question
from .forms import QuestionForm  # Import the form here

def chatbot_view(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            client_question = form.cleaned_data['question']
            faq_match = match_question(client_question)
            
            if faq_match:
                # FAQ match found
                return render(request, 'chatbot/faq_suggestion.html', {
                    'faq': faq_match, 
                    'client_question': client_question
                })
            else:
                # No FAQ match, submit the question to admins
                client = request.user if request.user.is_authenticated else None  # Handle anonymous user
                new_question = ClientQuestion.objects.create(
                    question=client_question,
                    client=client  # Can be None for anonymous users
                )
                
                # Send notification to admins
                admins = User.objects.filter(is_staff=True)
                for admin in admins:
                    send_mail(
                        'New Question Submitted',
                        f'A new question has been submitted: {new_question.question}',
                        'noreply@yourdomain.com',
                        [admin.email]
                    )
                
                return render(request, 'chatbot/question_submitted.html', {
                    'question': new_question
                })
    else:
        form = QuestionForm()

    return render(request, 'chatbot/chat.html', {'form': form})
def chatbot_view(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            client_question = form.cleaned_data['question']
            faq_match = match_question(client_question)
            
            if faq_match:
                # FAQ match found
                return render(request, 'chatbot/faq_suggestion.html', {
                    'faq': faq_match, 
                    'client_question': client_question
                })
            else:
                # No FAQ match, submit the question to admins
                client = request.user if request.user.is_authenticated else None  # Handle anonymous user
                new_question = ClientQuestion.objects.create(
                    question=client_question,
                    client=client  # Can be None for anonymous users
                )
                
                # Send notification to admins
                admins = User.objects.filter(is_staff=True)
                for admin in admins:
                    send_mail(
                        'New Question Submitted',
                        f'A new question has been submitted: {new_question.question}',
                        'noreply@yourdomain.com',
                        [admin.email]
                    )
                
                return render(request, 'chatbot/question_submitted.html', {
                    'question': new_question
                })
    else:
        form = QuestionForm()

    return render(request, 'chatbot/chat.html', {'form': form})
