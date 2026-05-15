# Zoo Application Admin Login System

This project is a simple command-line login system for a Zoo Application's admin user. It demonstrates the use of Python functions, modules, and decorators.

---

## Project Structure

The project is organized into the following files:

```
zoo_login_project/
├── main.py
├── auth.py
├── decorators.py
└── README.md
```

- **`main.py`**: The main entry point of the application. It handles user input and displays the final login status.
- **`auth.py`**: Contains the core authentication logic. It defines the `admin_login` function which validates user credentials.
- **`decorators.py`**: Defines the `@log_admin_activity` decorator used in the project.

---

## Functionality

When you run `main.py`, the application will:
1. Prompt the user to enter a username and password.
2. Call the `admin_login` function to verify the credentials.
3. The login attempt (both success and failure) is automatically logged to the console by the decorator.
4. Display a final "Access Granted" or "Access Denied" message.

For this demo, the credentials are hardcoded in `auth.py`:
- **Username**: `admin`
- **Password**: `zoo_keeper_123`

---

## Decorator Implementation

The project uses a decorator named `@log_admin_activity` located in `decorators.py`.

This decorator is applied to the `admin_login` function in `auth.py`. Its purpose is to "wrap" the login function and add extra functionality without modifying the function's core code.

Specifically, every time `admin_login` is called, the `@log_admin_activity` decorator automatically:
1. Prints a log header.
2. Prints the name of the function being executed (`admin_login`).
3. Prints the current date and time.
4. Executes the original `admin_login` function.
5. Prints a log footer after the function completes.

This provides a clean and reusable way to log activity for any function, simply by adding `@log_admin_activity` above its definition.