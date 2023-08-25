from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MainConfig(AppConfig):
    name = "chinglish.main"
    verbose_name = _("Main")

    def ready(self):
        try:
            import chinglish.users.signals  # noqa F401
        except ImportError:
            pass
