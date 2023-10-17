#!/bin/bash

COLUMNS="`tput cols`"
LINES="`tput lines`"
BOLD=$(tput bold)
NORMAL=$(tput sgr0)

DOCKER_COMPOSE="docker compose"

_requires() {
    service="$1"
    $DOCKER_COMPOSE ps -q $service &> /dev/null
    if [[ "$?" == 1 ]]; then
        echo "'$service' service is not running. Please run \`start\` first."
        exit 1
    fi
}

bounce() {
    stop
    build
    start
}

build() {
    $DOCKER_COMPOSE build --force-rm \
        "${@:1}"
}

check() {
    _requires djangosocial-django
    exec djangosocial-django django-admin check "$@"
}

compose() {
    $DOCKER_COMPOSE "$@"
}

djshell() {
    _requires djangosocial-django
    exec djangosocial-django django-admin shell "$@"
}

makemigrations() {
    _requires djangosocial-django
    exec djangosocial-django django-admin makemigrations "$@"
}

migrate() {
    _requires djangosocial-django
    exec djangosocial-django python -m manage migrate "$@"
}

pip-compile() {
    _requires djangosocial-django
    exec djangosocial-django pip-compile --generate-hashes "$@"
}

pip-upgrade() {
    _requires djangosocial-django
    exec djangosocial-django pip-compile --generate-hashes -U "$@"
}

shell() {
    _requires djangosocial-django
    exec djangosocial-django /bin/bash
}

start() {
    $DOCKER_COMPOSE up "$@"
}

stop() {
    $DOCKER_COMPOSE down "$@"
}

exec() {
    $DOCKER_COMPOSE exec -e COLUMNS -e LINES "$@"
}

_usage() {
    cat <<USAGE
Convenience wrapper around docker-compose.

Usage:

    ${BOLD}build${NORMAL}

        Builds all the images (or the ones specified) for running

    ${BOLD}check${NORMAL}

        Validate Django settings

    ${BOLD}compose${NORMAL}

        Minimal wrapper around docker-compose, just ensures the correct config files are loaded.

    ${BOLD}djshell${NORMAL}

        Opens a Django shell

    ${BOLD}exec${NORMAL} [<arg>]

        Execute a command in a container

    ${BOLD}makemigrations${NORMAL} [<arg>]

        Create a new Django migration, using the given args

    ${BOLD}migrate${NORMAL} [<arg>]

        Apply any unapplied Django migrations

    ${BOLD}pip-compile${NORMAL} [<arg>]

        This will re-compile the python requirements from the current requirements.in file
        This is good to do if you add a new requirement, but don't want to upgrade any others when compiling requirements.txt
        https://github.com/jazzband/pip-tools#pip-tools--pip-compile--pip-sync

    ${BOLD}pip-upgrade${NORMAL}

        This will re-compile the python requirements from the current requirements.in file while also including the upgrade flag.
        Therefore requirements.txt will be generated with newer versions of packages which aren't pinned

    ${BOLD}shell${NORMAL}

        Opens a bash terminal in djangosocial-django

    ${BOLD}start${NORMAL} [<arg>]

        Start the django server (and dependent services)
        You can pass `-d` for running detached.

    ${BOLD}stop${NORMAL} [<arg>]

        Stop the django server (and dependent services)

USAGE
}

if [ "$1" == "" ]; then
    _usage;
fi

$*
