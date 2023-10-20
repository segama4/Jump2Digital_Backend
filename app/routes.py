from flask import Blueprint, request, jsonify
from .skins_controller import get_available_skins, buy_skin, get_my_skins, change_skin_color, delete_skin, get_skin

skins_bp = Blueprint('skins', __name__)


@skins_bp.route('/skins/available', methods=['GET'])
def available_skins():
    return jsonify(get_available_skins())


@skins_bp.route('/skins/buy', methods=['POST'])
def buy():
    data = request.get_json()
    return jsonify(buy_skin(data))


@skins_bp.route('/skins/myskins', methods=['GET'])
def my_skins():
    return jsonify(get_my_skins())


@skins_bp.route('/skins/color', methods=['PUT'])
def change_color():
    data = request.get_json()
    return jsonify(change_skin_color(data))


@skins_bp.route('/skins/delete/<string:id>', methods=['DELETE'])
def delete(id):
    return jsonify(delete_skin(id))


@skins_bp.route('/skins/getskin/<string:id>', methods=['GET'])
def get(id):
    return jsonify(get_skin(id))
