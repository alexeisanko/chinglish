from typing import Any, Dict

from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse

from chinglish.students.models import Student
from chinglish.students.forms import InfoStudentForm, PhotoStudentForm


class StudentView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/student.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user:
            context['user_info'], created = Student.objects.get_or_create(user=user)
            context['form_user_data'] = InfoStudentForm()
            context['form_user_photo'] = PhotoStudentForm()
        return context


student_view = StudentView.as_view()


class UpdatePhotoStudentView(UpdateView):
    model = Student
    form_class = PhotoStudentForm
    template_name = 'pages/student.html'
    template_name_suffix = ''


update_photo_student_view = UpdatePhotoStudentView.as_view()


class UpdateInfoStudentView(UpdateView):
    model = Student
    form_class = InfoStudentForm
    template_name = 'pages/student.html'
    template_name_suffix = ''

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        return JsonResponse(form.errors, status=500)

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        return JsonResponse({'status': 'ok'})


update_info_student_view = UpdateInfoStudentView.as_view()
