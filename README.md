# 📁 Django My Site

## 📖 Кратко о проекте

По сути, сказать тут нечего. Просто личный сайт (без запуска на сервере) с возможностями микроблога. Планов серьезных на него нет.

---

## 🧾 TODO список (основные положения)

- [x] Инициировать проект (окружение, настройки, тестовый вывод домашней стр. и др.).
- [x] CRUD для микроблога. (Не совсем CRUD, потому как я убрал update с сайта, заменив его на change из админ-панели)
- [ ] Страница с информацией обо мне (в формате резюме).
- [ ] Список просмотренных фильмов/сериалов/аниме, прочитанных книг и пройденных игр.

Более подробный TODO [тут](./mySite.todo).

---

## 💻 Запуск проекта

В проекте используется [poetry](https://github.com/python-poetry/poetry) -
менеджер зависимостей. Для его установки на OSX / Linuxosx / linux /
bashonwindows используейте команду:

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -

```

Для Windows:

```PowerShell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py -UseBasicParsing).Content | python -

```

Для успешной установки всех зависимостей и запуска виртуального окружения
необходимо запустить последовательно следующие команды в консоли:

```bash
git clone git@github.com:ALittleMoron/django-my-site.git
cd django-my-site
poetry install
poetry shell
```
