# skypro_coursework_djangro

## Описание проекта
Данное веб-приложение представляет собой сервис управления рассылками, администрирования и получения статистики ('SkyForest').
Которое используется для того, чтобы удерживать текущих клиентов (вспомогательными или «прогревающими» рассылками), 
а так же рассылки для информирования и привлечения клиентов.

## Развертывание проекта
Для корректной работы проекта, вам необходимо выполнить следующие шаги:

1) Установить локально на свой компьютер Python версией не ниже 3.10.x!
2) Клонировать файлы проекта с GitHub репозитория.
3) Установите виртуальное окружение.
```bash
python -m venv venv 
```
4) Активировать виртуальное окружение (если есть необходимость).
```bash
venv/Scripts/activate.bat 
```
5) Установить необходимые зависимости проекта, указанные в файле `requirements.txt`
```bash
pip install -r requirements.txt
```
6) Установить Redis, глобально себе на компьютер (используйте wsl, терминал Ubuntu).
```bash
sudo apt-get install redis-server
```
7) Запустить Redis-сервер (Redis-сервер запустится на стандартном порту 6379).
```bash
sudo service redis-server start
```
8) Убедиться, что Redis-сервер работает правильно, выполните команду:
```bash
redis-cli ping
```
9) Установить БД PostreSQL (используйте wsl, терминал Ubuntu).
```bash
sudo apt-get install postgresql
```
10) Если БД PostreSQL уже была ранее установлена, то перезапустите сервер PostreSQL.
```bash
sudo service postgresql restart
```
11) Выполнить вход.
```bash
sudo -u postgres psql
```
12) Создать базу данных с помощью следующей команды:
```bash
create database skyforest;
```
Если такая база данных уже используется, то возможно изменить ее название на свою.

13) Выйти.
```bash
\q
```
14) Создать файл .env
15) Добавить в файл настройки, как в .env.sample и заполнить их.
16) Применить миграции (локально, у себя в виртуальном окружении проекта).
```bash
python manage.py migrate users
```
```bash
python manage.py migrate
```
17) Запустить сервер (появившуюся ссылку открыть в браузере  http://127.0.0.1:8000/ )
```bash
python manage.py runserver
```
## Для запуска рассылок используется библиотека django-crontab. Она позволяет запускать задачи по расписанию.
18) Запустить Crontab (используйте wsl, терминал Ubuntu).
```bash
sudo service cron start
```
19) Для запуска рассылки из командной строки используйте команду:
```bash
python manage.py sending
```
* Разовые рассылки отправляются автоматически (при статусе - создана).
* Настройки периодических рассылок содержатся в файле settings.py, параметр "CRONJOBS".
