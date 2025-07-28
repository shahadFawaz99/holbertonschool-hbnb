from flask_restx import Api
from flask import Blueprint

# Import all namespaces
from .users import api as user_ns
from .amenities import api as amenity_ns
from .places import api as place_ns
from .reviews import api as review_ns

# Create blueprint
api_v1_bp = Blueprint('api_v1', __name__, url_prefix='/api/v1')
api = Api(api_v1_bp, version='1.0', title='HBnB API',
          description='API for the HBnB application')

# Register namespaces
api.add_namespace(user_ns, path='/users')
api.add_namespace(amenity_ns, path='/amenities')
api.add_namespace(place_ns, path='/places')
api.add_namespace(review_ns, path='/reviews')

