import string

from django import forms
from .models import Consult


# class ConsultForm(forms.Form):
#     name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите ваше имя'}),
#                            min_length=2, max_length=255, label="Имя")
#     # error_messages={'min_length': "Слишком короткое имя"})
#     surname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите вашу фамилию'}),
#                               max_length=255, label="Фамилия")
#     email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'example@mail.com'}),
#                              label="Электронная почта")
#     description = forms.CharField(widget=forms.Textarea(attrs={
#         'placeholder': 'Не работает формула в параметре - "MKR_Доп. глубина наружная".'}),
#         label="Описание")
#     date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'format': '%d.%m.%Y'}),
#                            required=False, label="Срок до",
#                            input_formats=['%d.%m.%Y', '%d/%m/%Y', '%Y-%m-%d'])
#     attachment = forms.FileField(required=False, label="Вложения")

class ConsultFormModel(forms.ModelForm):
    class Meta:
        descr = 'Не работает формула в параметре - "MKR_Доп. глубина наружная".'
        model = Consult
        fields = ('name', 'surname', 'email', 'description', 'date', 'attachment')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Введите ваше имя',
                                           'class': 'form-label'}),
            'surname': forms.TextInput(attrs={'placeholder': 'Введите вашу фамилию',
                                              'class': 'form-label'}),
            'email': forms.TextInput(attrs={'placeholder': 'example@mail.com',
                                            'class': 'form-label'}),
            'description': forms.Textarea(attrs={'placeholder': descr,
                                                 'class': 'form-label'}),
            'date': forms.DateInput(attrs={'type': 'date', 'format': '%d.%m.%Y',
                                           'class': 'form-label'}),
        }
        labels = {'name': 'Имя',
                  'surname': 'Фамилия',
                  'email': 'Электронная почта',
                  'description': 'Описание',
                  'date': 'Срок сдачи',
                  'attachment': 'Вложения'}
