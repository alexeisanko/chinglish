from django import forms

from chinglish.teachers.models import Teacher
from chinglish.main.models import Lesson, HomeWorkFile, Visitors


class InfoTeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name', 'second_name', 'last_name', 'phone', 'birthday']


class PhotoTeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['photo']


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['teacher', 'date', 'type_lesson', 'time', 'homework_text']
        widgets = {
            'teacher': forms.TextInput(attrs={'placeholder': 'Учитель'}),
            'date': forms.TextInput(attrs={'placeholder': 'Дата занятия'}),
            'homework_text': forms.Textarea(attrs={'placeholder': 'Описание домашнего задания'})
        }


class ModelFormWithFileField(forms.ModelForm):
    class Meta:
        model = HomeWorkFile
        fields = ['lesson', 'homework_file']
