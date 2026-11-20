# User Services API

A clean, modular, and layered RESTful API built with **FastAPI** for managing users.

---

## 🚀 Features

- **Layered Architecture**: Separation of concerns across API, Application (Service), Domain (Entity), and Infrastructure (Repository) layers.
- **RESTful API**: CRUD operations for users.
- **Automatic OpenAPI Documentation**: Swagger UI and ReDoc out of the box.

---

## 🛠️ Tech Stack

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **ASGI Server**: [Uvicorn](https://www.uvicorn.org/)
- **Validation**: [Pydantic](https://docs.pydantic.dev/)

---

## 📁 Project Structure

```text
├── src/
│   ├── api/            # API routes (Controllers)
│   ├── application/    # Business logic (Services)
│   ├── domain/         # Domain models (Entities)
│   └── infrastructure/ # Persistence layer (Repositories)
├── tests/              # Pytest suite
├── main.py             # Application entry point
├── pyproject.toml      # Project metadata + ruff config
└── requirements.txt    # Pinned dependencies
```

---

## ⚡ Getting Started

### 1. Prerequisites

- Python 3.13+

### 2. Installation

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/jwjooth/User-Services.git
cd User-Services
```

Create and activate a virtual environment:

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux / macOS
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Run the Application

Start the development server:

```bash
uvicorn src.main:app --reload
```

The API will be accessible at: `http://localhost:8000`

---

## 📖 API Documentation

Once the server is running, explore the interactive documentation:

- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🧪 Tests & Lint

```bash
pytest
ruff check .
ruff format --check .
```
