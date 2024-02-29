web: gunicorn djangosocial.wsgi:application --bind 0.0.0.0:$PORT --timeout 300 --chdir django
release: python django/manage.py migrate
