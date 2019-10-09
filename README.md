# Quick API

Quick API is a RESTful API project for Backend Dev job application.

## Installation

Download [Python](https://www.python.org/downloads/) and use the Package Manager to install Django.

```bash
pip install djangorestframework
```

## Usage

Migrate database:

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

Start the project by running:

```bash
python manage.py runserver
```

Open the following URL in your favorite browser:

```bash
http://localhost:8000
```

Additionally, you can export clients list in CSV format at the following endpoint:

```bash
http://localhost:8000/export-clients
```

