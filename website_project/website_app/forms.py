from django import forms
from .models import Consult


class ConsultForm(forms.Form):
    name = forms.CharField(max_length=255, label="Имя")
    surname = forms.CharField(max_length=255, label="Фамилия")
    email = forms.EmailField(label="Электронная почта")
    description = forms.CharField(widget=forms.Textarea, label="Описание")
    date = forms.DateField(widget=forms.DateInput, required=False, label="Дата")
    attachment = forms.FileField(required=False, label="Вложения")
