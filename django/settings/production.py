import os
from .base import *

import dj_database_url


try:
    from .local import *
except ImportError:
    pass

STATIC_ROOT = BASE_DIR / ".." / "static"
MIDDLEWARE += [
    "whitenoise.middleware.WhiteNoiseMiddleware",
]


ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(",")


DATABASES = {
    "default": dj_database_url.config(
        conn_max_age=600,
        conn_health_checks=True,
    ),
}
