from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.models.user import add_user, verify_user
from werkzeug.security import generate_password_hash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, EqualTo

auth = Blueprint('auth', __name__)

# Define the login form using Flask-WTF
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

# Define the registration form using Flask-WTF
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=50)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[InputRequired(), EqualTo('password')])

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if 'user' in session:
        return redirect(url_for('student.index'))  # Redirect if already logged in

    form = LoginForm()  # Initialize the form
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        
        user = verify_user(username, password)
        if user:
            session.permanent = True
            session['user'] = username  # Store the username in the session
            flash('Logged in successfully!', 'success')
            return redirect(url_for('student.index'))  # Redirect to dashboard
        else:
            flash('Invalid username or password.', 'danger')

    return render_template('login.html', form=form)



@auth.route('/logout')
def logout():
    session.pop('user', None)
    session.permanent = False
    flash('You have been logged out.', 'info')  # Only flash the logout message
    return redirect(url_for('auth.login'))



# Registration route
@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()  # Initialize the registration form
    if form.validate_on_submit():  # This checks if the form is submitted and valid
        username = form.username.data
        password = form.password.data
        hashed_password = generate_password_hash(password)  # Hash the password
        
        # Add the new user to the database
        if add_user(username, hashed_password):
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('auth.login'))  # Redirect to login page
        else:
            flash('Username already taken. Please choose a different one.', 'danger')
    
    return render_template('register.html', form=form)
