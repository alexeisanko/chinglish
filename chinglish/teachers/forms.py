import re

from django import forms
from django.core.validators import RegexValidator


class ChangeTeacherInfoForm(forms.ModelForm):
    phone_regex = re.compile(r'(?:\+|\d)[\d\-\(\) ]{9,}\d')
    
    first_name = forms.CharField(max_length=150)
    second_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    phone_number = forms.CharField(validators=[RegexValidator(regex=phone_regex, message='Некорректный номер телефона')])
    birthday = forms.DateField()
    

class PhotoTeacherForm(forms.Form):
    photo = forms.ImageField()