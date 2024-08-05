#!/usr/bin/python3
"""
Create Flask app and register the blueprint app_views to flask instance
"""
from flask import Flask, jsonify
from os import getenv
from models import storage
from api.v1.views import app_views

app = Flask(__name__)

# Register the blueprint
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Method to handle app context teardown"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """404 status code response"""
    response = {
            "error": "Not found"
            }
    return jsonify(response), 404


if __name__ == '__main__':
    HOST = getenv('HBNB_API_HOST', '0.0.0.0')
    PORT = int(getenv('HBNB_API_PORT', 5000))
    app.run(host=HOST, port=PORT, threaded=True)
