web: gunicorn wsgi:application --bind 0.0.0.0:$PORT --timeout 300 --chdir djangosocial
release: python djangosocial/manage.py migrate
