from flask import Flask
import mysql.connector
from .config import DB_USER, DB_PASSWORD, DB_NAME, DB_HOST, SECRET_KEY, CLOUDINARY_CLOUD_NAME, CLOUDINARY_API_KEY, CLOUDINARY_API_SECRET
from flask_wtf.csrf import CSRFProtect
import cloudinary

db = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME,
    port=3306,
    unix_socket=None 
)


cloudinary.config( 
  cloud_name=CLOUDINARY_CLOUD_NAME, 
  api_key=CLOUDINARY_API_KEY,
  api_secret=CLOUDINARY_API_SECRET
)

app = Flask(__name__, instance_relative_config=True)
app.config['SECRET_KEY'] = SECRET_KEY
CSRFProtect(app)

from .controller.students import student
app.register_blueprint(student)

from .controller.courses import course
app.register_blueprint(course)

from .controller.colleges import college
app.register_blueprint(college)