from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import RedirectView, UpdateView

from chinglish.students.models import Student
from chinglish.teachers.models import Teacher

User = get_user_model()


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = User
    fields = ["email"]
    success_message = _("Information successfully updated")

    def get_success_url(self):
        assert (
            self.request.user.is_authenticated
        )  # for mypy to know that the user is authenticated
        return self.request.user.get_absolute_url()

    def get_object(self):
        return self.request.user


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):

    permanent = False

    def get_redirect_url(self):
        student = Student.objects.filter(user=self.request.user)
        teacher = Teacher.objects.filter(user=self.request.user)
        if teacher:
            return reverse('teachers:profile')
        elif student:
            return reverse('students:profile')
        else:
            return reverse('students:profile')


user_redirect_view = UserRedirectView.as_view()
