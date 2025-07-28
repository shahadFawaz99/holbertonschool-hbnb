from flask_cors import CORS
"""
REST API setup module.
Handles configuration and registration of various endpoints.

Endpoint structure:
    - users: User management features
    - amenities: Resource and facility handling
    - places: Location-related operations
    - reviews: Feedback and review system
    - auth: Authentication and access control
"""

from flask_restx import Api

# Import des namespaces
from app.api.v1.users import api as users_ns
from app.api.v1.amenities import api as amenities_ns
from app.api.v1.places import api as places_ns
from app.api.v1.reviews import api as reviews_ns
from app.api.v1.auth import api as auth_ns
from app.api.v1.admin import api as admin_ns
from app.api.v1.protected import api as protected_ns

# Définition de l'objet API global
api = Api(
    version="1.0",
    title="HBnB API",
    description="API REST pour la gestion de locations",
    doc="/api/v1/docs",
)

# Ajout des namespaces
api.add_namespace(users_ns, path="/api/v1/users")
api.add_namespace(places_ns, path="/api/v1/places")
api.add_namespace(reviews_ns, path="/api/v1/reviews")
api.add_namespace(amenities_ns, path="/api/v1/amenities")
api.add_namespace(auth_ns, path="/api/v1/auth")
api.add_namespace(admin_ns, path="/api/v1/admin")
api.add_namespace(protected_ns, path="/api/v1/protected")
