<br>
<h1 align="center"> База знаний </h1>
<p align="center"> </p>

***В проекте используются следующие технологии:***

    - Python 3.9.4
    - Django 3.2.9
    - PostgreSQL 14

***О проекте***<br>

    Проект предназначен для сбора и хранения полезных статей/документов организации, разбитых по категориям.
    Данная версия проекта является тестовой (был собран образ и запущен с использованием Docker)

***Примечание***

***Запуск проекта:***

    git clone https://github.com/Evgenqr/forwork_docker

    cd forwork_docker

    python -m venv venv

    venv\scripts\activate

    docker compose build

    docker compose up -d

    (для остановки выполнить команду docker compose down)

    (для просмотра логов выполнить команду docker compose logs -f)