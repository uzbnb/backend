# UzBnB Backend

This is a UzBnB Backend implementing a RESTful API using Django Rest Framework (DRF). It includes integration with DRF-YASG for automatic generation of OpenAPI documentation.

## Setup

### Installation

1. Clone this repository to your local machine.
2. Create a virtual environment using your preferred tool (e.g., virtualenv, pipenv).
3. Activate the virtual environment.
4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Environment Variables

Create a `.env` file in the project root directory based on the provided `env.example` file. Modify the values as necessary for your local setup.

```bash
# Example .env file
# Django settings
SECRET_KEY=your_secret_key_here
DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1

# JWT settings
ACCESS_TOKEN_LIFETIME_MINUTES=60
REFRESH_TOKEN_LIFETIME_DAYS=7
ROTATE_REFRESH_TOKENS=False
BLACKLIST_AFTER_ROTATION=False
UPDATE_LAST_LOGIN=True
SIGNING_KEY=complexkey
ALGORITHM=HS512

# Database settings
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=db
SQL_USER=postgres
SQL_PASSWORD=postgres
SQL_HOST=localhost
SQL_PORT=5432

# CORS settings
CORS_ALLOWED_ORIGINS=http://127.0.0.1:8000 http://127.0.0.1:3000
CORS_ALLOW_ALL_ORIGINS=True

# Static and Media files settings
STATIC_URL=/static/
MEDIA_URL=/media/

```

### Database Setup

Make migrations and migrate to set up the database schema.

```bash
python manage.py makemigrations
python manage.py migrate
```

### Run the Server

Start the development server:

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`.

### Accessing API Documentation

API documentation is automatically generated using DRF-YASG and is available at `/swagger/` when the server is running.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

