from typing import Any, Dict

from django.views.generic import TemplateView, CreateView
from django.http import JsonResponse, HttpRequest

from chinglish.main.models import TrialLesson
from chinglish.main.forms import TrialLessonForm
from chinglish.main.utilities import  get_teacher_for_trial_lesson, get_free_date_time


class HomeView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user:
            context['form'] = TrialLessonForm
            teacher_for_trial = get_teacher_for_trial_lesson()
            context['teacher_for_trial'] = teacher_for_trial
        return context


home_view = HomeView.as_view()


class TrialLessonCreateView(CreateView):
    model = TrialLesson
    form_class = TrialLessonForm
    template_name = 'home.html'
    template_name_suffix = ''

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        return JsonResponse(form.errors, status=500)

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        return JsonResponse({'status': 'ok'})


trial_lesson_create_view = TrialLessonCreateView.as_view()


def free_times_for_record_view(request: HttpRequest, teacher_id):
    free_date_time = get_free_date_time(teacher_id)
    return JsonResponse(free_date_time)
