# Python Web Application

Implementation of web application using Flask and generating a Docker Image and container to support cross-platform.

Reference of the websites generated by the web application:

``` bash
  localhost:8000/home (Home Page)
  localhost:8000/data (Get url and view_count of a given website)
  localhost:8000/process (Get process and CPU Utilization of the Container)
```
## Commands

#### Build Image

```http
  docker build .
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `.` | `Object` | **Required**. Builds Docker Image based on Dockerfile of current folder |

#### Start Container

```http
  docker compose up
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `compose`      | `Object` | **Required**. Start container based on compose file in current folder |

#### pip3 freeze > requirements.txt

Generate all libraries used in Python and save into text file

#### pip3 install -r requirements.txt

Installs all libraries listed in requirements.txt 

#### flask run

Start python application (app.py) in current folder
## Authors

- [@jmandawi](https://www.linkedin.com/in/jeffandawi/)
## Environment Variables

Dockerfile contains the following environment variables:

`FLASK_APP=app.py`

`FLASK_RUN_HOST=0.0.0.0`
## Run Locally

Download the project and unzip

```bash
  sudo apt install unzip
  unzip PythonApp-Docker.zip
```

Go to the project directory and build image

```bash
  cd app
  docker build .
```

Run container

```bash
  docker compose up
```
## Deployment

Check website

To check website generated by web application

```bash
  localhost:8000/home
  localhost:8000/data
  localhost:8000/process
```

Check config files

To check config files (pid.conf) inside running container

```bash
  docker ps -a
  docker exec -it <container tag> /bin/sh
  cat /etc/pid.conf
```
## Documentation

[Documentation](https://docs.docker.com/compose/gettingstarted/)
## Tech Stack

**Client:** Python, Flask, Ubuntu WSL 2

**CSS:** Bootstrap 5

**Container:** Docker