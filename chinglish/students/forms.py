from django import forms

from chinglish.students.models import Student


class InfoStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'second_name', 'last_name', 'phone', 'birthday']


class PhotoStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['photo']
