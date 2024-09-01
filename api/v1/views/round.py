#!/usr/bin/python3
"""Objects that handle all default RestFul API actions for Rounds."""

from models.payout import Payout
from models.contribution import Contribution
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/groups/<group_id>/rounds', methods=['GET'],
                 strict_slashes=False)
def get_round(group_id):
    """Retrieve the list of all Rounds object in a group."""
    group = storage.get(Group, group_id)
    if not group:
        abort(404)

    list_rounds = [round_.to_dict() for round_ in group.rounds]
    return jsonify(list_rounds)


@app_views.route('/groups/<group_id>/rounds/<round_id>', methods=['GET'],
           strict_slashes=False)
def get_rounds(group_id, round_id):
    """Retrieve a specific round based on round_id and group_id."""
    round_ = storage.get(Round, round_id)
    if not round_ or round_.group_id != int(group_id):
        abort(404)

    return jsonify(round_.to_dict())


@app_views.route('/groups/<group_id>/rounds', methods=['POST'],
                 strict_slashes=False)
def post_round(group_id):
    """Create a round in a specific group."""
    group = storage.get(Group, group_id)
    if not group:
        abort(404)

    if not request.get_json():
        abort(400, "Not a Json file")
    if 'month' not in request.get_json() or 'year' not in request.get_json() or
    'amount' not in request.get_json():
        abort(400, "Missing required fields")

    data = request.get_json()
    # ensure the round is linked to the correct group
    data['group_id'] = group_id
    instance = Round(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/groups/<group_id>/rounds/<round_id>', methods=['PUT'],
                 strict_slashes=False)
def put_round(group_id, round_id):
    """
    Updates a Round
    """
    round_ = storage.get(Round, round_id)
    if not round_ or round_.group_id != int(group_id):
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'group_id', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(round_, key, value)
    storage.save()
    return make_response(jsonify(round_.to_dict()), 200)


@app_views.route('/groups/<group_id>/rounds/<round_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_round(group_id, round_id):
    """
    Deletes a round based on round_id and group_id
    """
    round_ = storage.get(Round, round_id)
    if not round_ or round_.group_id != int(group_id):
        abort(404)

    storage.delete(round_)
    storage.save()
    return make_response(jsonify({}), 200)
