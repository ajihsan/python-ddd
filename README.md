# Python DDD - Library Service Example

Created by **Ihsan** (April 2025)

## Overview

This project implements a **Library Service API** using Python, FastAPI, and Domain-Driven Design (DDD) principles. It serves as a practical example and learning sandbox for applying modern Python best practices.

A key characteristic of this project is its **"Group by Domain" folder structure**. Instead of organizing code by technical layers (e.g., `models`, `controllers`, `repositories` at the top level), the code is structured around business domains or features (e.g., `book`, `loan`, `member`), keeping all related components (API, models, services, repositories) for a specific domain together.

The project also demonstrates:
* Using **Polars** for relevant data processing tasks.
* Focused **unit testing** (`pytest`) on domain models and services.
* Automated code quality checks via **pre-commit hooks**.
* **Continuous Integration (CI)** testing using GitHub Actions.

This repository is intended for learning and experimentation purposes.

## Key Concepts & Features Demonstrated

* **FastAPI Web API:** Building a robust and performant asynchronous API.
* **Domain-Driven Design (DDD):** Applying DDD principles to structure the application logic.
    * **"Group by Domain" Structure:** Organizing all code related to a specific business feature (e.g., `loan`) within a dedicated folder, including its API endpoints, domain models, business services, and repository logic.
    * **Domain Model:** Rich domain objects (Entities, Value Objects) defined within each domain's `model.py`.
    * **Domain Services:** Encapsulating business logic within each domain's service files (e.g., `borrowing_service.py`).
    * **Repositories:** Handling data persistence logic, defined within each domain's `repository.py`.
* **Polars Data Processing:** Potential use of Polars within domain services or specific modules for efficient data manipulation.
* **Unit Testing:** Focused unit tests using `pytest`, primarily targeting domain models and services (found within `library_service/tests/`).
* **Pre-commit Hooks:** Automated code formatting (`black`, `isort`) and linting (`flake8`) before each commit using `pre-commit`.
* **GitHub Actions CI:** Automated testing and quality checks triggered on push and pull requests via workflows defined in `.github/workflows/`.

## Technology Stack

* Python 3.11+
* FastAPI: Web framework.
* Uvicorn: ASGI server.
* Polars: DataFrames library.
* Pytest: Testing framework.
* **GitHub Actions:** CI/CD platform.
* Pre-commit: Git hooks management.
* Black, isort, flake8, mypy (optional): Code quality tools.
* Virtual Environment Management (e.g., `venv`)

## Project Structure

```
PYTHON_DDD/                     # Project Root
│
├── .github/
│   └── workflows/
│       └── ci.yaml                         # GitHub Actions CI workflow definition
│
├── library_service/                        # Main application package
│   │
│   ├── domains/                            # Root for all business domains
│   │   ├── __init__.py
│   │   ├── book/                           # 'book' domain feature
│   │   │   ├── __init__.py
│   │   │   ├── api.py                      # FastAPI endpoints for books
│   │   │   ├── model.py                    # Domain models for books
│   │   │   └── repository.py               # Data access logic for books
│   │   │
│   │   ├── loan/                           # 'loan' domain feature
│   │   │   ├── __init__.py
│   │   │   ├── api.py                      # FastAPI endpoints for loans
│   │   │   ├── borrowing_service.py        # Business logic service
│   │   │   ├── loan_reporting_service.py   # Analytic logic service
│   │   │   ├── model.py                    # Domain models for loans
│   │   │   └── repository.py               # Data access logic for loans
│   │   │
│   │   └── member/                         # 'member' domain feature
│   │       ├── __init__.py
│   │       ├── api.py                      # FastAPI endpoints for members
│   │       ├── model.py                    # Domain models for members
│   │       └── repository.py               # Data access logic for members
│   │
│   ├── database.py                         # Database configuration/session management
│   ├── main.py                             # FastAPI application entry point & setup
│   │
│   └── tests/                              # Unit tests
│       ├── book/
│       │   └── test_model.py               # Tests for book models
│       └── loan/
│           └── test_borrowing_service.py   # Tests for loan services
│
├── .env                      # Local environment variables
├── .gitignore
├── .pre-commit-config.yaml   # Configuration for pre-commit hooks
├── README.md                 # This file
└── requirements.txt          # Project dependencies
```

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    # Make sure you clone into a directory named PYTHON_DDD or navigate accordingly
    git clone <your-repository-url> PYTHON_DDD
    cd PYTHON_DDD
    ```

2.  **Create and activate a virtual environment:**
    * Using `venv`:
        ```bash
        python -m venv venv
        # On Windows:
        .\venv\Scripts\activate
        # On macOS/Linux:
        source venv/bin/activate
        ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables (if needed):**
    * Create a `.env` file in the root directory (copy from `.env.example` if provided).
    * Fill in any required configuration like database URLs, secrets, etc.

5.  **Install pre-commit hooks:**
    ```bash
    pre-commit install
    ```
    * Ensures code quality checks run automatically before each commit.*

## Running the Application

To run the FastAPI application locally:

```bash
# Make sure your virtual environment is activated
uvicorn library_service.main:app --reload
```

*(Assuming your FastAPI app instance in `library_service/main.py` is named `app`)*

The API will typically be available at `http://127.0.0.1:8000`.
Access the interactive API documentation (Swagger UI) at `http://127.0.0.1:8000/docs`.

## Running Tests

Execute the unit tests using `pytest` from the project root directory (`PYTHON_DDD/`):

```bash
# Make sure your virtual environment is activated
pytest
```

Pytest will automatically discover tests within the `library_service/tests/` directory.

## Pre-commit Hooks

This project uses `pre-commit` to enforce code style and quality before code is committed. The hooks configured in `.pre-commit-config.yaml` (like `black`, `isort`, `flake8`) run automatically on `git commit`.

If a hook modifies a file, the commit will be aborted. Simply `git add` the modified files and attempt the commit again.

Run hooks manually on all files:
```bash
pre-commit run --all-files
```

## Continuous Integration (CI)

This project uses **GitHub Actions** for Continuous Integration. The workflow is defined in `.github/workflows/ci.yaml`. It typically includes steps to:
* Set up Python environment.
* Install dependencies.
* Run linters (like `flake8`).
* Run unit tests (`pytest`).

This workflow is automatically triggered on events like `push` to the main branch or `pull_request` creation/updates, providing feedback on code quality and test results.

## Contributing

This is primarily a personal learning project, but contributions, suggestions, or issue reports are welcome! Please feel free to fork the repository, create issues, or submit pull requests.

## License

This project is licensed under the MIT License.
