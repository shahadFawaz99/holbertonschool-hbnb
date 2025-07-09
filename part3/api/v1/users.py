from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services import facade

api = Namespace('users', description='User operations')

@api.route('/')
class UserCreate(Resource):
    @jwt_required()
    def post(self):
        current_user = get_jwt_identity()
        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403

        data = api.payload
        if facade.get_user_by_email(data.get('email')):
            return {'error': 'Email already registered'}, 400

        user = facade.create_user(data)
        return user.to_dict(), 201

@api.route('/<string:user_id>')
class UserUpdate(Resource):
    @jwt_required()
    def put(self, user_id):
        current_user = get_jwt_identity()
        is_admin = current_user.get('is_admin', False)

        if user_id != current_user['id'] and not is_admin:
            return {'error': 'Unauthorized action'}, 403

        data = api.payload
        if 'email' in data:
            existing = facade.get_user_by_email(data['email'])
            if existing and existing.id != user_id:
                return {'error': 'Email already in use'}, 400

        if not is_admin and ('email' in data or 'password' in data):
            return {'error': 'You cannot modify email or password'}, 400

        user = facade.update_user(user_id, data)
        return user.to_dict(), 200
