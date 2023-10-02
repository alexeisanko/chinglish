from typing import Any, Dict

from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from chinglish.students.models import Student


class StudentView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/student.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user:
            context['student'] = Student.objects.get_or_create(user=user)
        return context


student_view = StudentView.as_view()
