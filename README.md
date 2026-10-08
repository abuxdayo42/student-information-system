# Student Information System

A beginner-friendly Python-based Student Information System built to practice clean project structure, object-oriented programming, file handling, JSON persistence, validation, error handling, logging, configuration management, automated testing, and Git/GitHub workflow.

## Features

* View student information
* Update student marks
* Update student semester
* Validate marks between 0 and 100
* Validate semester between 1 and 8
* Store student data in JSON
* Separate repository/data-access layer
* Service layer for application logic
* Object-oriented student model
* Error handling for invalid input and file problems
* Application logging
* Environment-based configuration using `.env`
* Automated tests using `pytest`
* Git version control
* GitHub repository integration

## Technologies Used

* Python
* JSON
* python-dotenv
* pytest
* Git
* GitHub

## Project Structure

```text
student-information-system/
│
├── .venv/
├── data/
│   └── student.json
│
├── logs/
│
├── src/
│   └── student_app/
│       ├── __init__.py
│       ├── config.py
│       ├── main.py
│       │
│       ├── models/
│       │   ├── __init__.py
│       │   └── student.py
│       │
│       ├── repositories/
│       │   ├── __init__.py
│       │   └── student_repository.py
│       │
│       ├── services/
│       │   ├── __init__.py
│       │   └── student_service.py
│       │
│       └── utils/
│           ├── __init__.py
│           ├── logger.py
│           └── validation.py
│
├── tests/
│   ├── __init__.py
│   ├── test_config.py
│   ├── test_repository.py
│   ├── test_student.py
│   └── test_validation.py
│
├── .env
├── .gitignore
├── README.md
└── requirements.txt
```

## Architecture

The project follows a simple layered structure:

### Model

The `Student` class represents the student and contains student-related data and operations.

### Repository

`StudentRepository` handles reading and writing student information to the JSON file.

### Service

`student_service.py` connects the application logic with the repository and model layers.

### Utilities

The `utils` package contains reusable functionality such as:

* Input validation
* Application logging

### Configuration

`config.py` loads application settings from environment variables using `python-dotenv`.

## Example Student Data

The application currently uses a JSON file to store student information.

```json
{
    "id": "2024001",
    "name": "Ali",
    "program": "BS Computer Science",
    "semester": 4,
    "marks": 85
}
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/abuxdayo42/student-information-system.git
```

### 2. Open the project directory

```bash
cd student-information-system
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

#### Windows PowerShell

```powershell
.venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project root.

Example:

```text
APP_NAME=Student Information System
DEBUG=True
MAX_STUDENTS=100
```

Additional environment variables can be added as required.

> Do not commit sensitive information such as API keys or passwords to GitHub.

## Running the Application

From the project root, run:

```powershell
python -m src.student_app.main
```

The application provides the following menu:

```text
1. View Student
2. Update Marks
3. Update Semester
4. Exit
```

## Running Tests

The project uses `pytest` for automated testing.

Run:

```powershell
pytest
```

The current test suite covers:

* Configuration
* Student model
* Repository operations
* Input validation

## Testing Result

The project currently contains **14 automated tests**, all of which pass successfully.

```text
14 passed
```

## Git Workflow

This project also demonstrates a basic Git workflow:

```bash
git add .
git commit -m "Commit message"
git push
```

The project uses the `main` branch and is connected to GitHub.

## Learning Goals

This project was developed as a practical learning project to understand how a Python application grows from a simple script into a structured application.

The project covers:

* Python fundamentals
* Functions and modules
* Object-oriented programming
* File handling
* JSON
* Exception handling
* Input validation
* Layered project architecture
* Repository pattern
* Logging
* Environment configuration
* Automated testing
* Virtual environments
* Dependency management
* Git
* GitHub

## Author

**Allah Bux Dayo**

GitHub: `abuxdayo42`

---

This project is intended for learning and demonstration purposes.
