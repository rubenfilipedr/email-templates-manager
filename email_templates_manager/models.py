from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


try:
    from django.utils.timezone import now
except ImportError:
    from datetime import datetime

    now = datetime.now


class Template(models.Model):
    title = models.CharField(_('Template'), max_length=255)
    subject = models.CharField(_('Subject'), max_length=255, blank=True)
    content = models.TextField(_('Content'))
    language = models.CharField(_('Language'), max_length=10, choices=settings.LANGUAGES, default=settings.LANGUAGE_CODE)
    help_context = models.JSONField(_('Help Context'), null=True, blank=True,
                                    help_text='{"username": "Name of user in hello expression"}', default=dict)
    created = models.DateTimeField(default=now)

    class Meta:
        unique_together = (('title', 'language'),)

    def __str__(self):
        return '%s (%s)' % (self.title, self.language)
