from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services import facade

api = Namespace('amenities', description='Amenity operations')

@api.route('/')
class AmenityCreate(Resource):
    @jwt_required()
    def post(self):
        current_user = get_jwt_identity()
        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403
        amenity = facade.create_amenity(api.payload)
        return amenity.to_dict(), 201

@api.route('/<string:amenity_id>')
class AmenityUpdate(Resource):
    @jwt_required()
    def put(self, amenity_id):
        current_user = get_jwt_identity()
        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403
        amenity = facade.update_amenity(amenity_id, api.payload)
        return amenity.to_dict(), 200
