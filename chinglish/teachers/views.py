from typing import Any, Dict
import json
import re

from django.views.generic import TemplateView, UpdateView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpRequest

from chinglish.teachers.models import Teacher
from chinglish.students.models import Student
from chinglish.teachers.forms import (
    PhotoTeacherForm,
    InfoTeacherForm,
    LessonForm,
    ModelFormWithFileField,
)
from chinglish.main.models import Lesson, HomeWorkFile, Visitors
from chinglish.teachers.utilities import (
    get_all_lesson_teacher,
    get_available_type_lesson,
    free_time_to_date,
    get_info_lesson_to_calendar,
)


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
            context['form_lesson'] = LessonForm()
            context['lessons_for_calendar'] = json.dumps(get_all_lesson_teacher(teacher))
            context['available_lesson'] = json.dumps(get_available_type_lesson(teacher))
            context['all_students'] = Student.objects.all()
        return context


teacher_view = TeacherView.as_view()


class UpdatePhotoTeacherView(UpdateView):
    model = Teacher
    form_class = PhotoTeacherForm
    template_name = 'pages/teacher.html'
    template_name_suffix = ''


update_photo_teacher_view = UpdatePhotoTeacherView.as_view()


class UpdateInfoTeacherView(UpdateView):
    model = Teacher
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


class CreateLessonView(CreateView):
    model = Lesson
    form_class = LessonForm
    template_name = 'pages/teacher.html'
    template_name_suffix = ''

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        return JsonResponse(form.errors, status=500)

    def form_valid(self, form):
        self.object = form.save()
        info_lesson = get_info_lesson_to_calendar(self.object)
        return JsonResponse({'status': 'ok', 'info': info_lesson})


create_lesson_view = CreateLessonView.as_view()


class UpdateLessonView(UpdateView):
    model = Lesson
    form_class = LessonForm
    template_name = 'pages/teacher.html'
    template_name_suffix = ''

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        return JsonResponse(form.errors, status=500)

    def form_valid(self, form):
        self.object = form.save()
        info_lesson = get_info_lesson_to_calendar(self.object)
        return JsonResponse({'status': 'ok', 'info': info_lesson})


update_lesson_view = UpdateLessonView.as_view()


def update_homework_file_view(request: HttpRequest):
    if request.POST:
        id_lesson = request.POST['lesson']

        lesson = Lesson.objects.get(id=id_lesson)
        HomeWorkFile.objects.filter(lesson=lesson).delete()
        for file in request.FILES:
            form = ModelFormWithFileField({'lesson': request.POST['lesson']}, {'homework_file': request.FILES[file]})
            if form.is_valid():
                # file is saved
                form.save()
            else:
                return JsonResponse(form.errors, status=500)
        return JsonResponse({'status': 'ok'})


def update_visitors_view(request: HttpRequest):
    if request.POST:
        id_lesson = request.POST['id_lesson']
        id_students = [int(re.search(r'id: (\d+)', request.POST[student]).group(1))
                       for student in request.POST.keys() if 'student' in student]

        lesson = Lesson.objects.get(id=id_lesson)
        Visitors.objects.filter(lesson=lesson).delete()

        for id_student in id_students:
            student = Student.objects.get(id=id_student)
            Visitors.objects.create(lesson=lesson, student=student)
        return JsonResponse({'status': 'ok'})


def get_free_times(request: HttpRequest, date: str):
    teacher = Teacher.objects.get(user=request.user)
    free_time = free_time_to_date(date, teacher)
    return JsonResponse({'free_time': free_time})


def get_select_lesson(request: HttpRequest, lesson_id: str):
    lesson = Lesson.objects.get(id=lesson_id)
    info = get_info_lesson_to_calendar(lesson)
    return JsonResponse(info)


class CreateLessonView(CreateView):
    model = HomeWorkFile
    form_class = LessonForm
    template_name = 'pages/teacher.html'
    template_name_suffix = ''

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        return JsonResponse(form.errors, status=500)

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)


create_lesson_view = CreateLessonView.as_view()
