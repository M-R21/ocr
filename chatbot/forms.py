from django import forms

class QuestionForm(forms.Form):
    question = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ask your question here...'
        }),
        label=''
    )
