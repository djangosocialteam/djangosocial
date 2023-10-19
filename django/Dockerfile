# Wagtail Dockerfile
# Python image to use
ARG PYTHON_IMAGE=python:3.12-slim-bookworm

FROM ${PYTHON_IMAGE} as django-base
# The uid for your user account
ENV DEV_UID=1000
# Create base dirs
RUN useradd -md /django -u ${DEV_UID} python
WORKDIR /django
# Install system packages required by Wagtail and Django.
RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
  build-essential \
  libpq-dev \
  libjpeg62-turbo-dev \
  zlib1g-dev \
  libwebp-dev \
  && rm -rf /var/lib/apt/lists/*
# Install common requirements
COPY requirements.txt /tmp/requirements.txt
RUN python -m pip install -r /tmp/requirements.txt && rm /tmp/requirements.txt

# Dev stage
FROM django-base as django-dev
COPY requirements-dev.txt /tmp/requirements.txt
RUN python -m pip install pip-tools
RUN python -m pip install -r /tmp/requirements.txt && rm /tmp/requirements.txt
USER python
ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]
