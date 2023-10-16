from django.urls import path

from chinglish.teachers.views import (
    teacher_view,
    update_photo_teacher_view,
    update_info_teacher_view,
    update_lesson_view,
    update_visitors_view,
    update_homework_file_view

)

app_name = "teachers"
urlpatterns = [
    path("", view=teacher_view, name="profile"),
    path("update-photo/<int:pk>/", view=update_photo_teacher_view, name="update-photo"),
    path("update-info/<int:pk>/", view=update_info_teacher_view, name="update-info"),
    path("update_lesson/", view=update_lesson_view, name="update_lesson"),
    path("update_homeworkfile/", view=update_homework_file_view, name="update_homework_file"),
    path("update_visitors/", view=update_visitors_view, name="update_visitors"),

]
