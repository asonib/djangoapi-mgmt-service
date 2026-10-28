# Django Backend Service

Production-grade Django microservice built with clean separation of concerns, enterprise layered architecture (Controllers, Services, Models, Exceptions, Config), custom token-based filter middleware authentication, OpenAPI/Swagger/ReDoc documentation, and pagination.

## Python Version: `3.12.x`

***This project works with persistent SQLite/PostgreSQL and Custom Filter Authentication***

- Run database migrations before starting the server.
- Obtain an authorization token via `/api/auth/register/` or `/api/auth/login/`.
- Supply the token as an `Authorization` header (`Token <your-token>` or `Bearer <your-token>`) for all protected endpoints.

## Project Structure
- `app/config/`: Application constants, whitelists, and runtime configurations
- `app/controllers/`: API views and request dispatchers
- `app/services/`: Service interfaces and business logic implementations
- `app/models/`: Django ORM database persistence models
- `app/exceptions/`: Custom API exception classes and handlers
- `app/middlewares/`: Authentication filter layer executed before controllers
- `app/serializers/`: Data validation and serialization schemas

## Environment Variables
Create `.env` file in the project root if using environment-based database overrides or custom secrets:
```bash
SECRET_KEY=your-django-secret-key
DEBUG=True
ALLOWED_HOSTS=*
```

## Virtual Environment Setup
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

## Install Dependencies
```bash
pip install -r requirements.txt
```

### Apply Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Run Server (Development)
```bash
python manage.py runserver 8000
```

## API cURL Examples

***1. Register User***
```bash
curl --location 'http://localhost:8000/api/auth/register/' \
--header 'Content-Type: application/json' \
--data '{
    "username": "testuser",
    "password": "Password123!",
    "email": "testuser@example.com"
}'
```

***2. Login***
```bash
curl --location 'http://localhost:8000/api/auth/login/' \
--header 'Content-Type: application/json' \
--data '{
    "username": "testuser",
    "password": "Password123!"
}'
```

***3. Upload Document (Multipart File Form-Data)***
```bash
curl --location 'http://localhost:8000/api/documents/' \
--header 'Authorization: Token <YOUR_AUTH_TOKEN>' \
--form 'title="Quarterly Report"' \
--form 'file=@"/path/to/document.pdf"'
```

***4. Upload Document (JSON Payload)***
```bash
curl --location 'http://localhost:8000/api/documents/' \
--header 'Authorization: Token <YOUR_AUTH_TOKEN>' \
--header 'Content-Type: application/json' \
--data '{
    "title": "System Architecture Notes",
    "content": "Detailed overview of the microservice architecture."
}'
```

***5. List Documents (Paginated)***
```bash
curl --location 'http://localhost:8000/api/documents/?page=1&page_size=10' \
--header 'Authorization: Token <YOUR_AUTH_TOKEN>'
```

***6. Retrieve Single Document***
```bash
curl --location 'http://localhost:8000/api/documents/1/' \
--header 'Authorization: Token <YOUR_AUTH_TOKEN>'
```

***7. Delete Document***
```bash
curl --location --request DELETE 'http://localhost:8000/api/documents/1/' \
--header 'Authorization: Token <YOUR_AUTH_TOKEN>'
```

***8. Run a Query***
```bash
curl --location 'http://localhost:8000/api/query/' \
--header 'Authorization: Token <YOUR_AUTH_TOKEN>' \
--header 'Content-Type: application/json' \
--data '{
    "query_text": "Summarize the latest document metrics."
}'
```

***9. List Query History (Paginated)***
```bash
curl --location 'http://localhost:8000/api/queries/?page=1&page_size=10' \
--header 'Authorization: Token <YOUR_AUTH_TOKEN>'
```

## Swagger & ReDoc Documentation

- **Swagger UI**: http://localhost:8000/api/docs/
- **ReDoc**: http://localhost:8000/api/redoc/
- **OpenAPI Schema**: http://localhost:8000/api/schema/
