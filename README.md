# 📁 Django My Site

## 📖 Кратко о проекте

По сути, сказать тут нечего. Просто личный сайт (без запуска на сервере) с возможностями микроблога. Планов серьезных на него нет.

upd: планы некоторым образом поменялись. Возможно этот проект я как раз доведу до деплоинга на сервер. + Возможности сайта уже расширились как минимум до личного списка с призведениями (играми, книгами, сериалами и т.д.)

---

## 🧾 TODO список (основные положения)

- [x] Инициировать проект (окружение, настройки, тестовый вывод домашней стр. и др.).
- [x] CRUD для микроблога. (Не совсем CRUD, потому как я убрал update с сайта, заменив его на change из админ-панели)
- [ ] Страница с информацией обо мне.
- [x] Список просмотренных фильмов/сериалов/аниме, прочитанных книг и пройденных игр.

Более подробный TODO [тут](./mySite.todo).

---

## 💻 Запуск проекта

В проекте используется [poetry](https://github.com/python-poetry/poetry) -
менеджер зависимостей. Для его установки на OSX / Linuxosx / linux /
bashonwindows используейте команду:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Для Windows:

```PowerShell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

Для успешной установки всех зависимостей и запуска виртуального окружения
необходимо запустить последовательно следующие команды в консоли:

```bash
git clone git@github.com:ALittleMoron/django-my-site.git
cd django-my-site
poetry install
poetry shell
```

Непосредственный запуск проекта:

```bash
cd путь-до-корневой-папки-репозитория/mySite

# замена настроек БД и ключа django под себя.

python3 manage.py collectstatic    # \
python3 manage.py makemigrations   #  Или все одной командой через &&
python3 manage.py migrate          # /

python3 manage.py runserver 8000   # либо полноценно через gunicorn, nginx и т.д.
```
