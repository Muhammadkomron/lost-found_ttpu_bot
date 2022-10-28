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

- If *pre commit* has not been installed please install by running following command:

```
pip install pre-commit
pre-commmit install
```

- Type the command below to deploy the project locally:

```
docker-compose -f local.yaml up -d
```

- You should be good to go now