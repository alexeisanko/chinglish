from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class TeacherView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/teacher.html'


teacher_view = TeacherView.as_view()
