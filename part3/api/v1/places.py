from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services import facade

api = Namespace('places', description='Place operations')

place_model = api.model('Place', {
    'title': fields.String(required=True),
    'description': fields.String,
    'price': fields.Float,
    'latitude': fields.Float,
    'longitude': fields.Float
})

@api.route('/')
class PlaceList(Resource):
    def get(self):
        # Public: return all places
        places = facade.place_repo.get_all()
        return [place.to_dict() for place in places], 200

    @jwt_required()
    @api.expect(place_model)
    def post(self):
        current_user = get_jwt_identity()
        data = api.payload
        place = facade.create_place(data, current_user['id'])
        return place.to_dict(), 201

@api.route('/<string:place_id>')
class PlaceResource(Resource):
    def get(self, place_id):
        place = facade.get_place(place_id)
        if not place:
            return {'error': 'Place not found'}, 404
        return place.to_dict(), 200

    @jwt_required()
    @api.expect(place_model)
    def put(self, place_id):
        current_user = get_jwt_identity()
        data = api.payload
        try:
            place = facade.update_place(place_id, data, current_user['id'])
            return place.to_dict(), 200
        except PermissionError:
            return {'error': 'Unauthorized action'}, 403
