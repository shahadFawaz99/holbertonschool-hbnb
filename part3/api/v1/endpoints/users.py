from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.user import User

users_bp = Blueprint('users', __name__, url_prefix='/api/v1/users')

@users_bp.route('/', methods=['POST'])
def register_user():
    data = request.get_json()
    required_fields = ['first_name', 'last_name', 'email', 'password']

    # Validate presence of required fields
    if not data or not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400

    # Check if email already exists
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'error': 'Email already registered'}), 409

    user = User(
        first_name=data['first_name'],
        last_name=data['last_name'],
        email=data['email']
    )
    user.hash_password(data['password'])

    db.session.add(user)
    db.session.commit()

    return jsonify({'id': user.id, 'message': 'User registered successfully'}), 201

@users_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify(user.to_dict())
