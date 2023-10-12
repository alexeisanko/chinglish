import re

from django.db import models
from django.core.validators import RegexValidator


class StartTime(models.Model):
    start_time = models.TimeField(verbose_name='Время начала занятий')
    actual = models.BooleanField(verbose_name="Актуальное время?", default=True)

    def __str__(self):
        return f'{self.start_time}'

    class Meta:
        verbose_name = 'Время начала занятий'
        verbose_name_plural = "Время начала занятий"


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
    time = models.ForeignKey(StartTime, verbose_name='Время', on_delete=models.PROTECT)
    name = models.CharField(verbose_name='Ученик', max_length=100)
    age = models.IntegerField(verbose_name='Возраст')
    teacher = models.ForeignKey('teachers.Teacher', on_delete=models.CASCADE, verbose_name="Преподаватель")
    phone_regex = re.compile(r'(?:\+|\d)[\d\-\(\) ]{9,}\d')
    phone = models.CharField(verbose_name="Номер телефона", max_length=18,
                             validators=[RegexValidator(regex=phone_regex, message='Некорректный номер телефона')])
    classroom = models.IntegerField(verbose_name='Класс')

    def __str__(self):
        return f'{self.type_lesson}-{self.date} ({self.name}: {self.phone})'

    class Meta:
        verbose_name = 'Пробное занятие'
        verbose_name_plural = "Пробные занятия"


class NotStandardDays(models.Model):
    day = models.DateField(verbose_name='Дата')
    is_work = models.BooleanField(verbose_name='Это рабочий день?', default=False)

    class Meta:
        verbose_name = 'Нестандартный рабочий день'

    verbose_name_plural = "Нестандартные рабочие дни"


class Lesson(models.Model):
    teacher = models.ForeignKey('teachers.Teacher', on_delete=models.CASCADE, verbose_name="Преподаватель")
    type_lesson = models.ForeignKey(TypeLesson, on_delete=models.CASCADE, verbose_name="Тип занятия")
    date = models.DateField(verbose_name='Дата')
    time = models.ForeignKey(StartTime, verbose_name='Время', on_delete=models.PROTECT)
    homework_text = models.TextField(verbose_name='Домашнее задание', blank=True)


class Visitors(models.Model):
    student = models.ForeignKey('students.Student', on_delete=models.CASCADE, verbose_name="Студент")
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name="Занятие")


class HomeWork(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name="Занятие")
    homework_file = models.FileField(verbose_name='Домашнее задание', blank=True, upload_to='homework')
