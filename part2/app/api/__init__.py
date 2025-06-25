from flask_restx import Api
from flask import Blueprint

from app.api.v1.users import api as users_ns
from app.api.v1.places import api as places_ns
from app.api.v1.amenities import api as amenities_ns
from app.api.v1.reviews import api as reviews_ns

# Create a Blueprint for version 1 of the API
v1 = Blueprint('api_v1', __name__, url_prefix='/api/v1')
api = Api(v1, version='1.0', title='HBnB API', description='API for the HBnB Application')

# Register all namespaces
api.add_namespace(users_ns)
api.add_namespace(places_ns)
api.add_namespace(amenities_ns)
api.add_namespace(reviews_ns)

