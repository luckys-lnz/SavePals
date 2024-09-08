#!/usr/bin/python3
"""Objects that handle all default RestFul API actions for transactionss"""
from models.payout import Payout
from models.contribution import Contribution
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request


@app_views.route('/transactions/contributions/<contribution_id>',
                 methods=['GET'], strict_slashes=False)
def get_contribution_details(contribution_id):
    """Retrieve contribution details based on the contribution_id"""
    contribution = storage.get(Contribution, contribution_id)
    return jsonify(contribution.to_dict())


@app_views.route('/transactions/payments/<payment_id>',
                 methods=['GET'], strict_slashes=False)
def get_payment_details(payment_id):
    """Retrieve payment details based on the payment_id"""
    payment = storage.get(Payout, payment_id)
    return jsonify(payment.to_dict())


@app_views.route(
    '/groups/<group_id>/rounds/<round_id>/users/<user_id>/contribution',
    methods=['POST'], strict_slashes=False)
def create_contribution(group_id, round_id, user_id):
    """
    Create a contribution to a specified group and round by a specific user
    based on user_id.
    """

    # Get the JSON data from the request
    data = request.get_json()

    # Validate the incoming data
    if not data:
        abort(400, description="No input data provided")
    if 'amount' not in data:
        abort(400, description="Contribution amount is required")

    amount = data['amount']

    try:
        # Create a new Contribution instance
        new_contribution = Contribution(
            user_id=user_id,
            group_id=group_id,
            round_id=round_id,
            amount=amount
        )

        # save the new contribution to the database
        new_contribution.save()

        # Return a success response
        return jsonify({
            "message": "Contribution created successfully",
            "contribution": {
                "user_id": user_id,
                "group_id": group_id,
                "round_id": round_id,
                "amount": amount
            }
        }), 201

    except Exception as e:
        # Handle any unexpected errors
        desc = f"An error occurred while creating the contribution: {str(e)}"
        abort(500, description=desc)


@app_views.route('/users/<user_id>/transactions', methods=['GET'],
                 strict_slashes=False)
def get_user_transactions(user_id):
    """Retrieve transactions based on the user_id"""
    contributions = storage.filter(Contribution, user_id=user_id)
    payments = storage.filter(Payout, user_id=user_id)

    # create the transactions
    transactions = {
        'contributions':
        [contribution.to_dict() for contribution in contributions],
        'payments': [payment.to_dict() for payment in payments]
    }

    return jsonify(transactions), 200


@app_views.route('/groups/<group_id>/transactions', methods=['GET'],
                 strict_slashes=False)
def get_group_transactions(group_id):
    """Retrieve transactions based on the group_id"""
    contributions = storage.filter(Contribution, group_id=group_id)
    payments = storage.filter(Payout, group_id=group_id)

    # create the transactions
    transactions = {
        'contributions':
        [contribution.to_dict() for contribution in contributions],
        'payments': [payment.to_dict() for payment in payments]
    }

    return jsonify(transactions), 200


@app_views.route('/rounds/<round_id>/transactions', methods=['GET'],
                 strict_slashes=False)
def get_round_transactions(round_id):
    """Retrieve transactions based on the round_id"""
    contributions = storage.filter(Contribution, round_id=round_id)
    payments = storage.filter(Payout, round_id=round_id)

    # create the transactions
    transactions = {
        'contributions':
        [contribution.to_dict() for contribution in contributions],
        'payments': [payment.to_dict() for payment in payments]
    }

    return jsonify(transactions), 200
