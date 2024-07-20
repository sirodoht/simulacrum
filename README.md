# simulacrum

Policy Reaction Simulator

## Setup with Docker

1. Copy the docker compose override config:

```sh
cp docker-compose.override.example.yml docker-compose.override.yml
```

2. Add an OpenAI API Key in the `OPENAI_API_KEY` property of `docker-compose.override.yml`

3. Run:

```sh
docker compose up --build
```

4. Load or create some personas!

```sh
docker compose run web python manage.py loaddata personas
```

## Setup without Docker

1. Setup python environment:

```sh
python -m venv .venv
source .venv/bin/activate
```

2. Install requirements and migrate:

```sh
pip install -r requirements.txt
python manage.py migrate
```

3. Make a `.envrc` based on the example:

```sh
cp .envrc.example .envrc
```

4. Add an OpenAI API Key in the `OPENAI_API_KEY` property of `.envrc`

5. Load the `.envrc`:

```sh
source .envrc
```

6. Run development server:

```sh
python manage.py runserver
```

7. Load or create some personas!

```sh
python manage.py loaddata personas
```

## Load pre-defined test data

```sh
docker compose run web python manage.py loaddata test-data-file
# or
python manage.py loaddata test-data-file
```

This works for:

* `personas`: pre-defined personas, see `main/fixtures/personas.json`
* `users`: test admin user, see `main/fixtures/users.json`
