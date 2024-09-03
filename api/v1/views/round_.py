#!/usr/bin/python3
"""Objects that handle all default RestFul API actions for Rounds."""
from models.payout import Payout
from models.contribution import Contribution
from models.group import Group
from models.round_ import Round
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request


@app_views.route('/groups/<group_id>/rounds', methods=['GET'],
                 strict_slashes=False)
def get_rounds(group_id):
    """Retrieve the list of all Rounds object in a group."""
    group = storage.get(Group, group_id)
    if not group:
        abort(404)

    list_rounds = [round_.to_dict() for round_ in group.rounds]
    return jsonify(list_rounds)


@app_views.route('/groups/<group_id>/rounds/<round_id>', methods=['GET'],
           strict_slashes=False)
def get_round(group_id, round_id):
    """Retrieve a specific round based on round_id and group_id."""
    group = storage.get(Group, group_id)
    if not group:
        abort(404)

    round_ = storage.get(Round, round_id)
    if not round_:
        abort(404)

    return jsonify(round_.to_dict())


@app_views.route('/groups/<group_id>/rounds', methods=['POST'],
                 strict_slashes=False)
def create_round(group_id):
    """Create a round in a specific group."""
    group = storage.get(Group, group_id)
    if not group:
        abort(404)

    data = request.get_json()
    if not data:
        abort(400, "Not a Json")

    required_fields = ['round_number', 'amount']
    for field in required_fields:
        if field not in data:
            abort(400, description=f"Missing {', '.join(required_fields)}")

    # ensure the round is linked to the correct group
    data['group_id'] = group_id
    instance = Round(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/groups/<group_id>/rounds/<round_id>', methods=['PUT'],
                 strict_slashes=False)
def update_round(group_id, round_id):
    """
    Updates a Round
    """
    group = storage.get(Group, group_id)
    if not group:
        abort(404)

    round_ = storage.get(Round, round_id)
    if not round_:
        abort(404)

    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")

    ignore = ['id', 'group_id', 'created_at', 'updated_at']
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
    group = storage.get(Group, group_id)
    if not group:
        abort(404)

    round_ = storage.get(Round, round_id)
    if not round_:
        abort(404)

    storage.delete(round_)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/rounds/<round_id>/payouts/<payout_id>',
                 methods=['POST'], strict_slashes=False)
def add_payout_to_round(round_id, payout_id):
    """Add a payout to round."""

    # Retrieve the payment
    payout = storage.get(Payout, payout_id)
    if not payout:
        abort(404, description="Payout not found")

    # Retrieve the round
    round_ = storage.get(Round, round_id)
    if not round_:
        abort(404, description="Round not found")

    # Add payout to the round
    if payout not in round_.payouts:
        round_.payouts.append(payout)
        storage.save()
        return make_response(jsonify(round_.to_dict()), 200)
    else:
        return make_response(
            jsonify({"message": "Payout already in round"}), 400)


@app_views.route('/rounds/<round_id>/payouts/<payout_id>/',
                 methods=['DELETE'], strict_slashes=False)
def remove_payout_from_round(round_id, payout_id):
    """Remove a payout from a round."""

    # Retrieve the payout
    payout = storage.get(Payout, payout_id)
    if not payout:
        abort(404, description="Payout not found")

    # Retrieve the round
    round_ = storage.get(User, user_id)
    if not round_:
        abort(404, description="Round not found")

    # Remove payout from the round
    if payout in round_.payouts:
        round_.payouts.remove(payout)
        storage.save()
        return make_response(jsonify(round_.to_dict()), 200)
    else:
        return make_response(
            jsonify({"message": "Payout not in round"}), 400)


@app_views.route('/rounds/<round_id>/contributions/<contribution_id>',
                 methods=['POST'], strict_slashes=False)
def add_contribution_to_round(user_id, contribution_id):
    """Add a contributions to rounds."""

    # Retrieve the contribution
    contribution = storage.get(Contribution, contribution_id)
    if not contribution:
        abort(404, description="Contribution not found")

    # Retrieve the round
    round_ = storage.get(Round, round_id)
    if not round_:
        abort(404, description="Round not found")

    # Add contribution to the round
    if contribution not in round_.contributions:
        round_.contributions.append(contribution)
        storage.save()
        return make_response(jsonify(round_.to_dict()), 200)
    else:
        return make_response(
            jsonify({"message": "Contribution already in round"}), 400)


@app_views.route('/rounds/<round_id>/contributions/<contribution_id>/',
                 methods=['DELETE'], strict_slashes=False)
def remove_contribution_from_round(round_id, contribution_id):
    """Remove a contribution from a round."""

    # Retrieve the contribution
    contribution = storage.get(Contribution, contribution_id)
    if not payout:
        abort(404, description="Contribution not found")

    # Retrieve the round
    round_ = storage.get(Round, round_id)
    if not round:
        abort(404, description="Round not found")

    # Remove contribution from round
    if contribution in round_.contributions:
        round_.contributions.remove(contribution)
        storage.save()
        return make_response(jsonify(round_.to_dict()), 200)
    else:
        return make_response(
            jsonify({"message": "Contribution not in round"}), 400)
