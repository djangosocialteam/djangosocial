# Nginx Dockerfile for Django.social
ARG NGINX_IMAGE=nginx:stable

FROM ${NGINX_IMAGE} as nginx-dev
# Copy the config file. Edit it as needed.
COPY nginx.dev.conf /etc/nginx/nginx.conf

FROM ${NGINX_IMAGE} as nginx-prod
COPY nginx.conf /etc/nginx/nginx.conf
