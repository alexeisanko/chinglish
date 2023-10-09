import re

from django.db import models
from django.core.validators import RegexValidator


class TypeLesson(models.Model):
    name = models.CharField(verbose_name='Тип занятия', unique=True, max_length=40)
    is_group_lesson = models.BooleanField(verbose_name='Групповое занятие', default=False)
    available_trial_lesson = models.BooleanField(verbose_name='Доступно для пробной записи?', default=False)
    duration = models.IntegerField(verbose_name='Продолжительность занятия (минуты)', default=60)
    cost = models.IntegerField(verbose_name='Стоимость (рубли)', default=1000)
    description = models.TextField(verbose_name='Описание', blank=True, default='')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Тип занятия'
        verbose_name_plural = "Типы занятий"


class TrialLesson(models.Model):
    type_lesson = models.ForeignKey(TypeLesson, on_delete=models.CASCADE, verbose_name="Тип занятия")
    date = models.DateField(verbose_name='Дата')
    time = models.TimeField(verbose_name='Время')
    name = models.CharField(verbose_name='Ученик', max_length=100)
    age = models.IntegerField(verbose_name='Возраст')
    teacher = models.ForeignKey('teachers.Teacher', on_delete=models.CASCADE, verbose_name="Преподаватель")
    phone_regex = re.compile(r'(?:\+|\d)[\d\-\(\) ]{9,}\d')
    phone = models.CharField(verbose_name="Номер телефона", max_length=18, validators=[RegexValidator(regex=phone_regex, message='Некорректный номер телефона')])
    classroom = models.IntegerField(verbose_name='Класс')

    def __str__(self):
        return f'{self.type_lesson}-{self.date} ({self.name}: {self.phone})'

    class Meta:
        verbose_name = 'Пробное занятие'
        verbose_name_plural = "Пробные занятия"
