import string

from django import forms


class ConsultForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите ваше имя'}),
                           min_length=2, max_length=255, label="Имя")
    # error_messages={'min_length': "Слишком короткое имя"})
    surname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите вашу фамилию'}),
                              max_length=255, label="Фамилия")
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'example@mail.com'}),
                             label="Электронная почта")
    description = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Не работает формула в параметре - "MKR_Доп. глубина наружная".'}),
        label="Описание")
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'format': '%d.%m.%Y'}),
                           required=False, label="Срок до",
                           input_formats=['%d.%m.%Y', '%d/%m/%Y', '%Y-%m-%d'])
    attachment = forms.FileField(required=False, label="Вложения")