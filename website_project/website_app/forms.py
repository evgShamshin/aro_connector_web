from django import forms
from .models import Consult


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
