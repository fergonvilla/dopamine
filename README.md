# Setting up the environment

- instal pip
- install virtualenv

- Clone the project:   `git clone git@github.com:fergonvilla/dopamine.git`

Install the dependencies.
Recommend [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/)
Create a virtualenv environment to isolate python dependencies:

`cd dopamine`
`virtualenv env`


Activate virtual environment:
`source env/bin/activate`

Install python dependencies:
`pip install mezzanine`

#TODO: put permissions to execute manage.py

Create a local database:
`python manage.py createdb`
#todo: Configure superuser email password ...

Start coding:

cd en el directorio (cd ~/Programming/dopamine/), activar el virtualenv (source env/bin/activate), arrancar el servidor (runserver)
`python manage.py runserver 8000`

Abrir el navegador en `http://localhost:8000'

Abri sublime y a picar codigo.

templates/base.html y templates/index.html

