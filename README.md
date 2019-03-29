# Smart telegram bot

Умный телеграм-бот, способный вести более или менее адекватную беседу.

## Запуск

Для запуска необходимо в корень проекта добавить файл `config.ini` с соответствующими значениями параметров:

```ini
[telegram]
token = TOKEN
proxy_url = 

[dialog_flow]
token = TOKEN
lang = ru
session_id = SESSION_ID
```

## Flake8

```ini
[flake8]
max-line-length = 120
```