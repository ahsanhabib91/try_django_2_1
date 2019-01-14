# try_django_2_1
`git clone https://github.com/ahsanhabib91/try_django_2_1.git`
* `cd try_django_2_1`
* `virtualenv -p python3 .`
* `source bin/activate` (if in a terminal)
* `pip install -r requirements.txt`
* `cd src`
## Postgresql setup
* `psql -U postgres`
* `CREATE DATABASE try_django_2_1;`

## After DB setup
* `python manage.py makemigrations`
* `python manage.py migrate`
* `python manage.py createsuperuser`(Optional)
* `python manage.py runserver`

### If want to export packagelist
* `Navigate to try_django_2_1`
* `pip freeze > requirements.txt`