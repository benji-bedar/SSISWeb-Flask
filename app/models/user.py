from app import db  # Import the db object from your app
from werkzeug.security import check_password_hash, generate_password_hash
import mysql.connector

def get_user(username):
    try:
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()
        cursor.close()
        return user
    except mysql.connector.Error as err:
        print(f"Error in get_user: {err}")
        return None

def verify_user(username, password):
    user = get_user(username)
    if user and check_password_hash(user['password'], password):  # Check password hash
        return user
    return None

def add_user(username, hashed_password):
    try:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        existing_user = cursor.fetchone()

        if existing_user:  # Check if username already exists
            cursor.close()
            return False

        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
        db.commit()
        cursor.close()
        return True
    except mysql.connector.Error as err:
        print(f"Error in add_user: {err}")
        return False
