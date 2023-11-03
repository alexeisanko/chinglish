import re
from datetime import date

from django.db import models
from django.core.validators import RegexValidator


class Teacher(models.Model):
    phone_regex = re.compile(r'(?:\+|\d)[\d\-\(\) ]{9,}\d')
    first_name = models.CharField(verbose_name="Имя", max_length=25, null=True, default=None)
    second_name = models.CharField(verbose_name="Отчество", max_length=25, blank=True, null=True, default=None)
    last_name = models.CharField(verbose_name="Фамилия", max_length=25, null=True, default=None)
    phone = models.CharField(verbose_name="Номер телефона", max_length=18, null=True, default=None, validators=[RegexValidator(regex=phone_regex, message='Некорректный номер телефона')])
    birthday = models.DateField(verbose_name="День рождения", null=True, default=None)
    user = models.OneToOneField('users.User', verbose_name="ID пользователя", on_delete=models.PROTECT, null=True, default=None)
    photo = models.ImageField(verbose_name="Фото", upload_to='teacher', null=True, default=None)

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = "Преподаватели"

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        if self.first_name:
            full_name = f'{self.last_name} {self.first_name} {self.second_name}'
        else:
            full_name = "Отсутствует"
        return full_name

    def get_short_name(self):
        return self.first_name

    def get_age(self):
        now = date.today()
        age = now.year - self.birthday.year - ((now.month, now.day) < (self.birthday.month, self.birthday.day))
        return age

    def get_absolute_url(self):
        return f'/teachers/'


class TeacherLesson(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    type_lesson = models.ForeignKey('main.TypeLesson', on_delete=models.CASCADE)
