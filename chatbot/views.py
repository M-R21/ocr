from django.shortcuts import render

from django.shortcuts import render, redirect
from .models import FAQ, ClientQuestion
from .services import match_question
from .forms import QuestionForm

def chatbot_view(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            client_question = form.cleaned_data['question']
            faq_match = match_question(client_question)
            
            if faq_match:
                return render(request, 'chatbot/faq_suggestion.html', {
                    'faq': faq_match, 
                    'client_question': client_question
                })
            else:
                # Save client question if no match found
                new_question = ClientQuestion.objects.create(
                    question=client_question, 
                    client=request.user
                )
                return render(request, 'chatbot/question_submitted.html', {
                    'question': new_question
                })
    else:
        form = QuestionForm()
    
    return render(request, 'chatbot/chat.html', {'form': form})

