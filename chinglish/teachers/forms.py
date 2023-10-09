from django import forms


from chinglish.teachers.models import Teacher


class InfoTeacherForm(forms.ModelForm):
    class Meta:
            model = Teacher
            fields = ['first_name', 'second_name', 'last_name', 'phone', 'birthday']



class PhotoTeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['photo']
