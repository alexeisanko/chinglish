from django.urls import path

from chinglish.teachers.views import (
    teacher_view,
)

app_name = "teacher"
urlpatterns = [
    path("", view=teacher_view, name="profile"),
]
