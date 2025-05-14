from django import forms
from .models import Consult


class ConsultForm(forms.Form):
    name = forms.CharField(max_length=255)
    surname = forms.CharField(max_length=255)
    email = forms.EmailField()
    description = forms.CharField(widget=forms.Textarea)
    date = forms.DateField(widget=forms.DateInput, required=False)
    attachment = forms.FileField(required=False)