from typing import Any, Dict

from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from chinglish.teachers.models import Teacher


class TeacherView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/teacher.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user:
            context['teacher'], created = Teacher.objects.get_or_create(user=user)

        return context


teacher_view = TeacherView.as_view()


class UpdateTeacherView(UpdateView):
    model = Teacher
