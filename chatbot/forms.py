from django import forms
from .models import ClientQuestion

class QuestionForm(forms.ModelForm):
    class Meta:
        model = ClientQuestion
        fields = ['question']
