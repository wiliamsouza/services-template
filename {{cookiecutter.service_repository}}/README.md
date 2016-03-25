#{{ cookiecutter.service_name }}

{{ cookiecutter.service_short_description }}

# Requirements

 * Python >= 3.5
 * PostgreSQL >= 9.3
 * memcached >= 1.4

# Installation

Install system requirements:

```
sudo apt-get install postgresql-client-9.3 postgresql-9.3 postgresql-server-dev-9.3 mencached libmemcached-dev
```

Create the user:

```bash
sudo -u postgres createuser --createdb {{ cookiecutter.service_slug }} -P
```

Create db:

```bash
sudo -u postgres createdb {{ cookiecutter.service_slug }} -O {{ cookiecutter.service_slug }}
```

Set superuser password for db:

```bash
sudo -u postgres createuser postgresadmin -P
```

Change "listen_addresses" to "localhost" to listen on all interfaces:

```
sudo vim /etc/postgresql/9.3/main/postgresql.conf
```

Create your local settings:

```
cp dot_env .env
```

> NOTES:
> Review the values and change if necessary.
> You can use [autoenv](https://github.com/kennethreitz/autoenv) to loads the
> environment variables settings automaticaly.

Create a virutalenv using Python 3.5:

Where the Python binary version 3.5 live?

```
which python3.5
/bin/python3.5
```

If you are lucky and have [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/) do:

```
mkservice --python=/bin/python3.5 {{ cookiecutter.service_slug }}
```

If you are using `mkservice` its time to clone the repo:

```
git clone {{ cookiecutter.git_clone_url }} .
```

> This create a virtualenv and activate it, as a plus every time you activate
> the environment using `workon {{ cookiecutter.service_slug }}` it will change to the service directory.
> there are others nice commands like `cdservice` and `cdvirtualenv`.

Install the service requirements:

```
pip install -r requirements/local.txt
```

Install git hooks:

```
pre-commit install
```

Database migrations
-------------------

All migrations SHOULD have a descritive description always use a command like:

```
python manage.py makemigrations --name <description> <app_label>
```

More info [hehe](https://docs.djangoservice.com/en/1.8/ref/django-admin/#django-admin-option---name).

Tests
-----

We use `pytest` with some nice plugins :)

Reuse DB is enabled default in `{{ cookiecutter.service_slug }}/pytest.ini` and has the same effect as running with:

```
py.test --reuse-db
```

> NOTE: If you want to **force** database creation use `--create-db`

for more info take look in [reuse database](http://pytest-django.readthedocs.org/en/latest/database.html?highlight=nomigration#reuse-db-reuse-the-testing-database-between-test-runs).


If time to run tests increase you can find out which tests are the slowest using:

```
$ py.test --durations=10
```

This will list the 10 slowest tests.

More info in [profiling test duration](http://pytest.org/latest/example/simple.html#profiling-test-duration)

Timeout is set to 3s in `pytest.ini` you can change it using:

```
py.test --timeout=10
```

Alternatively you can mark individual tests as having a timeout:

```
@pytest.mark.timeout(60)
def test_foo():
    pass
```

For more info take a look to [pytest-timeout plugin](https://pypi.python.org/pypi/pytest-timeout)
