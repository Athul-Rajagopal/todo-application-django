# Django Todo Application

This is a simple Todo application built with Django, allowing users to add, edit, and delete tasks. Each task has a title, description, and status (pending or completed).

## Features
- User authentication (login and logout)
- Add new tasks
- Edit existing tasks
- Delete tasks after confirmation
- Display tasks in a tabular format

## Prerequisites

- Python 3.6 or higher
- pip (Python package installer)
- virtualenv (recommended)

## Setup and Installation

#### Step 1: Clone the repository

``` bash
git clone https://github.com/your-username/django-todo.git
cd django-todo
```
#### Step 2: Create and activate a virtual environment

``` bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment (Linux/macOS)
source venv/bin/activate

# Activate the virtual environment (Windows)
venv\Scripts\activate
```

#### Step 3: Install dependencies

``` bash
pip install -r requirements.txt
```

#### Step 4: Apply migrations

``` bash
python manage.py makemigrations
python manage.py migrate
```

#### Step 5: Create a superuser

``` bash
python manage.py createsuperuser
```
Follow the prompts to create an admin user.

#### Step 6: Run the development server

``` bash
python manage.py runserver
```

Open your web browser and go to http://127.0.0.1:8000/ to see the application in action.

## Usage

#### Adding a Task
1. Log in with your credentials.
2. Click on "Add Task".
3. Fill in the task details and click "Save".

#### Editing a Task
1. Click on the "Edit" button next to the task you want to edit.
2. Modify the task details and click "Save".

#### Deleting a Task
1. Click on the "Delete" button next to the task you want to delete.
