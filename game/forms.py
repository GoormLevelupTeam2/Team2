from django import forms
from .models import Question


class AnswerInputForm(forms.ModelForm):
    class Meta:
        model = Question

        fields = ['input']