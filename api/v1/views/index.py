#!/usr/bin/python3
"""
create app_views
"""
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status')
def api_status():
    """
    Status function
    """
    response = {'status': 'ok'}
    return jsonify(response)
