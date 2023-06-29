Документация к проекту API_YamDB
=====

Описание проекта
----------
REST API для сервиса YaMDb — базы отзывов о фильмах, книгах и музыке.

Реализован с помощью REST API, для аутентификации применяются JWT-токены.

----------
Стек технологий
* Python 3.7
* Django 2.2
* Django Rest Framework
* Pytest
* Simple-JWT
----------
Установка проекта на Windows
----------
1. Клонировать репозиторий
```bash
git clone https://github.com/Glebastaa/api_yamdb.git

cd api_final_yatube
```
2.Создать и активировать вирутальное окружение:
```bash
python -m venv venv

. venv/Scripts/activate
```
3.Установить зависимости из файла ```requirements.txt```
```bash
pip install -r requirements.txt
```
4. Выполнить миграции:
```bash
cd yatube_api

python manage.py migrate
```
5. Запустить проект:
```bash
python manage.py runserver
```
Документация к проекту
----------
Документация для API после установки доступна по адресу ```/redoc/```.
