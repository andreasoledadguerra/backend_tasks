# Backend Tasks

A Python backend project using SQLAlchemy ORM with PostgreSQL for database operations. This project demonstrates basic CRUD operations with a User model.

## Prerequisites

- Python 3.8 or higher
- PostgreSQL database (this project uses Supabase PostgreSQL)

## Installation

1. Clone the repository:
   ```bash
   git clone [text](https://github.com/andreasoledadguerra/backend_tasks.git)
   cd backend_tasks
   ```

2. Install the required dependencies:
   ```bash
   pip install python-dotenv==1.1.1 typing_extensions==4.15.0 SQLAlchemy psycopg2-binary
   ```

## Environment Setup

1. Create a `.env` file in the root directory of the project.

2. Add your PostgreSQL password to the `.env` file:
   ```
   POSTGRES_PASSWORD=your_postgresql_password_here
   ```

   Note: The database connection is configured to use Supabase PostgreSQL. Update the connection string in `db.py` and `main.py` if using a different PostgreSQL instance.

## Usage

1. Initialize the database and run the example:
   ```bash
   python main.py
   ```

   This will:
   - Create the database tables if they don't exist
   - Add a new user named "Andy"
   - Query and print all users in the database

## Database Schema

### User Model
- `id`: Integer, primary key, auto-increment
- `name`: String (50 characters max)

## License

This project is licensed under the terms specified in the [LICENSE](LICENSE) file.
