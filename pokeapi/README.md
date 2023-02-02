
# Installation Instructions

For install this project, firs youn need to clone it. It doesn't matter if you download or clone it, feel free to do it! ;)

### Requirements
- Docker
- Docker Compose


1.  change directory to `pokeapi` folder and type the following command:
    `docker-compose up`

    > *Note:* if you have linux distributions you would be need to be a super user or using  `sudo` 

    ` sudo docker-compose up`

2. Open your browser and put the address `localhost:8000`


If you want to run it local you need to run the database container 
with the following command:

`sudo docker-compose up postgres`

Meanwhile you need to create a `virtualenv` and activate it.

   `python -m venv env`

   `source env/bin/activate`


Now you need to install the dependencies:

> Install Poetry:
  `pip install poetry`

> install dependencies
  `python -m poetry install --without test, prod`

Last but not least apply migrations and sync database

`python manage.py migrate`

`python manage.py sync`

And finally run the server

`python manage.py runserver_plus`
