from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class EmailTemplatesManagerConfig(AppConfig):
    name = "email_templates_manager"

    verbose_name = _("Email Template Manager")

    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):
        pass


