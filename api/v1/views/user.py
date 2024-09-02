#!/usr/bin/python3
"""Objects that handle all default RestFul API actions for users."""
from models.user import User
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """Retrieve a specific user based on user_id."""
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    return jsonify(user.to_dict())


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def list_users():
    """Retrieve the list of all user objects."""
    users = storage.all(User).values()
    list_users = [user.to_dict() for user in users]
    return jsonify(list_users)


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_user(user_id):
    """Update a user profile based on user_id."""
    user = storage.get(User, user_id)
    if not user:
        abort(404)

    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")

    ignore = ['id', 'created_at', 'updated_at', 'email']
    for key, value in data.items():
        if key not in ignore:
            setattr(user, key, value)

    storage.save()

    return make_response(jsonify(user.to_dict()), 200)


@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    """Delete a user based on user_id."""
    user = storage.get(User, user_id)
    if not user:
        abort(404)

    storage.delete(user)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    """Create a new user."""
    data = request.get_json()

    required_keys = ['email', 'password', 'first_name',
                     'last_name', 'user_name']
    missing_keys = [key for key in required_keys if key not in data]
    if missing_keys:
        abort(400, description=f"Missing {', '.join(missing_keys)}")

    instance = User(**data)
    instance.save()

    return make_response(jsonify(instance.to_dict()), 201)
