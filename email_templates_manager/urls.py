from django.conf.urls import url

from email_templates_manager.views import email_preview_view


urlpatterns = [
    url(r'^email-preview/(?P<pk>\d+)/$', email_preview_view, name='email_preview'),
]
