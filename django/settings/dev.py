from .base import *

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

# Make sure we don't send emails in dev if ever implemented
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass
