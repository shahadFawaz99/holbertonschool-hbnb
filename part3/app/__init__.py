from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
import os

from app.extensions import db, bcrypt, jwt
from config import DevelopmentConfig  # تأكد من وجود الملف config.py

def create_app(config_class=DevelopmentConfig):
    """Factory function to create the Flask application"""
    app = Flask(__name__)

    # Load the configuration class
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # Swagger UI configuration
    SWAGGER_URL = '/api/v1'
    API_URL = '/static/swagger.json'

    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "HBNB API"
        }
    )

    # Register Swagger blueprint
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    # Ensure the static folder exists
    if not os.path.exists(os.path.join(app.root_path, 'static')):
        os.makedirs(os.path.join(app.root_path, 'static'))

    # Register the API
    from app.api.v1 import api as api_v1
    api_v1.init_app(app)

    return app
