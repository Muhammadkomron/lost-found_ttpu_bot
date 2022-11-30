![Django project](https://github.com/Muhammadkomron/lost-found_ttpu_bot)

# Lost&Found TTPU Project

## Outline

- Prerequisites
- Setup
    - Development
    - Production
- Documentation

## Prerequisites

This project has the following prerequisites

- python 3.9.8
- docker 19.03.12
- docker-compose 1.25.0

## Setup

### Development

- Clone project:

```
git clone https://github.com/Muhammadkomron/lost-found_ttpu_bot
cd lost-found_ttpu_bot
```

- First create or login to https://ngrok.com and copy your token then paste it to *.envs/.local/.ngrok*

```
AUTH_TOKEN="paste your ngrok token here"
```

- Make sure you have created new test bot in Telegram and pasted into .envs/local/django:

```
TELEGRAM_BOT_TOKEN="paste your bot token here"
```

- Type the command below to run the project locally:

```
docker-compose -f local.yaml up -d
```

- After you started your local project open new terminal and create superuser to get access to admin panel:

```
docker-compose -f local.yaml run --rm django python manage.py createsuperuser
```

- Then you should import static written Telegram Bot buttons which located in *src/apps/bot/management/commands/bot_content_credentials.py* later you can edit in admin panel:

```
docker-compose -f local.yaml run --rm django python manage.py import_bot_credentials
```
- The last thing you should create is test telegram channel and get *id*
- You should be good to go now