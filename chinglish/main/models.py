from django.db import models
from django.utils.translation import gettext_lazy as _


class TypeLesson(models.Model):
    name = models.CharField(_('type lessons'), unique=True, max_length=40)
    is_group_lesson = models.BooleanField(_('is this a group lesson?'), default=False)
    duration = models.IntegerField(_('duration lesson (minutes)'), default=60)
    cost = models.IntegerField(_('cost lesson (ruble)'), default=1000)


class Lesson(models.Model):
    type_lesson = models.ForeignKey(TypeLesson, on_delete=models.CASCADE)
