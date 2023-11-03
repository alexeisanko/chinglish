import re
from datetime import date

from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


class Student(models.Model):
    phone_regex = re.compile(r'(?:\+|\d)[\d\-\(\) ]{9,}\d')
    first_name = models.CharField(_('first name'), max_length=25, null=True, default=None)
    second_name = models.CharField(_('second name'), max_length=25, null=True, default=None)
    last_name = models.CharField(_('last name'), max_length=25, null=True, default=None)
    phone = models.CharField(verbose_name="Номер телефона", max_length=18, null=True, default=None, validators=[RegexValidator(regex=phone_regex, message='Некорректный номер телефона')])
    birthday = models.DateField(_('birthday'), null=True, default=None)
    classroom = models.CharField(_('classroom'), max_length=12, null=True, default=None)
    is_child = models.BooleanField(_('is this a child?'), default=False)
    phone_parents = models.CharField(_('number phone parents'), max_length=18, null=True, default=None)
    photo = models.ImageField(_('photo student'), upload_to='student', null=True, default=None)
    user = models.OneToOneField('users.User', on_delete=models.PROTECT, null=True)

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = "Студенты"

    def get_full_name(self):
        if self.first_name:
            full_name = f'{self.last_name} {self.first_name} {self.second_name}'
        else:
            full_name = "Отсутствует"
        return full_name

    def get_short_name(self):
        return self.first_name

    def get_absolute_url(self):
        return f'/students/'

    def get_age(self):
        now = date.today()
        age = now.year - self.birthday.year - ((now.month, now.day) < (self.birthday.month, self.birthday.day))
        return age


