# EduCore – Education Management Backend

EduCore is an education management backend built with Python and FastAPI. It provides REST APIs for teacher management, database operations, and JWT-based authentication.

The project follows a layered architecture to keep the code organized, maintainable, and easy to extend.

## 🚀 Features

- Teacher registration and management
- REST API development using FastAPI
- CRUD operations for teacher records
- PostgreSQL database integration
- SQLModel and SQLAlchemy for database operations
- Password hashing and verification
- JWT access token generation and verification
- Protected endpoints using FastAPI dependencies
- Request and response validation using Pydantic
- Interactive API documentation with Swagger UI

## 🛠️ Tech Stack

- **Language:** Python
- **Backend Framework:** FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLModel / SQLAlchemy
- **Validation:** Pydantic
- **Authentication:** JWT with PyJWT
- **Password Security:** Passlib / bcrypt
- **API Documentation:** Swagger UI
- **Version Control:** Git and GitHub

## 📁 Project Structure

```text
EduCore/
├── api/
│   └── teacher/
│       └── register.py
├── core/
│   ├── config.py
│   ├── security.py
│   └── dependencies.py
├── database/
│   └── database.py
├── model/
│   └── teacher.py
├── repositories/
│   └── teacher_repo.py
├── schemas/
│   └── teacher_schemas.py
├── service/
│   └── teacher_service.py
├── tests/
├── .env.example
├── .gitignore
├── main.py
└── README.md
```

## 🏗️ Architecture

EduCore follows a layered architecture:

```text
Client
  |
  v
FastAPI Router
  |
  v
Service Layer
  |
  v
Repository Layer
  |
  v
PostgreSQL Database
```

### Layer Responsibilities

- **API / Router:** Handles HTTP requests and responses.
- **Service:** Implements business logic and coordinates authentication.
- **Repository:** Handles database queries and CRUD operations.
- **Model:** Defines database table structures.
- **Schemas:** Validates incoming requests and outgoing responses.
- **Core:** Contains configuration, security utilities, and authentication dependencies.
- **Database:** Manages database connections and sessions.

## ⚙️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/nittasamith1/educore-fastapi-backend.git
cd educore-fastapi-backend
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

If a `requirements.txt` file exists:

```bash
python -m pip install -r requirements.txt
```

Otherwise, install the packages used by the project and save the verified dependencies to `requirements.txt`.

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql+psycopg://username:password@localhost:5432/educore
JWT_SECRET_KEY=replace_with_a_strong_random_secret
JWT_ALGORITHM=HS256
```

Replace the database credentials with your PostgreSQL configuration.

**Security:** Never commit `.env` or expose database passwords and JWT secrets.

### 5. Start the Application

Run from the project root:

```bash
python -m uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## 📚 API Documentation

FastAPI automatically generates interactive API documentation.

- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

Use Swagger UI to inspect endpoints and test requests.

## 🔐 Authentication Flow

EduCore uses JWT-based authentication.

1. A teacher registers with their details.
2. The password is hashed before being stored.
3. The teacher logs in with valid credentials.
4. The API verifies the password and generates a JWT access token.
5. The client sends the token in the Authorization header.
6. FastAPI extracts and verifies the token.
7. Protected endpoints return data for the authenticated teacher.

Example request header:

```http
Authorization: Bearer <your_access_token>
```

The token must be valid and unexpired to access protected endpoints.

## 🧪 Testing

Automated tests can be executed using pytest.

Install pytest if required:

```bash
python -m pip install pytest
```

Run tests:

```bash
python -m pytest
```

## 🔒 Security Practices

- Passwords should never be stored as plain text.
- JWT secrets must be kept in environment variables.
- Sensitive configuration files must not be committed to GitHub.
- Protected endpoints must validate JWT tokens.
- Passwords and password hashes must not be returned in API responses.
- Invalid or expired tokens should be rejected.

## 🛣️ Future Improvements

- Automated unit and integration tests
- Role-based access control
- Database migrations using Alembic
- Pagination, filtering, and searching
- Docker containerization
- CI/CD integration
- Production deployment
- Improved logging and error handling

## 🎯 Project Goal

The goal of EduCore is to develop practical skills in Python backend development, REST API design, database integration, authentication, and maintainable application architecture.

## 👨‍💻 Author

**Nitta Samith**

GitHub: https://github.com/nittasamith1

---

Built with Python and FastAPI.
