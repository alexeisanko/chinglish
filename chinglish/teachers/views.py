from typing import Any, Dict

from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from chinglish.teachers.models import Teacher
from chinglish.teachers.forms import PhotoTeacherForm


class TeacherView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/teacher.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user:
            context['teacher'], created = Teacher.objects.get_or_create(user=user)

        return context


teacher_view = TeacherView.as_view()


class UpdatePhotoTeacherView(UpdateView):
    model = Teacher
    form_class = PhotoTeacherForm
    template_name = 'pages/teacher.html'
    template_name_suffix = ''

update_photo_teacher_view = UpdatePhotoTeacherView.as_view()
