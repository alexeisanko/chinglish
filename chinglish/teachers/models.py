from django.db import models
from django.utils.translation import gettext_lazy as _


class Teacher(models.Model):
    first_name = models.CharField(_('first name'), max_length=50)
    second_name = models.CharField(_('second name'), max_length=50, blank=True, null=True)
    last_name = models.CharField(_('last name'), max_length=50)
    phone = models.CharField(_('number phone'), max_length=15)
    birthday = models.DateField(_('birthday'))
    user = models.OneToOneField('users.User', on_delete=models.PROTECT, null=True)

    def get_full_name(self):
        full_name = f'{self.last_name} {self.first_name} {self.second_name}'
        return full_name

    def get_short_name(self):
        return self.first_name
