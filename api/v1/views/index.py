#!/usr/bin/python3
"""
create app_views
"""
from flask import jsonify
from api.v1.views import app_views
from models import storage
import json


@app_views.route('/status')
def api_status():
    """
    Status function
    """
    response = {'status': 'ok'}
    return jsonify(response)


@app_views.route('/stats')
def get_status():
    """
    Retrieves the number of each objects by type
    """
    stats = {
            "amenities": storage.count('Amenity'),
            "cities": storage.count('City'),
            "places": storage.count('Place'),
            "reviews": storage.count('Review'),
            "states": storage.count('State'),
            "users": storage.count('User'),
    }
    response = json.dumps(stats, indent=4)
    return response
