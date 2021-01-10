## Application Requirements
- Python 3.8
- Pipenv
- Redis ([Download](https://www.memurai.com/get-memurai) for Windows users)

## Setup Application
1. Clone this repository into a folder and `cd` into that folder
2. Run `pipenv sync` to install the project's dependencies into a new environment
3. Start a new Pipenv shell by running `pipenv shell`
4. Run `python manage.py makemigrations` and then `python manage.py migrate` to set up a local SQLite database for the application
5. Run `python manage.py runserver` to run the application development server and open it in your browser
