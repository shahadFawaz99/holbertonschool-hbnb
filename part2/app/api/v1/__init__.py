from flask import Blueprint
from flask_restx import Api
from api.v1.places import api as places_ns

# Create a Flask Blueprint for versioned API routing
api_bp = Blueprint('api', __name__, url_prefix='/api/v1')

# Create the API object
api = Api(
    api_bp,
    version='1.0',
    title='HBnB API',
    description='API documentation for the HBnB application (Task 4 - Place endpoints)',
)

# Register the namespace for places
api.add_namespace(places_ns, path='/places')

