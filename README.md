# User REST API
Test task for the position of Python backend developer, to implement a user API on Django REST Framework. 
During the test task, the following RESTful API endpoints were developed: user registration, login, 
getting a user profile, updating a user profile, and deleting an account using Django Rest Framework (DRF). 
Implemented password storage in encrypted form using the Django Argon encryption algorithm. 
Authorization was developed on the basis of sending OTP codes with a limited validity period to the user's email 
using Celery.

### Stack:
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Celery](https://img.shields.io/badge/celery-%23a9cc54.svg?style=for-the-badge&logo=celery&logoColor=ddf4a4)
![Gunicorn](https://img.shields.io/badge/gunicorn-%298729.svg?style=for-the-badge&logo=gunicorn&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![RabbitMQ](https://img.shields.io/badge/Rabbitmq-FF6600?style=for-the-badge&logo=rabbitmq&logoColor=white)
![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white)
![Flower](https://img.shields.io/badge/flower-8bca59?style=for-the-badge&logo=hulu&logoColor=white)
![pgAdmin](https://img.shields.io/badge/pgAdmin-598bca?style=for-the-badge&logo=hulu&logoColor=white)



## Installation

To deploy the project, use`docker-compose.yml`. Make sure you have [Docker installed](#installing-docker) and Docker Compose.

Clone the project from Github:
```bash
git clone git@github.com:Mist3s/user_restfull_api.git
```
Create a ".env" file in the project root, filling example:
```text
POSTGRES_USER=django_user
POSTGRES_PASSWORD=mysecretpassword
POSTGRES_DB=django
DB_HOST=db_host
DB_PORT=5432
SECRET_KEY='django-insecure-b9)zjp+%-wty5656gfdh5pw4qr(-452xrn_xrlinz^!+@=dk&96'
DEBUG=False
PGADMIN_DEFAULT_EMAIL=admin@email.com
PGADMIN_DEFAULT_PASSWORD=adminpassword
RABBITMQ_DEFAULT_USER=rabbitmq
RABBITMQ_DEFAULT_PASS=rabbitmq
```

Run Docker Compose with this configuration on your machine
```bash
docker compose up -d
```
Run the migrations, collect the backend static files and copy them to /static/static/:
```bash
sudo docker compose exec backend python manage.py makemigrations
```
```bash
sudo docker compose exec backend python manage.py migrate
```
```bash
sudo docker compose exec backend python manage.py collectstatic
```
```bash
sudo docker compose exec backend cp -r /app/static/. /static/static/
```
API documentation is available at:
[user-restfull-api.mist3s.site/api/v1/docs/](https://user-restfull-api.mist3s.site/api/v1/docs/)
or locally
[127.0.0.1:8000/api/v1/docs/](http://127.0.0.1:8000/api/v1/docs/)



## Installing Docker

<details>
<summary>Installation on Ubuntu</summary>

1. ```bash
    sudo apt-get update
   ```
2. ```bash
    sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common
   ```
3. ```bash
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
   ```
4. ```bash
    echo "deb [signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
   ```
5. ```bash
    sudo apt-get update
   ```
6. ```bash
    sudo apt-get install -y docker-ce docker-ce-cli containerd.io
   ```
7. ```bash
    sudo usermod -aG docker $USER
   ```
8. ```bash
    sudo reboot
   ```
</details>

<details>
<summary>Installation on Windows</summary>

1. Download the Docker Desktop installer from [the official Docker website](https://www.docker.com/products/docker-desktop) and install it.
2. Launch Docker Desktop after installation.

</details>

<details>
<summary>Installation on macOS</summary>

1. Download the Docker Desktop installer from [the official Docker website](https://www.docker.com/products/docker-desktop) and install it.
2. Launch Docker Desktop after installation.

</details>

## About the author
Python developer

[Andrey Ivanov](https://github.com/Mist3s)
