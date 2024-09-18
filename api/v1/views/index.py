#!/usr/bin/python3
"""
Defines an endpoint that gets the API status
"""
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'])
def get_status():
    """Check status of file"""
    return jsonify({"status": "OK"})
