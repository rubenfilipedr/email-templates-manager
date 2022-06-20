from django import forms

from email_templates_manager.models import Template


class TemplateAdminForm(forms.ModelForm):
    class Meta:
        model = Template
        fields = [
            'title',
            'subject',
            'content',
            'language',
            'help_context',
            'created',
        ]

    def __init__(self, *args, **kwargs):
        super(TemplateAdminForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['title'].widget = forms.TextInput(attrs={'readonly': 'readonly'})
            self.fields['language'].widget = forms.TextInput(attrs={'readonly': 'readonly'})
