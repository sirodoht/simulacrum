# simulacrum

Policy Reaction Simulator

## Setup

```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Load pre-defined personas

```sh
python manage.py loaddata personas
```
