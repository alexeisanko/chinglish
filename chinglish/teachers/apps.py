from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TeachersConfig(AppConfig):
    name = "chinglish.teachers"
    verbose_name = _("Teachers")

    def ready(self):
        try:
            import chinglish.teachers.signals  # noqa F401
        except ImportError:
            pass
