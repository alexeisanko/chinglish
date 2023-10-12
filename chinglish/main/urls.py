from django.urls import path
from chinglish.main.views import home_view, free_times_for_record_view

app_name = "main"

urlpatterns = [
    path("", view=home_view, name="home"),
    path("free_date_time/<int:teacher_id>/", view=free_times_for_record_view, name="free_date_time"),
]
