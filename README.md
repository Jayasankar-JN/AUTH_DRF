# AUTH_DRF

A framework for launching  Django Rest Framework projects  Comes with a custom user model, login/logout/signup

## Features

- Custom user model
- Token-based auth
- Signup/login/logout

## Initial Setups
1.  Make sure Python 3.7x and Pipenv are already installed. 
2.  Clone the repo and configure the virtual environment:

```
$ pipenv install
$ pipenv shell
```
3.Set up the initial migration for our custom user models in users and build the database.

```
$ python manage.py makemigrations users
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```
## Endpoints

Login with your superuser account. Then navigate to all users. Logout. Sign up for a new account and repeat the login, users, logout flow.

- login - http://127.0.0.1:8000/api/rest-auth/login/
- all users - http://127.0.0.1:8000/api/users
- logout - http://127.0.0.1:8000/api/rest-auth/logout/
- signup - http://127.0.0.1:8000/api/rest-auth/registration/
