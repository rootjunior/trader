### Get started
    $ bash env-prepare.sh
    $ docker network create bus
    $ docker compose build
    $ docker compose run -d postgresql
    $ docker compose run api alembic -c /code/api/db/migrations/alembic.ini upgrade head
    $ docker compose up

### Migrations

#### Generate new
    $ docker compose run api alembic -c /code/api/db/migrations/alembic.ini revision --autogenerate -m <migration name>
#### Upgrade tables
    $ docker compose run api alembic -c /code/api/db/migrations/alembic.ini upgrade head

### Code style

#### Clean code
    $ docker compose run api bash /code/scripts/clean.sh
#### Run lint
    $ docker compose run api bash /code/scripts/lint.sh