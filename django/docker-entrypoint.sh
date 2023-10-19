# Entrypoint for docker
set -e
python await_pg.py
python manage.py migrate --no-input
python manage.py collectstatic --no-input

if [ "$STAGE" = "dev" ]; then
  echo Running in dev mode...
  python manage.py runserver 0.0.0.0:8000
else
  gunicorn djangosocial.wsgi:application --bind 0.0.0.0:8000
fi
