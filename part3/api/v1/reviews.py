from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services import facade

api = Namespace('reviews', description='Review operations')

review_model = api.model('Review', {
    'place_id': fields.String(required=True),
    'text': fields.String(required=True)
})

@api.route('/')
class ReviewList(Resource):
    @jwt_required()
    @api.expect(review_model)
    def post(self):
        current_user = get_jwt_identity()
        data = api.payload
        try:
            review = facade.create_review(data, current_user['id'])
            return review.to_dict(), 201
        except ValueError as e:
            return {'error': str(e)}, 400

@api.route('/<string:review_id>')
class ReviewResource(Resource):
    @jwt_required()
    def put(self, review_id):
        current_user = get_jwt_identity()
        data = api.payload
        try:
            review = facade.update_review(review_id, data, current_user['id'])
            return review.to_dict(), 200
        except PermissionError:
            return {'error': 'Unauthorized action'}, 403

    @jwt_required()
    def delete(self, review_id):
        current_user = get_jwt_identity()
        try:
            facade.delete_review(review_id, current_user['id'])
            return {'message': 'Review deleted'}, 200
        except PermissionError:
            return {'error': 'Unauthorized action'}, 403
