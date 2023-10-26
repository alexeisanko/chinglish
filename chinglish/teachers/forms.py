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


class UpdateLessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['teacher', 'date', 'type_lesson', 'time', 'homework_text']
        widgets = {
            'teacher': forms.TextInput(attrs={'placeholder': 'Учитель'}),
            'date': forms.TextInput(attrs={'placeholder': 'Учитель'})

        }
    id_lesson = forms.IntegerField(widget=forms.NumberInput(attrs={'required': False, 'hidden': True}))


class UpdateHomeWorkForm(forms.ModelForm):
    class Meta:
        model = HomeWorkFile
        fields = '__all__'


class UpdateVisitorsForm(forms.ModelForm):
    class Meta:
        model = Visitors
        fields = '__all__'

