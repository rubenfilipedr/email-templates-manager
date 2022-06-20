from email_templates_manager.email import EmailFromTemplate


def send_email(name, ctx_dict, send_to=None, subject='Subject', **kwargs):
    eft = EmailFromTemplate(name=name)
    eft.subject = subject
    eft.context = ctx_dict
    eft.get_object()
    eft.render_message()
    eft.send_email(send_to=send_to, **kwargs)


# send_email(name="nome_template", ctx_dict={"username": "teste"}, send_to=["example@example.com"], subject="Test")
