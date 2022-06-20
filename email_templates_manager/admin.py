from django.contrib import admin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe

from email_templates_manager.models import Template
from email_templates_manager.forms import TemplateAdminForm


class TemplateAdmin(admin.ModelAdmin):
    form = TemplateAdminForm
    readonly_fields = ['show_links', 'created']

    def show_links(self, obj):
        if not obj.pk:
            return ''
        return mark_safe('<a href="%s" target="_blank">%s</a>' % (
            reverse('email_preview', kwargs={'pk': obj.pk}), _('Show email preview')
        ))

    show_links.allow_tags = True
    show_links.short_description = _('Actions')

admin.site.register(Template, TemplateAdmin)
