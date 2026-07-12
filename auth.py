#this is space to write the authentication code for the github demo

def authenticate_user(username, password):
    # Placeholder for authentication logic
    if username == "admin" and password == "password":
        return True
    else:
        return False
    
def logout_user():
    # Placeholder for logout logic
    return True

def reset_password(username, new_password):
    # Placeholder for password reset logic
    if username == "admin":
        return True
    else:
        return False    
    

def change_password(username, old_password, new_password):
    # Placeholder for password change logic
    if username == "admin" and old_password == "password":
        return True
    else:
        return False

def get_user_details(username):
    # Placeholder for retrieving user details logic
    if username == "admin":
        return {"username": "admin", "email": "admin@example.com"}
    else:
        return None