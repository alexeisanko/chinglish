from django.urls import path
from chinglish.main.views import home_view, trial_lesson_create_view

app_name = "main"

urlpatterns = [
    path("", view=home_view, name="home"),
    path("create_trial_lesson/", view=trial_lesson_create_view, name="create_trial_lesson"),
]
