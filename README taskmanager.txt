# Django Task Manager API

This project is a Task Manager API built using Django. It provides endpoints for creating, retrieving, updating, and deleting tasks. The API also includes features like recurring tasks and reminder notifications.

## Features
- Create, retrieve, update, and delete tasks.
- Recurring tasks (daily, weekly, monthly).
- Reminder notifications for tasks due soon.
- Predict due dates for tasks (future implementation).

## Tech Stack
- **Language**: Python
- **Framework**: Django
- **Database**: SQLite (default), configurable to other databases like PostgreSQL or MySQL
- **Task Queue**: Redis (for background tasks)
- **Environment Management**: Virtualenv

## Requirements
- Python 3.x
- Django 3.x
- Redis (for task queue)
- Virtualenv

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/task-manager-api.git
   cd task-manager-api
