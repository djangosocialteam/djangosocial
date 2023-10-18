# django.social

Website for https://django.social project.

## Running in development mode

### Using Docker Compose

The easiest way to run the development server is to use [Docker Compose](https://docs.docker.com/compose/). This presumes you have Docker and Docker compose installed. Please refer to the [Docker installation instructions](https://docs.docker.com/engine/install/) or your operating system's documentation for details. I would recommend installing Docker Engine rather than Docker Desktop.

First, clone the repository:

```bash
git clone ...
cd djangosocial/
```

Copy the Docker Override file into the project's root directory:

```bash
cp -iv dev-templates/docker-compose.override.yml.tpl ./docker-compose.override.yml
```

Edit the file if needed, then you need to build the containers and run them.

You can do this manually:

```bash
docker compose up --build
# Note: if you have an older version of Docker, you may instead need to use:
docker-compose up --build
```

The server should now be running at http://localhost:8000, or whichever port you defined.

Alternatively there is a bash script to aid development, ``do.sh``.

The useful parts of the script to get going are:

* ``do.sh build`` - runs docker compose build
* ``do.sh start`` - runs docker compose up
* ``do.sh migrate`` - runs django migrations
* ``do.sh shell`` - starts a bash prompt in the app

### Running commands inside the python container

You can now run commands inside the python container by running:

```bash
./do.sh shell
```

This will give you access to the `bash` shell inside the container where you may run Django commands like:

```bash
python manage.py createsuperuser # to create and admin account
python manage.py makemigrations # to run migrations
python manage.py migrate # to apply migrations
python manage.py shell # to access the Django shell
```

### Utility functions from the bash script

* ``do.sh check`` - run django's check command in the container
* ``do.sh djshell`` - run django's shell command in the container
* ``do.sh migrate`` - run makemigrations from within the container
* ``do.sh makemigrations`` - run makemigrations from within the container
* ``do.sh pip-compile`` - compile the requirements from within the container
* ``do.sh pip-upgrade`` - compile the requirements with the upgrade flag

### Using a virtual environment

This section is a work in progress (and I haven't had time to test it properly yet), but you should be able to run this project inside a virtual environment like most Django projects. The general idea should be:

- Install and configure PostgreSQL.
- Clone the repository.
- Create a virtual environment.
- Activate the virtual environment.
- Install dependencies.
- Set environment variables.
- Run the development server inside the virtual environment.

TODO: Figure out if this causes conflicts with the media and static files, though `urls.py` should include a hack to avoid this.

### Running on Windows

TODO.

## Contributing

See the [CONTRIBUTING.md](CONTRIBUTING.md) file for details.
