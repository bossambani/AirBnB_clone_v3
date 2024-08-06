#!/usr/bin/python3
"""
view for City objects that handles all default RESTFul API actions
"""
from flask import jsonify, request, abort
from api.v1.views import app_views
from models import storage
from models.state import State
from models.city import City


@app_views.route("/states/<state_id>/cities", strict_slashes=False)
def get_all_cities(state_id):
    """Retrieves the list of all City objects of a State"""
    state = storage.get(State, state_id)
    if not state:
        return abort(404)
    cities = [city.to_dict() for city in state.cities]
    return jsonify(cities)


@app_views.route("/cities/<city_id>", strict_slashes=False)
def get_city(city_id):
    """Retrieves a City object"""
    city = storage.get(City, city_id)
    if city:
        return jsonify(city.to_dict())
    return abort(404)


@app_views.route("cities/<city_id>", methods=['DELETE'], strict_slashes=False)
def deletes_city(city_id):
    """Retrieves a city object"""
    city = storage.get(City, city_id)
    if city:
        storage.delete(city)
        storage.save()
        return jsonify({}), 200
    return abort(404)


@app_views.route("/states/<state_id>/cities",
                 methods=['POST'],
                 strict_slashes=False)
def create_city(state_id):
    """Creates a City"""
    if request.content_type != 'application/json':
        return abort(400, 'Not a JSON')
    state = storage.get(State, state_id)
    if not state:
        return abort(404)
    if not request.get_json():
        return abort(400, 'Not a JSON')
    data = request.get_json()
    if 'name' not in data:
        return abort(400, 'Missing name')
    data['state_id'] = state_id

    city = City(**data)
    city.save()
    return jsonify(city.to_dict()), 201


@app_views.route("/cities/<city_id>", methods=['PUT'], strict_slashes=False)
def update_city(city_id):
    """Updates a City"""
    if request.content_type != 'application/json':
        return abort(400, 'Not a JSON')
    city = storage.get(City, city_id)
    if city:
        if not request.get_json():
            return abort(400, 'Not a JSON')

        data = request.get_json()
        ignore_keys = ['id', 'state_id', 'created_at', 'updated_at']

        for key, value in data.items():
            if key not in ignore_keys:
                setattr(city, key, value)

        city.save()
        return jsonify(city.to_dict()), 200
    else:
        return abort(404)
