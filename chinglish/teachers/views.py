from typing import Any, Dict

from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse

from chinglish.teachers.models import Teacher
from chinglish.teachers.forms import PhotoTeacherForm, InfoTeacherForm


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
