from django.urls import path
from chinglish.main.views import home_view, trial_lesson_create_view, load_homework

app_name = "main"

urlpatterns = [
    path("", view=home_view, name="home"),
    path("create_trial_lesson/", view=trial_lesson_create_view, name="create_trial_lesson"),
    path("load_homework/<int:id_homework_file>/", view=load_homework, name="load_homework")
]
