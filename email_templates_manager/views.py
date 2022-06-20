from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404
from django.template import Template, Context
from django.views.generic import TemplateView

from email_templates_manager.models import Template as Template_Model


class EmailPreviewView(TemplateView):

    template_name = 'email_preview.html'

    def get_email_template(self):
        return get_object_or_404(Template_Model, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        email_template = self.get_email_template()
        email_content = Template(email_template.content)
        rendered_content = email_content.render(Context(email_template.help_context))
        context = {'subject':email_template.subject, 'content':rendered_content}
        return context


email_preview_view = staff_member_required(EmailPreviewView.as_view())

