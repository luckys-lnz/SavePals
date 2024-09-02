#!/usr/bin/python3
"""
Object that displays the summary of the API.

actions for groups and rounds.
"""

from models.round import Round
from models.group import Group
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify


@app_views.route('/groups/<group_id>/summary', methods=['GET'],
                 strict_slashes=False)
def group_summary(group_id):
    """Retrieve the summary of the groups overall status."""
    group = storage.get(Group, group_id)
    if not group:
        abort(404)

    summary_data = {
        "group_name": group.name,
        "total_rounds": len(group.rounds),
        "total_amount_collected": sum(round_.amount for round_ in group.rounds),
        "next_collector": group.rounds[-1].collector if group.rounds else None
    }
    return jsonify(summary_data)


@app_views.route('/groups/<group_id>/rounds/<round_id>/summary',
                 methods=['GET'], strict_slashes=False)
def round_summary(group_id, round_id):
    """Retrieve the summary of the rounds overall status."""
    round_ = storage.get(Round, round_id)
    if not round_ or round_.group_id !=int(group_id):
        abort(404)

    summary_data = {
        "round_month": round_.month,
        "round_year": round_.year,
        "amount_collected": round_.amount,
        "collector": round_.collector,
        "contributions": [{"user.id": contribution.user.id, "amount":
                           contribution.amount} for contribution in
                          round_.contributions]
    }
    return jsonify(summary_data)


