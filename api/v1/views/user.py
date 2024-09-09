#!/usr/bin/python3
"""Objects that handle all default RestFul API actions for users."""
from models.user import User
from models.payout import Payout
from models.contribution import Contribution
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """Retrieve a specific user based on user_id."""
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    return jsonify(user.to_dict(depth=2))


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def list_users():
    """Retrieve the list of all user objects."""
    users = storage.all(User).values()
    list_users = [user.to_dict(depth=2) for user in users]
    return jsonify(list_users)


@app_views.route('/users/<user_id>/groups',
                 methods=['GET'], strict_slashes=False)
def list_user_groups(user_id):
    """Retrieve the list of all groups of a specified user"""
    user = storage.get(User, user_id)
    # Check if the user exists
    if not user:
        abort(404, description="User not found")

    list_groups = [group.to_dict(depth=2) for group in user.groups]
    return jsonify(list_groups)


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

    return make_response(jsonify(user.to_dict(depth=2)), 200)


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

    return make_response(jsonify(instance.to_dict(depth=2)), 201)


@app_views.route('/users/<user_id>/contributions/<contribution_id>',
                 methods=['POST'], strict_slashes=False)
def add_contribution_to_user(user_id, contribution_id):
    """Add a contributions to users."""

    # Retrieve the contribution
    contribution = storage.get(Contribution, contribution_id)
    if not contribution:
        abort(404, description="Contribution not found")

    # Retrieve the user
    user = storage.get(User, user_id)
    if not user:
        abort(404, description="User not found")

    # Add contribution to the user
    if contribution not in user.contributions:
        user.contributions.append(contribution)
        storage.save()
        return make_response(jsonify(user.to_dict(depth=2)), 200)
    else:
        return make_response(
            jsonify({"message": "Contribution already in user"}), 400)


@app_views.route('/users/<user_id>/contributions/<contribution_id>/',
                 methods=['DELETE'], strict_slashes=False)
def remove_contribution_from_user(user_id, contribution_id):
    """Remove a contribution from a user."""

    # Retrieve the contribution
    contribution = storage.get(Contribution, contribution_id)
    if not payout:
        abort(404, description="Contribution not found")

    # Retrieve the user
    user = storage.get(User, user_id)
    if not user:
        abort(404, description="User not found")

    # Remove contribution from the user
    if contribution in user.contributions:
        user.contributions.remove(contribution)
        storage.save()
        return make_response(jsonify(user.to_dict(depth=2)), 200)
    else:
        return make_response(
            jsonify({"message": "Contribution not in user"}), 400)


@app_views.route('/users/<user_id>/payouts/<payout_id>',
                 methods=['POST'], strict_slashes=False)
def add_payout_to_user(user_id, payout_id):
    """Add a payout to users."""

    # Retrieve the payment
    payout = storage.get(Payout, payout_id)
    if not payout:
        abort(404, description="Payout not found")

    # Retrieve the user
    user = storage.get(User, user_id)
    if not user:
        abort(404, description="User not found")

    # Add payout to the user
    if payout not in user.payouts:
        user.payouts.append(payout)
        storage.save()
        return make_response(jsonify(user.to_dict(depth=2)), 200)
    else:
        return make_response(
            jsonify({"message": "Payout already in user"}), 400)


@app_views.route('/users/<user_id>/payouts/<payout_id>/',
                 methods=['DELETE'], strict_slashes=False)
def remove_payout_from_user(user_id, payout_id):
    """Remove a payout from a user."""

    # Retrieve the payout
    payout = storage.get(Payout, payout_id)
    if not payout:
        abort(404, description="Payout not found")

    # Retrieve the user
    user = storage.get(User, user_id)
    if not user:
        abort(404, description="User not found")

    # Remove payout from the user
    if payout in user.payouts:
        user.payouts.remove(payout)
        storage.save()
        return make_response(jsonify(user.to_dict(depth=2)), 200)
    else:
        return make_response(
            jsonify({"message": "Payout not in user"}), 400)
