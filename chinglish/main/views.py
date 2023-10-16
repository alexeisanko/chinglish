from typing import Any, Dict
import json

from django.views.generic import TemplateView, CreateView
from django.http import JsonResponse


from chinglish.main.models import TrialLesson
from chinglish.main.forms import TrialLessonForm
from chinglish.main.utilities import get_free_teacher_for_trial_lesson


class HomeView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user:
            context['form'] = TrialLessonForm
            available_type_lesson, free_time_teachers = get_free_teacher_for_trial_lesson()
            lessons = json.dumps(available_type_lesson)
            free_times = json.dumps(free_time_teachers)
            context['available_type_lesson'] = lessons
            context['free_time_teachers'] = free_times
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

