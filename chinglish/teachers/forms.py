import re

from django import forms
from django.core.validators import RegexValidator

from chinglish.teachers.models import Teacher


class ChangeTeacherInfoForm(forms.ModelForm):
    phone_regex = re.compile(r'(?:\+|\d)[\d\-\(\) ]{9,}\d')

    first_name = forms.CharField(max_length=150)
    second_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    phone_number = forms.CharField(validators=[RegexValidator(regex=phone_regex, message='Некорректный номер телефона')])
    birthday = forms.DateField()


class PhotoTeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['photo']
