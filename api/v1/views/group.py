#!/usr/bin/python3
"""Objects that handle all default RestFul API actions for users."""
from models.group import Group
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/users/<user_id>/groups', methods=['GET'], strict_slashes=False)
def get_user_groups(user_id):
    """Retrieve the groups of a specific user based on user_id."""
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    groups = [group.to_dict() for group in user.groups]
    return jsonify(groups)


@app_views.route('/groups/<group_id>', methods=['GET'], strict_slashes=False)
def get_group(group_id):
    """Retrieve a group based on the group_id"""
    group = storage.get(Group, group_id)
    return jsonify(group.to_dict())


@app_views.route('/groups/<group_id>', methods=['PUT'], strict_slashes=False)
def update_group(group_id):
    """Update a group details based on group_id."""
    group = storage.get(Group, group_id)
    if not group:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(group, key, value)
    storage.save()
    return make_response(jsonify(group.to_dict()), 200)


@app_views.route('/groups/<group_id>', methods=['DELETE'], strict_slashes=False)
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
    """Create a new group"""
    data = request.get_json()

    if not data:
        abort(400, description="Not a JSON")
    if 'name' not in data:
        abort(400, description="Missing name")
    if 'description' not in data:
        abort(400, description="Missing description")
    if 'creator_id' not in data:
        abort(400, description="Missing creator id")

    instance = Group(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)

@app_views.route('/groups/<group_id>/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user_from_group(group_id, user_id):
    """Delete a user from a group based on group_id and user_id."""
    group = storage.get(Group, group_id)
    if not group:
        abort(404, description="Group not found")

    user = storage.get(User, user_id)
    if not user:
        abort(404, description="User not found")

    if user not in group.users:
        abort(404, description="User not in this group")

    # Remove the user from the group's users relationship
    group.users.remove(user)
    
    # Save the changes to the database
    storage.save()

    return make_response(jsonify({}), 200)

@app_views.route('/groups/<group_id>/users/<user_id>', methods=['POST'], strict_slashes=False)
def add_user_to_group(group_id, user_id):
    """Add a user to a group based on group_id."""
    group = storage.get(Group, group_id)
    if not group:
        abort(404, description="Group not found")
    
    user = storage.get(User, user_id)
    if not user:
        abort(404, description="User not found")

    if user in group.users:
        abort(400, description="User already in this group")

    # Add the user to the group's users relationship
    group.users.append(user)
    
    # Save the changes to the database
    storage.save()

    return make_response(jsonify(group.to_dict()), 201)
