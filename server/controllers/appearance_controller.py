# server/controllers/appearance_controller.py

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from server.models.appearance import Appearance
from server.extentions import db

appearance_bp = Blueprint('appearance_bp', __name__)

@appearance_bp.route('', methods=['POST'])
@jwt_required()
def create_appearance():
    data = request.get_json()

    # Validate required fields
    if not all(k in data for k in ('rating', 'guest_id', 'episode_id')):
        return jsonify(error="Missing guest_id, episode_id, or rating"), 400

    # Validate rating value
    try:
        rating = int(data['rating'])
        if not (1 <= rating <= 5):
            return jsonify(error="Rating must be between 1 and 5"), 400
    except ValueError:
        return jsonify(error="Rating must be an integer"), 400

    # Create and save the appearance
    appearance = Appearance(
        rating=rating,
        guest_id=data['guest_id'],
        episode_id=data['episode_id']
    )

    db.session.add(appearance)
    db.session.commit()

    return jsonify(message="Appearance created successfully"), 201
