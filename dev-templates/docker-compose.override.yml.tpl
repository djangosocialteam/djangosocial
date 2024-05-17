# Local dev overrides
services:
  djangosocial-django:
    build:
      target: django-dev
    environment:
      - DJANGO_DEBUG=True
      - DJANGO_LOG_LEVEL=DEBUG
      - DJANGO_SECRET_KEY=NotReallySecret
      - POSTGRES_DB=djangosocial
      - POSTGRES_HOST=djangosocial-postgres
      - POSTGRES_PASSWORD=djangosocial
      - POSTGRES_USER=djangosocial
    volumes:
      - ./djangosocial:/django/
  djangosocial-postgres:
    environment:
      - POSTGRES_DB=djangosocial
      - POSTGRES_PASSWORD=djangosocial
      - POSTGRES_USER=djangosocial
