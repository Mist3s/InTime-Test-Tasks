# User REST API
Тестовое задание на должность Python backend-developer, реализовать API пользователя на Django REST Framework. 
В ходе выполнения тестового задания были разработаны конечных точек RESTful API регистрации пользователей, 
входа в систему, получения профиля пользователя, обновления профиля пользователя и удаления учетной записи с 
помощью Django Rest Framework (DRF). Внедрено хранение паролей в зашифрованном виде c использованием алгоритма 
шифрования Django Argon. Разработана авторизация на основе отправки OTP кодов с ограниченным срокам действия 
на почту пользователю используя Celery.

### Стек:
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Celery](https://img.shields.io/badge/celery-%23a9cc54.svg?style=for-the-badge&logo=celery&logoColor=ddf4a4)
![Gunicorn](https://img.shields.io/badge/gunicorn-%298729.svg?style=for-the-badge&logo=gunicorn&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![RabbitMQ](https://img.shields.io/badge/Rabbitmq-FF6600?style=for-the-badge&logo=rabbitmq&logoColor=white)


## Установка

Для развертывания проекта, используйте `docker-compose.yml`. Убедитесь, что у вас [установлен Docker](#установка-docker) и Docker Compose.

Клонируйте проект из гитхаба:
```bash
git clone git@github.com:Mist3s/InTime-Test-Tasks.git
```
В корне проекта создать файл ".env", пример заполнения:
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
```

Запустите Docker Compose с этой конфигурацией на своём компьютере
```bash
docker compose up -d
```
Выполните миграции, соберите статические файлы бэкенда и скопируйте их в /static/static/:
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
## Установка Docker

<details>
<summary>Установка на Ubuntu</summary>

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
<summary>Установка на Windows</summary>

1. Скачайте установщик Docker Desktop с [официального сайта Docker](https://www.docker.com/products/docker-desktop) и выполните его установку.
2. Запустите Docker Desktop после установки.

</details>

<details>
<summary>Установка на macOS</summary>

1. Скачайте установщик Docker Desktop с [официального сайта Docker](https://www.docker.com/products/docker-desktop) и выполните его установку.
2. Запустите Docker Desktop после установки.

</details>

## Об авторе
Python-разработчик

[Андрей Иванов](https://github.com/Mist3s)