from django import forms
from .models import SuggestionForm


class suggest_form(forms.ModelForm):
    class Meta:
        model =SuggestionForm
        fields=["name","email","content"]