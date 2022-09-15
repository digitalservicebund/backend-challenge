# DigitalServiceBund Backend code challenge

Backend stack providing a single endpoint and a template to visualize the 
aggregated dataset counts for each ministry and its subordinates.

## Backend Requirements

* [Docker](https://www.docker.com/).
* [Poetry](https://python-poetry.org/) for Python package and environment management.

**Recommended tools**

* [pyenv](https://github.com/pyenv/pyenv)

## Run

* Navigate to app folder:

```commandline
cd app/
```

* Build Docker image:

```commandline
make backend-image
```

* Start the stack:

```commandline
make run-docker
```

* Remove container after stopping:

```commandline
docker container rm dsb-backend
```

* See README inside app folder for details on how to run in development mode 