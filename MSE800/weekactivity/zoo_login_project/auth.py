from decorators import log_admin_activity

# Hardcoded admin credentials for demonstration
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "zoo_keeper_123"


@log_admin_activity
def admin_login(username, password):
    """
    Handles the admin login process by checking provided credentials.
    This function is decorated to log every login attempt.
    """
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        print("  -> Login successful!")
        return True
    else:
        print("  -> Login failed: Invalid username or password.")
        return False