import logging
from smtplib import SMTPException

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import EmailMessage
from django.template import Template, Context

from email_templates_manager.models import now
from email_templates_manager.models import Template as Template_Model

logger = logging.getLogger(__name__)


class EmailFromTemplate(object):

    def __init__(self, name="", from_email=settings.DEFAULT_FROM_EMAIL,
                 language=settings.LANGUAGE_CODE, subject="", template_class=Template_Model,
                 template_object=None):

        self.from_email = from_email
        self.template_class = template_class
        self.template_object = template_object
        self.subject = subject
        self.language = language
        self.name = name

        self.template = None
        self.compiled_template = None  # for storing compiled template
        self.context = {'date': now()}  # default context
        self.sent = 0  # number of messages sent
        self.message = ""
        self.content_subtype = 'html'
        self._template_source = 'default'


    def get_template_object(self):
        if self.template_object:
            return self.template_object
        return self.template_class.objects.get(title=self.name, language=self.language)

    def get_object(self):
        while True:
            try:
                tmp = self.get_template_object()
            except ObjectDoesNotExist:
                logger.warning("Can't find EmailTemplate object in database, using default file template.")
                break
            else:
                self.template = str(tmp.content)
                self.subject = str(tmp.subject) or self.subject
                self._template_source = 'database'
                logger.debug("Got template %s from database", self.name)
                return


    def __compile_template(self):
        if not self.compiled_template:
            self.compiled_template = Template(self.template)

    def render_message(self):
        self.__compile_template()
        try:
            message = self.compiled_template.render(self.context)  #
        except AttributeError:
            message = self.compiled_template.render(Context(self.context))
        self.message = message


    def send_email(self, send_to, fail_silently=True, *args, **kwargs):
        msg = EmailMessage(self.subject, self.message, self.from_email, send_to, *args, **kwargs)
        msg.content_subtype = self.content_subtype
        try:
            self.sent = msg.send()
        except SMTPException as e:
            if not fail_silently:
                raise
            logger.error('Problem sending email to %s: %s', send_to, e)
        return self.sent


    def send(self, to, *args, **kwargs):
        self.get_template_object()
        self.render_message()
        self.send_email(to, *args, **kwargs)
        if self.sent:
            logger.info("Mail has been sent to: %s ", to)
        return self.sent
