from typing import Any, Dict
import json

from django.views.generic import TemplateView, UpdateView
from django.views.generic.edit import ProcessFormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.core import serializers

from chinglish.teachers.models import Teacher
from chinglish.teachers.forms import (
    PhotoTeacherForm,
    InfoTeacherForm,
    UpdateLessonForm,
    UpdateHomeWorkForm,
    UpdateVisitorsForm
)
from chinglish.main.models import Lesson, HomeWorkFile, Visitors
from chinglish.teachers.utilities import get_all_lesson_teacher, get_available_type_lesson


class TeacherView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/teacher.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user:
            teacher, created = Teacher.objects.get_or_create(user=user)
            context['user_info'] = teacher
            context['form_user_data'] = InfoTeacherForm()
            context['form_user_photo'] = PhotoTeacherForm()
            context['form_lesson'] = UpdateLessonForm()
            context['lessons_for_calendar'] = json.dumps(get_all_lesson_teacher(teacher))
            context['available_lesson'] = json.dumps(get_available_type_lesson(teacher))
        return context


teacher_view = TeacherView.as_view()


class UpdatePhotoTeacherView(UpdateView):
    model = Teacher
    form_class = PhotoTeacherForm
    template_name = 'pages/teacher.html'
    template_name_suffix = ''


update_photo_teacher_view = UpdatePhotoTeacherView.as_view()


class UpdateInfoTeacherView(UpdateView):
    model = Lesson
    form_class = InfoTeacherForm
    template_name = 'pages/teacher.html'
    template_name_suffix = ''

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        return JsonResponse(form.errors, status=500)

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        return JsonResponse({'status': 'ok'})


update_info_teacher_view = UpdateInfoTeacherView.as_view()


class UpdateLessonInfoView(ProcessFormView):
    model = Teacher
    form_class = UpdateLessonForm
    template_name = 'pages/teacher.html'
    template_name_suffix = ''

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        return JsonResponse(form.errors, status=500)

    def form_valid(self, form):
        is_created = form.cleaned_data['id_lesson']
        if is_created:
            self.object = Lesson.objects.get(id=form.cleaned_data['id_lesson'])
        else:
            self.object = None
        """If the form is valid, save the associated model."""
        self.object = form.save()
        return JsonResponse({'status': 'ok'})


update_lesson_view = UpdateLessonInfoView.as_view()


class UpdateHomeWorkFileView(UpdateView):
    model = HomeWorkFile
    form_class = UpdateHomeWorkForm
    template_name = 'pages/teacher.html'
    template_name_suffix = ''

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        return JsonResponse(form.errors, status=500)

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        return JsonResponse({'status': 'ok'})


update_homework_file_view = UpdateHomeWorkFileView.as_view()


class UpdateVisitorsView(UpdateView):
    model = Visitors
    form_class = UpdateVisitorsForm
    template_name = 'pages/teacher.html'
    template_name_suffix = ''

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        return JsonResponse(form.errors, status=500)

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        return JsonResponse({'status': 'ok'})


update_visitors_view = UpdateVisitorsView.as_view()
