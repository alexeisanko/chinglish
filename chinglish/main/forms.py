from django import forms

from chinglish.main.models import TrialLesson, TypeLesson


class TrialLessonForm(forms.ModelForm):
    class Meta:
        model = TrialLesson
        fields = ['type_lesson', 'date', 'time', 'name', 'age', 'teacher', 'phone', 'classroom']
        widgets = {
            'type_lesson': forms.Select(attrs={'placeholder': 'Выберите тип занятия', 'class': 'input'}),
            'date': forms.Select(attrs={'placeholder': 'Выберите дату', 'class': 'input'}),
            'time': forms.Select(attrs={'placeholder': 'Выберите время', 'class': 'input'}),
            'name': forms.TextInput(attrs={'placeholder': 'Введите ФИО', 'class': 'input'}),
            'age': forms.TextInput(attrs={'placeholder': 'Введите возраст', 'class': 'input'}),
            'teacher': forms.Select(attrs={'placeholder': 'Выберите преподавателя', 'class': 'input'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Введите номер телефона', 'class': 'input'}),
            'classroom': forms.TextInput(attrs={'placeholder': 'Введите класс', 'class': 'input'}),
        }
