from django.urls import path

from chinglish.teachers.views import (
    teacher_view,
)

app_name = "teachers"
urlpatterns = [
    path("", view=teacher_view, name="profile"),
]
