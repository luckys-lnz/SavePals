#!/usr/bin/python3
""" Starts a Flash Web Application """
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.route('/signup', methods=['GET'], strict_slashes=False )
def get_index():
    """Get the index page"""
    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    # Replace 'dashboard.html' with the correct template for your dashboard
    return render_template('dashboard.html')


@app.route('/profile')
def profile():
    """Route to the user profile,and shows information of the user."""
    return render_template('profile.html')      


@app.route('/user/plans')
def goals():
    """Route to the user profile,and shows information of the user."""
    return render_template('profile.html')


@app.route('/create/plan')
def create_plan():
    """Returns the create new plan page"""
    return render_template("new-plan.html")


@app.route('/friends')
def friends():
    """Route to the user profile,and shows information of the user."""
    return render_template('friends.html')      
     

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000, debug=True)
