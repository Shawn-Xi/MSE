a decorator is a function which is used to add some extra logic to a function. Before and after.
Take function student_login as an example, it's assigned by "log_activity", and function/decorator is defined in file decorators.py.
So in the function body I can see some extra logic before the original fun is executed. print some logs.
Then the exactly function student_login is executed, it's passed to the decorator as an argument - fun.
after it's executed, more logs are printed.

---

## Student Login System (2023 Update)

This project includes a simple, command-line-based student login system with a password reset feature.

### Core Components

1.  **`login.py`**: The main entry point for the application. It provides a menu to log in or reset a password.
2.  **`user_database_setup.py`**: A utility script that creates and populates the database. It is called automatically when you run `login.py`.
3.  **`usersl.db`**: An SQLite database file that stores user information. It is created in the same directory as the scripts.

### How to Run the Project

To start the application, run the `login.py` file from your terminal:

```sh
python login.py
```

The script will automatically set up the database and present you with the main menu.

### Database: `usersl.db`

The `usersl.db` database contains a single table named `users`.

**`users` table schema:**

| Column       | Type    | Description                                          |
|--------------|---------|------------------------------------------------------|
| `id`         | INTEGER | The primary key for the user.                        |
| `email`      | TEXT    | The user's email address (must be unique).           |
| `password`   | TEXT    | The user's current password.                         |
| `reset_code` | TEXT    | A temporary 6-digit code for password resets.        |

By default, the following two users are created for testing:
- **Email:** `test@example.com`, **Password:** `password123`
- **Email:** `csu.wind@gmail.com`, **Password:** `123`

### Features

#### 1. User Login
- The system prompts for an email and password.
- It checks the credentials against the records in the `users` table.

#### 2. Forgot Password & Reset
This feature simulates a real-world password reset flow:
1.  **Request a Reset**: The user selects "Forgot Password" and enters their email.
2.  **Code Generation**: The system generates a random 6-digit code.
3.  **Email Simulation**: The code is **printed to the console** (simulating an email being sent). The code is also stored in the `reset_code` column for that user in the database.
4.  **Reset Password**: The user enters the code they received, along with a new password.
5.  **Validation**: The system checks if the code is correct. If it is, the password is updated in the database, and the `reset_code` is cleared.
