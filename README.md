# Chat App api

### Prerequisites

###### Requirements

Python 3.6.3


### Installing
Create virtual
- python3.6 -m venv virtual
Activate virtual
- source/bin/activate

#### Install all the requirements
- pip install -r requirements.txt

#### Databases
for postgresql users;
  * Go to settings;
    - Change user,password, name(database name) on the database settings.
for sqlite users;
  * Go to settings;
    - replace the database section with the following;
        - DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
      

### Make migrations
- python manage.py makemigrations
- python manage.py migrate

#### Run application
- python manage.py runserver
