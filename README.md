# Запуск проекта 

## Создать в корне .env файл с содержимым:

``` bash
DB_HOST=localhost
DB_PORT=5433
DB_USER=postgres
DB_PASS=postgres
DB_NAME=db_name

DB_DRIVER=postgresql+asyncpg
```

## Docker

```
docker compose up
```

Билдится долго (5-10 мин), зато одной командой. 
Если на машине установлен ffmpeg имеет смысл закоментировать строки в docker-compose.yaml относящиеся к приложению (web)
и перейти к следующим шагам:


## Установка виртуального окружения:
```bash
python -m venv venv
```

## Запуск вертуального окружения:

### Unix
```bash
. venv/bin/activete
```

### Windows
```bash
venv/Scripts/activete
```

## Установка зависимостей:

```bash
pip install -r requirements.txt
```

## Запуск бд:

```bash
docker compose up
```

## Запуск приложения:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```


# ENDPOINTS:

```
GET /docs/ автодокументация для тестирования от fastAPI
POST /api/users/  {"name": "str" } создать юзера
POST /api/users/attaching_file  {"u_id": 1, u_token: UUID, "audio": b'' #файл } конвертация wav в mp3
```