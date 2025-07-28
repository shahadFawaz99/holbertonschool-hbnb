"""
Flask application extensions module.
Initializes external tools separately to prevent import loop issues.

Included tools:
    - SQLAlchemy: Object-relational mapping for database operations
    - JWT: Manages authentication tokens
    - Bcrypt: Secure password hashing utility
"""

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

# Instance SQLAlchemy partagée dans toute l'application
db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()
