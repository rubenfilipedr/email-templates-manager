
# Email Templates Manager

***

email-templates-manager is a Django app that manages email templates

## Getting started

***

To make it easy for you to get started, here's a list of recommended steps.

## Installation

***

1. Add "email_templates_manager" to your INSTALLED_APPS settings:

```python
INSTALLED_APPS = [
    ...
    'email_templates_manager',
]
```

2. Run ``python manage.py migrate email_templates_manager`` to install package models.

## Usage

***

```python
from email_templates_manager.shortcuts import send_email

send_email(name="template_name", ctx_dict={"username": "Username"}, 
           send_to=["example@example.com"], subject="Subject")
```
