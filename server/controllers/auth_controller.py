# server/controllers/auth_controller.py

from flask import Blueprint, request, jsonify
from server.extentions import db
from server.models.user import User
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    # Ensure both username and password are provided
    if not data.get('username') or not data.get('password'):
        return jsonify(message="Username and password are required"), 400

    # Check if user already existsA
    if User.query.filter_by(username=data['username']).first():
        return jsonify(message="User already exists"), 409

    # Create new user
    user = User(username=data['username'])
    user.password_hash = data['password']  # This should trigger the password setter
    db.session.add(user)
    db.session.commit()

    return jsonify(message="User created successfully"), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    # Validate input
    if not data.get('username') or not data.get('password'):
        return jsonify(message="Username and password are required"), 400

    user = User.query.filter_by(username=data['username']).first()
    
    if user and user.authenticate(data['password']):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 200

    return jsonify(message="Invalid username or password"), 401
