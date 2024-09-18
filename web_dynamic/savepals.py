#!/usr/bin/python3
""" Starts a Flash Web Application """
from models import storage
from models.user import User
from flask import Flask, render_template
from flask_jwt_extended import jwt_required


app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.route('/signup', methods=['GET', 'POST'], strict_slashes=False)
def get_index():
    """Get the index (signup/login) page"""
    return render_template('login.html')


@app.route('/logout', methods=['GET'], strict_slashes=False )
def logout():
    """Get the index page"""
    return render_template('login.html')


@app.route('/dashboard')
@jwt_required()
def dashboard():
    # Replace 'dashboard.html' with the correct template for your dashboard
    return render_template('dashboard.html')


@app.route('/profile')
@jwt_required()
def profile():
    """Route to the user profile,and shows information of the user."""
    return render_template('profile.html')      


@app.route('/update_profile')
@jwt_required()
def update_profile():
    """Route to the user login, Allows user to login with new credentials."""
    return render_template('login.html')


@app.route('/goals')
@jwt_required()
def goals():
    """Route to the user profile,and shows information of the user."""
    return render_template('goals.html')


@app.route('/create_plan')
@jwt_required()
def create_plan():
    """Returns the create new plan page"""
    return render_template("new-plan.html")


@app.route('/friends')
@jwt_required()
def friends():
    """Route to the user profile,and shows information of the user."""
    return render_template('friends.html')


@app.route('/contribute')
@jwt_required()
def contribute():
    """Route to the user contribution,and shows information of the user."""
    return render_template('contribute.html')


@app.route('/round_')
@jwt_required()
def round_():
    """Route to the user rounds,  create group round"""
    return render_template('round_.html')


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000, debug=True)
