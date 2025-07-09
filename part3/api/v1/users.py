from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services import facade

api = Namespace('users', description='User operations')

user_update_model = api.model('UserUpdate', {
    'first_name': fields.String,
    'last_name': fields.String,
    # email and password excluded to prevent updates here
})

@api.route('/<string:user_id>')
class UserResource(Resource):
    @jwt_required()
    @api.expect(user_update_model)
    def put(self, user_id):
        current_user = get_jwt_identity()
        if user_id != current_user['id']:
            return {'error': 'Unauthorized action'}, 403
        data = api.payload
        if 'email' in data or 'password' in data:
            return {'error': 'You cannot modify email or password'}, 400
        try:
            user = facade.update_user(user_id, data)
            if not user:
                return {'error': 'User not found'}, 404
            return user.to_dict(), 200
        except ValueError as e:
            return {'error': str(e)}, 400
