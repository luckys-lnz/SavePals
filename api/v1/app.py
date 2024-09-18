#!/usr/bin/python3
"""
Module defines a Flask application
"""
from flask_cors import CORS
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from api.v1.auth import auth_bp
import os
from flask_jwt_extended import JWTManager


app = Flask(__name__)
CORS(app)
app.config['JWT_SECRET_KEY'] = 'savepal_dean_lucky_ben'
jwt = JWTManager(app)


# register blueprints
app.register_blueprint(app_views)
app.register_blueprint(auth_bp)


@app.errorhandler(404)
def not_found_error(error):
    """ Handles error 404 """
    return jsonify({"error": "Not found"}), 404


@app.teardown_appcontext
def teardown(exception=None):
    """ Closes the storage """
    storage.close()


if __name__ == '__main__':
    host = os.getenv('SAVEPAL_API_HOST', '0.0.0.0')
    port = int(os.getenv('SAVEPAL_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True, debug=True)
