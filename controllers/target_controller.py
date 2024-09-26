from flask import Blueprint, request, jsonify

from models import Target
from repositories.target_repository import (
    insert_target,
    find_target_by_id,
    find_all_targets,
    delete_target,
    update_target,
)
from returns.maybe import Nothing

from services.target_sevice import convert_target_to_json

target_bp = Blueprint('target', __name__)

@target_bp.route('/', methods=['GET'])
def get_all_targets():
    targets = find_all_targets()
    return jsonify([convert_target_to_json(target) for target in targets]), 200

@target_bp.route('/<int:target_id>', methods=['GET'])
def get_target(target_id):
    maybe_target = find_target_by_id(target_id)
    if maybe_target is Nothing:
        return jsonify({'error': f'No target with the ID - {target_id}'}), 404
    return jsonify(convert_target_to_json(maybe_target.unwrap())), 200

@target_bp.route('/', methods=['POST'])
def create_target():
    data = request.json
    target = Target(
        target_id=data['target_id'],
        city_id=data['city_id'],
        target_type_id=data['target_type_id'],
        target_industry_id=data['target_industry_id'],
        location_id=data['location_id'],
        priority=data['priority']
    )
    result = insert_target(target)
    if result.is_success:
        return jsonify(convert_target_to_json(result.unwrap())), 201
    return jsonify({'error': result.failure()}), 400

@target_bp.route('/<int:target_id>', methods=['DELETE'])
def remove_target(target_id):
    result = delete_target(target_id)
    if result.is_success:
        return jsonify({'message': 'Target deleted successfully.'}), 200
    return jsonify({'error': result.failure()}), 400

@target_bp.route('/<int:target_id>', methods=['PUT'])
def update_existing_target(target_id):
    data = request.json
    target = Target(
        target_id=data['target_id'],
        city_id=data['city_id'],
        target_type_id=data['target_type_id'],
        target_industry_id=data['target_industry_id'],
        location_id=data['location_id'],
        priority=data['priority']
    )
    result = update_target(target_id, target)
    if result.is_success:
        return jsonify(convert_target_to_json(result.unwrap())), 200
    return jsonify({'error': result.failure()}), 400
