#!/usr/bin/python3
"""Objects that handle all default RestFul API actions for groups."""
from models.group import Group
from models.user import User
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request


@app_views.route('/groups/<group_id>', methods=['GET'], strict_slashes=False)
def get_group(group_id):
    """Retrieve a specific group based on group_id."""
    group = storage.get(Group, group_id)
    if not group:
        abort(404)
    return jsonify(group.to_dict())


@app_views.route('/groups/<group_id>/users',
                 methods=['GET'], strict_slashes=False)
def list_group_users(group_id):
    """Retrieve the list of all users in a group."""
    group = storage.get(Group, group_id)
    # Check if the group exists
    if not group:
        abort(404, description="Group not found")

    list_users = [user.to_dict() for user in group.users]
    return jsonify(list_users)


@app_views.route('/groups/<group_id>', methods=['PUT'], strict_slashes=False)
def update_group(group_id):
    """Update a group based on group_id."""
    group = storage.get(Group, group_id)
    if not group:
        abort(404, description="Group not found")

    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")

    ignore = ['id', 'created_at', 'updated_at', 'creator_id']
    for key, value in data.items():
        if key not in ignore:
            setattr(group, key, value)

    storage.save()

    return make_response(jsonify(group.to_dict()), 200)


@app_views.route('/groups/<group_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_group(group_id):
    """Delete a group based on group_id."""
    group = storage.get(Group, group_id)
    if not group:
        abort(404)

    storage.delete(group)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/groups', methods=['POST'], strict_slashes=False)
def create_group():
    """Create a new group."""
    data = request.get_json()

    required_keys = ['name', 'description', 'creator_id']
    missing_keys = [key for key in required_keys if key not in data]
    if missing_keys:
        abort(400, description=f"Missing {', '.join(missing_keys)}")

    # Validate creator_id exists in the database
    creator = storage.get(User, data['creator_id'])
    if not creator:
        abort(404, description="Creator not found")

    instance = Group(**data)

    # add creator as user in group automatically
    instance.users.append(creator)
    instance.save()

    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/groups/<group_id>/users/<user_id>',
                 methods=['POST'], strict_slashes=False)
def add_user_to_group(group_id, user_id):
    """Add a user to a group."""
    # Retrieve the group
    group = storage.get(Group, group_id)
    if not group:
        abort(404, description="Group not found")

    # Retrieve the user
    user = storage.get(User, user_id)
    if not user:
        abort(404, description="User not found")

    # Add user to the group
    if user not in group.users:
        group.users.append(user)
        storage.save()
        return make_response(jsonify(group.to_dict()), 200)
    else:
        return make_response(
            jsonify({"message": "User already in group"}), 400)


@app_views.route('/groups/<group_id>/users/<user_id>',
                 methods=['DELETE'], strict_slashes=False)
def remove_user_from_group(group_id, user_id):
    """Remove a user from a group."""
    # Retrieve the group
    group = storage.get(Group, group_id)
    if not group:
        abort(404, description="Group not found")

    # Retrieve the user
    user = storage.get(User, user_id)
    if not user:
        abort(404, description="User not found")

    # Remove user from the group
    if user in group.users:
        group.users.remove(user)
        storage.save()
        return make_response(jsonify(group.to_dict()), 200)
    else:
        return make_response(
            jsonify({"message": "User not in group"}), 400)
