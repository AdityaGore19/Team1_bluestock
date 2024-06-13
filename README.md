# Bluestock Fintech


## Setting Up the Database

To connect your PostgreSQL database with the application, follow the steps outlined in this video tutorial:

[Watch this video to connect your PostgreSQL database with your app](https://youtu.be/HEV1PWycOuQ?si=b97ziWjRzq41RWrH)

1. Ensure you have PostgreSQL installed on your machine. You can download it from the [official PostgreSQL website](https://www.postgresql.org/download/).
2. Create a new database and a user with the appropriate permissions.
3. Update your Django project's `settings.py` file to include the PostgreSQL database configurations:
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'your_db_name',
            'USER': 'your_db_user',
            'PASSWORD': 'your_db_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```
4. Run the following commands to apply migrations and start the development server:
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    ```
5. API Endpoints

You can interact with the IPO data using the following API endpoints:

    List all IPO info: GET /ipo_info/
    Retrieve a specific IPO info: GET /ipo_info/<id>/
    Create a new IPO info: POST /ipo_info/
    Update an IPO info: PUT /ipo_info/<id>/
    Delete an IPO info: DELETE /ipo_info/<id>/
