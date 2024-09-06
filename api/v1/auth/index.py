#!/usr/bin/python3
"""
Defines an endpoint that handles user authentication
"""
from flask import request, jsonify, abort
from flask_jwt_extended import JWTManager, create_access_token
from werkzeug.security import check_password_hash, generate_password_hash
from api.v1.auth import auth_bp


@auth_bp.route('/api/signup', methods=['POST'])
def signup():
    # retrieve user data
    data = request.get_json()

    # check if user exists
    if storage.filter_by(User, email=data['email']):
        abort(404, description='User already exists')

    required_keys = ['email', 'password', 'first_name', 'last_name']
    missing_keys = [key for key in required_keys if key not in data]
    if missing_keys:
        abort(400, description=f"Missing {', '.join(missing_keys)}")

    # create new user
    new_user = User(**data)
    new_user.save()

    return jsonify({'message': 'User created successfully'}), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = storage.filter_by(User, email=data['email'])
    pass = user.password

    if not user:
        return jsonify({'message': 'Invalid email'}), 401
    if password != pass:
        return jsonify({'message': 'Invalid password'}), 401

    # Create JWT token
    access_token = create_access_token(identity={'email': user.email})

    # Return the JWT token and user_id
    return jsonify({'token': access_token, 'user_id': user.id}), 200
