#!/usr/bin/python3
"""
Defines an endpoint that handles user authentication
"""
from flask import request, jsonify, abort, make_response
from flask_jwt_extended import JWTManager, create_access_token, unset_jwt_cookies
from werkzeug.security import check_password_hash, generate_password_hash
from api.v1.auth import auth_bp
from models import storage
from models.user import User

@auth_bp.route('/signup', methods=['POST'], strict_slashes=False)
def signup():
    # retrieve user data
    data = request.get_json()

    # Check if required keys are in the data
    required_keys = ['email', 'password', 'first_name', 'last_name']
    missing_keys = [key for key in required_keys if key not in data]
    if missing_keys:
        abort(400, description=f"Missing {', '.join(missing_keys)}")

    # Check if the user already exists
    existing_user = storage.filter(User, email=data['email'])
    if existing_user:
        abort(409, description='User already exists')

    # Create new user with hashed password
    hashed_password = generate_password_hash(data['password'])
    new_user = User(email=data['email'], password=hashed_password, first_name=data['first_name'], last_name=data['last_name'], age=data['age'], phone=data['phone'])
    new_user.save()

    return jsonify({'message': 'User created successfully'}), 201

@auth_bp.route('/login', methods=['POST'], strict_slashes=False)
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # Retrieve the user from the database
    users = storage.filter(User, email=email)
    user = users[0]
    if not user:
        return jsonify({'message': 'invalid email'}), 401

    # Check if the provided password matches the stored hashed password
    if not check_password_hash(user.password, password):
        return jsonify({'message': 'Invalid password'}), 401

    # Create JWT token
    access_token = create_access_token(identity={'email': user.email})

    # Create a response and set the JWT token in a cookie
    response = make_response(jsonify({'message': 'Login successful', 'user_id': user.id}))
    response.set_cookie('jwt_token', access_token, httponly=True)

    return response


@auth_bp.route('/logout', methods=['POST'])
def logout():
    response = jsonify({'message': 'Logged out successfully'})
    unset_jwt_cookies(response)
    return response