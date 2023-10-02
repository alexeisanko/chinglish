from django.urls import path

from chinglish.students.views import (
    student_view,
)

app_name = "students"
urlpatterns = [
    path("", view=student_view, name="profile"),
]
