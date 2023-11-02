from django.urls import path

from chinglish.students.views import (
    student_view,
    update_info_student_view,
    update_photo_student_view,
    get_select_lesson
)

app_name = "students"
urlpatterns = [
    path("", view=student_view, name="profile"),
    path("update-photo/<int:pk>/", view=update_photo_student_view, name="update-photo"),
    path("update-info/<int:pk>/", view=update_info_student_view, name="update-info"),
    path("get_select_lesson/<int:lesson_id>/", view=get_select_lesson, name="get_info_lesson"),
]
