from django.urls import path

from chinglish.teachers.views import (
    teacher_view,
    update_photo_teacher_view,
    update_info_teacher_view
)

app_name = "teachers"
urlpatterns = [
    path("", view=teacher_view, name="profile"),
    path("update-photo/<int:pk>/", view=update_photo_teacher_view, name="update-photo"),
    path("update-info/<int:pk>/", view=update_info_teacher_view, name="update-info"),
]
