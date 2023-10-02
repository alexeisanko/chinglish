from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class StudentsConfig(AppConfig):
    name = "chinglish.students"
    verbose_name = _("Students")

    def ready(self):
        try:
            import chinglish.students.signals  # noqa F401
        except ImportError:
            pass
