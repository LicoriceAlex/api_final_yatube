# Api для социальной сети Yatube
### Описание
Api позволяет публиковать посты с указанием группы и добавлением изображения, оставлять комментарии под постами, подписываться на других пользователей. Подключена паджинация для просмотра постов. Авторизованные пользователи могут просматривать свои подписки.
### Технологии
Python 3.7
Django 2.2.16
djangorestframework 3.12.4
djangorestframework-simplejwt 4.7.2
PyJWT 2.1.0
### Запуск проекта в dev-режиме
Cоздать и активировать виртуальное окружение:
```
python3 -m venv env
```
```
source env/bin/activate
```
Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
Выполнить миграции:
```
python3 manage.py migrate
```
Запустить проект:
```
python3 manage.py runserver
```
### Авторы
 Саша Савин