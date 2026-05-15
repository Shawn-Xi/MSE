from datetime import datetime
from functools import wraps


def log_admin_activity(func):
    """
    A decorator that logs the execution of an admin function,
    including its name and the timestamp.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("--------------------------\n")
        print("--- Admin Activity Log  ---")
        print(f"Executing function: '{func.__name__}'")
        print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        result = func(*args, **kwargs)  # Call the original function

        print("Function execution finished.")
        print("--------------------------\n")
        return result
    return wrapper