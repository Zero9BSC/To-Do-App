# 📝 To-Do App - Task Manager API

A simple RESTful API built with **Python (Flask)**, **MySQL**, and **Docker**, allowing users to manage tasks with JWT authentication.

## 🔧 Technologies
- Python 3.11
- Flask
- MySQL 8
- Docker + Docker Compose

## 🚀 How to Run the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/Zero9BSC/To-Do-App.git
   cd to-do-app
   ```

2. Make sure Docker Desktop is installed and running.

3. Start the containers:
   ```bash
   docker compose up --build
   ```

4. The MySQL container will automatically initialize the `task_db` database and `tasks` table using the `init.sql` script.

> The backend will be available at [http://localhost:5000](http://localhost:5000)

## 🧪 API Endpoints

### Authentication
- `POST /register` – Register a new user (in-memory).
- `POST /login` – Login and obtain JWT.

### Tasks (JWT required)
- `GET /tasks` – List all tasks.
- `POST /tasks` – Create a new task.

## 🔐 Authentication
All `/tasks` endpoints require a JWT token. Get it via the login endpoint and include it in the `Authorization` header:

```
Authorization: Bearer <your-token>
```

## 🗃️ Database Initialization

The `init.sql` file initializes the MySQL database and table:

```sql
CREATE DATABASE IF NOT EXISTS task_db;

USE task_db;

CREATE TABLE IF NOT EXISTS tasks (
  id INT AUTO_INCREMENT PRIMARY KEY,
  description VARCHAR(255)
);
```

This file is automatically executed by the MySQL container during the first run.

## 📄 License

MIT