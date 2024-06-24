# shopMaster
A scalable and customizable online shopping solution built with Django rest framework

## Motivation
ShopMaster is a basic e-commerce backend project. 

### Virtual environment setup
#### Create virtual environment

```
python3 -m venv venv
```

#### Activate virtual environment

```
source venv/bin/activate
```

#### Environment variables setup

Create a .env file in the root directory and add the following variables in the .env.example file.
Note

The default database is sqlite3 on local environment. If you want to use postgresql(or any other), then make sure you set the environment variables in the .env for the database as shown in the .env.example file so that the DB_IS_AVAIL variable in config.settings.local is set to True.

#### Install dependencies

```
pip install requirements.txt
```

#### Run migrations

If you don't set the DB variables in the .env file, then the default database is sqlite3.
```
python manage.py migrate
```
#### Run local server

python manage.py runserver

#### Run tests

This covers linting with flake8, unit tests with pytest and coverage report.

After installing the dependencies. Run the following command in the terminal.

```
tox
```

#### Docker setup
Note

The default port for postgresql is 5432 but in the Docker setup, the port is 5435. So, make sure you change the port number in the .env file when using Docker.
Build image and run container

docker-compose up --build

#### List images

docker images

#### List containers

docker ps



