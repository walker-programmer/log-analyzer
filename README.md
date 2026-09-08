# Log Analyzer

Небольшой CLI-инструмент для анализа access-логов веб-сервера в формате Apache/Nginx.

Проект демонстрирует базовые практики разработки на Python: структуру пакета, парсинг данных, агрегацию статистики, автоматические тесты, проверку качества кода и контейнеризацию с Docker.

## Возможности

* разбор строк access-лога;
* подсчёт общего количества запросов;
* группировка запросов по HTTP-методам;
* группировка по HTTP-кодам ответа;
* подсчёт запросов по URL;
* подсчёт запросов по IP-адресам;
* подсчёт общего объёма переданных данных;
* пропуск некорректных строк с предупреждением;
* запуск приложения в Docker-контейнере.

## Требования

* Python 3.12+
* Docker — для запуска в контейнере

## Структура проекта

```text
log-analyzer/
├── src/
│   └── log_analyzer/
│       ├── __init__.py
│       ├── __main__.py
│       ├── analyzer.py
│       ├── models.py
│       └── parser.py
├── tests/
│   ├── test_analyzer.py
│   ├── test_main.py
│   └── test_parser.py
├── .dockerignore
├── .gitignore
├── Dockerfile
├── pyproject.toml
└── README.md
```

## Установка

Клонировать репозиторий:

```bash
git clone git@github.com:walker-programmer/log-analyzer.git
cd log-analyzer
```

Создать виртуальное окружение:

```bash
python -m venv .venv
source .venv/bin/activate
```

Установить проект вместе с зависимостями для разработки:

```bash
pip install -e ".[dev]"
```

## Использование

Запустить анализатор с файлом лога:

```bash
python -m log_analyzer example.log
```

Пример результата:

```text
Log Analysis Report
-------------------
Total requests: 4
Total response size: 3576 bytes

Methods:
  GET: 3
  POST: 1

Status codes:
  200: 2
  302: 1
  404: 1

URLs:
  /index.html: 1
  /about.html: 1
  /login: 1
  /missing.html: 1

IPs:
  192.168.1.10: 2
  192.168.1.11: 2
```

## Docker

Собрать Docker-образ:

```bash
docker build -t log-analyzer .
```

Запустить анализатор с локальным файлом лога:

```bash
docker run --rm \
  -v "$(pwd)/example.log:/data/example.log:ro" \
  log-analyzer /data/example.log
```

Файл лога передаётся в контейнер только для чтения и не включается в Docker-образ.

## Тестирование

Запустить тесты:

```bash
pytest
```

Проверить код с помощью Ruff:

```bash
ruff check .
```

Проверить форматирование:

```bash
ruff format --check .
```

## Технологии

* Python
* pytest
* Ruff
* Git / GitHub
* Docker
* Linux / WSL2
* setuptools
