# Task Management API

This project is a Task Management API built with FastAPI. It provides endpoints to manage tasks and users, including creating, retrieving, updating, and deleting tasks and users. The API is designed to be fast, efficient, and easy to use, leveraging the power of FastAPI for asynchronous operations and automatic documentation generation.

## Features

- **Task Management**: Create, retrieve, update, and delete tasks.
- **User Management**: Create, retrieve, update, and delete users.
- **FastAPI**: Utilizes FastAPI for high performance and automatic interactive API documentation.

## Getting Started

### Prerequisites

- Python 3.7+
- pip (Python package installer)

### Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/your_username/task-management-api.git
   cd task-management-api
   
2. **Clone the repository**:
   ```sh
   pip install -r requirements.txt

### Running the Application

1. **Run the application**:
   ```sh
   fastapi dev main.py

3. **Access the API documentation**:
   Open your browser and navigate to http://127.0.0.1:8000/docs to view the interactive API documentation.

### Project Structure
```project/
│
├── main.py
├── models/
│   └── task.py
├── managers/
│   └── task_manager.py
├── routers/
│   └── task_router.py
├── utils/
│   └── utils.py
└── tasks/
    └── tasks.py
