
# Django Authentication App

This is a simple Django application for user authentication, including registration, login, logout, and protected views. 

## Features

- User Registration
- User Login
- User Logout
- Protected Pages (accessible only to logged-in users)

## Project Structure

- `auth_app/`
  - `migrations/`
  - `templates/auth_app/`
    - `base.html`
    - `index.html`
    - `login.html`
    - `register.html`
    - `protected.html`
  - `__init__.py`
  - `admin.py`
  - `apps.py`
  - `forms.py`
  - `models.py`
  - `tests.py`
  - `urls.py`
  - `views.py`
- `project_name/`
  - `__init__.py`
  - `settings.py`
  - `urls.py`
  - `wsgi.py`
- `manage.py`

## Setup Instructions

1. **Clone the repository**
    ```sh
    git clone https://github.com/Dimplektech/Authentication_App.git

    cd auth_project_folder
    ```

2. **Create and activate a virtual environment**
    ```sh
    python -m venv auth_venv
    source auth_venv/bin/activate  # On Windows use `auth_venv\Scripts\activate`
    ```

3. **Install dependencies**
    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations**
    ```sh
    python manage.py migrate
    ```

5. **Create a superuser**
    ```sh
    python manage.py createsuperuser
    ```

6. **Run the development server**
    ```sh
    python manage.py runserver
    ```

7. **Access the application**
    Open your browser and go to `http://127.0.0.1:8000/`.

## Main Components

### Views (auth_app/views.py)
- `index`: Renders the index page.
- `register`: Handles user registration using the built-in `User` model.
- `login_view`: Handles user login using the built-in `User` model.
- `logout_view`: Handles user logout.
- `protected_view`: Renders a protected page that requires authentication.

### Forms (auth_app/forms.py)
- `UserRegisterForm`: Extends `UserCreationForm` to include an email field. This form uses Django's built-in `User` model.

### Templates (auth_app/templates/auth_app/)
- `base.html`: Base template that other templates extend.
- `index.html`: Home page.
- `login.html`: Login page.
- `register.html`: Registration page.
- `protected.html`: Protected page.

### URLs (auth_app/urls.py)
- Defines URL patterns for the authentication views.

## Built-in User Model

This project uses Django's built-in `User` model for authentication. The `User` model is part of `django.contrib.auth` and provides a standard way to handle users, including fields for username, email, password, and more.

## Requirements

- Django
- Python 3.x

## Contact
- Dimpal Kaware (https://github.com/Dimplektech)
