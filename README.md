# Blogicum

Проект блога, реализованный с использованием Django. В проекте можно просматривать записи по категориям, всю ленту записей от новых к старым, ознакомиться с правилами и прочесть информацию о нас.

## Автор
https://github.com/Atsaev/

## Стек технологий

- Python 3.12
- Django 5.1.1
- HTML, CSS

## Структура проекта
├── blog
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-312.pyc
│   │   ├── admin.cpython-312.pyc
│   │   ├── apps.cpython-312.pyc
│   │   ├── models.cpython-312.pyc
│   │   ├── urls.cpython-312.pyc
│   │   └── views.cpython-312.pyc
│   ├── apps.py
│   ├── migrations
│   │   ├── __init__.py
│   │   └── __pycache__
│   ├── urls.py
│   └── views.py
├── blogicum
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-312.pyc
│   │   ├── settings.cpython-312.pyc
│   │   ├── urls.cpython-312.pyc
│   │   └── wsgi.cpython-312.pyc
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
├── pages
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-312.pyc
│   │   ├── admin.cpython-312.pyc
│   │   ├── apps.cpython-312.pyc
│   │   ├── models.cpython-312.pyc
│   │   ├── urls.cpython-312.pyc
│   │   └── views.cpython-312.pyc
│   ├── apps.py
│   ├── migrations
│   │   ├── __init__.py
│   │   └── __pycache__
│   └── urls.py
├── static
│   ├── css
│   │   └── bootstrap.min.css
│   └── img
│       ├── fav
│       └── logo.png
└── templates
    ├── base.html
    ├── blog
    │   ├── category.html
    │   ├── detail.html
    │   └── index.html
    ├── includes
    │   ├── article.html
    │   ├── footer.html
    │   └── header.html
    └── pages
        ├── about.html
        └── rules.html

## Запуск проекта

1. Клонируйте репозиторий:

```bash
git clone https://github.com/Atsaev/django-sprint1.git
cd blog
```
2. Установите зависимости

```bash
pip install -r requirements.txt
```
3. Примените миграции для базы данных:
```bash
python manage.py migrate
```
4. Запустите сервер разработки:
```bash
python manage.py runserver
```
5. Перейдите в браузере:
Откройте http://127.0.0.1:8000/ — Главная страница блога, список всех записей.

