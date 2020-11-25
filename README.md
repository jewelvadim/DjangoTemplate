# README

Этот README описывает шаги, необходимые для создания и запуска веб-приложения.

## Требования

* python 3.9+
* django 2.2+
* postgresql 12+
* docker
* docker-compose

## Установка

* Склонируйте репозиторий

### Используя Docker

* Создайте файл .env, содержащий все необходимые переменные окружения.
* Соберите контейнеры
```shell script
$ docker-compose build
```
* Примените миграции

### Без Docker

* Создайте виртуальное окружение для python3 и активируйте его
```shell script
$ virtualenv -p python3 env
$ source env/bin/activate
```
* Экспортируйте переменные окружения
* Установите зависимости
```shell script
$ pip install -r requirements.txt
```
* Создайте локальную базу данных 
```shell script
$ sudo su postgres
$ psql
$ create user username with encrypted password 'userpassword';
$ create database dbname;
$ grant all privileges on database dbname to username;
```
* Примените миграции
```shell script
$ python manage.py migrate
```

### Для pycharm
* Установить в настройках интерпритатор из docker-compose или виртуального окружения
* Переименовать project именем проекта
* Инициализировать новый репозиторий
* Отметить папку project как source root

## Запуск

* Для запуска в docker
```shell script
$ docker-compose up
```
* Для запуска локально
```shell script
$ source env/bin/activate
$ python manage.py runserver 0.0.0.0:8000
```

## Особенности

### Переменные окружения

* **RECAPTCHA_PRIVATE_KEY** - *google recaptcha private key*
* **RECAPTCHA_PUBLIC_KEY** - *google recaptcha public key*
* **EMAIL_HOST** - *gmail email address*
* **EMAIL_HOST_PASSWORD** - *gmail password or gmail app password(preferable)*
* **TILDA_PUBLIC_KEY** - *tilda api public key*
* **TILDA_PRIVATE_KEY** - *tilda api private key*
* **DB_NAME** - *PostgreSQL database name*
* **DB_USER** - *PostgreSQL database username*
* **DB_PASSWORD** - *PostgreSQL database password*
* **SECRET** - *Django project secret key*

### Менеджмент команды

* thumbnail [command]
    - clear_delete_all - *delete all thumbnail files including any orphans not in the Key Value Store.*

### Крон задачи (периодические)

### Extra

Не удаляйте файлы внутри папки **migrations** - проект содержит дата-миграции (0002_data). 
Вместо этого сделайте zero миграции при необходимости.

### Fabric

Файл `fabfile.py` содержит ряд функций, которые помогают при локальной разработке.

Установка: 
```shell script
$ pip install Fabric3
```

##### Команды fabric

* `fab dev` - запустить локально веб приложение
* `fab makemigrations` - создать файл миграций
* `fab migrate` - применить миграции
* `fab createsuperuser` - создать суперпользователя
* `fab shell` - зайти в shell django приложения
* `fab bash` - зайти в bash контейнера server
* `fab kill` - остановить все запущенные контейнеры

## Деплой

Тут будет информация о деплое. Наш стек: **nginx** + **supervisord** + **gunicorn**

## Авторы

Разработано в [Alente](https://alente.ru/)

* **Vadim Beglov** - *Lead-backend*
