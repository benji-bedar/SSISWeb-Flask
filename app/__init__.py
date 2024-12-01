from flask import Flask, session, redirect, url_for, request
from flask_session import Session
from flask_wtf.csrf import CSRFProtect  # Import CSRF protection
import mysql.connector
from .config import DB_USER, DB_PASSWORD, DB_NAME, DB_HOST, SECRET_KEY, CLOUDINARY_CLOUD_NAME, CLOUDINARY_API_KEY, CLOUDINARY_API_SECRET
import cloudinary

# Database connection
db = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME,
    port=3306,
    unix_socket=None
)

# Cloudinary configuration
cloudinary.config(
    cloud_name=CLOUDINARY_CLOUD_NAME,
    api_key=CLOUDINARY_API_KEY,
    api_secret=CLOUDINARY_API_SECRET
)

# Flask app initialization
app = Flask(__name__, instance_relative_config=True)
app.config['SECRET_KEY'] = SECRET_KEY  # Ensure a secret key is set for session handling
app.config['SESSION_TYPE'] = 'filesystem'  # Use filesystem for session storage
app.config['SESSION_PERMANENT'] = False  # Sessions will not persist across restarts
app.config['SESSION_FILE_DIR'] = './flask_session'  # Directory to store session files

# Initialize Flask-Session for server-side session storage
Session(app)

# Initialize CSRF protection
csrf = CSRFProtect(app)  # Add CSRF protection initialization here

# Register blueprints
from .controller.students import student
app.register_blueprint(student)

from .controller.courses import course
app.register_blueprint(course)

from .controller.colleges import college
app.register_blueprint(college)

# Import and register the authentication blueprint
from .controller.auth import auth
app.register_blueprint(auth, url_prefix='/auth')

# Ensure user is logged in before accessing protected routes
@app.before_request
def ensure_logged_in():
    if 'user' not in session and request.endpoint not in ['auth.login', 'auth.register']:  # Skip login page and registration page
        return redirect(url_for('auth.login'))  # Redirect to login page

    session.permanent = False  # Ensure session is not permanent

# Clear session explicitly after each request
@app.after_request
def after_request(response):
    # Clear session data after request
    session.modified = True  # Mark session as modified
    return response

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
