"""
SQLAlchemy-based implementation of the Repository design pattern.
Handles data persistence through SQL database interactions.

Key capabilities:
    - Full support for Create, Read, Update, Delete (CRUD)
    - Robust transaction management
    - Performance-oriented query handling
"""

from app.extensions import db
from app.models import User, Place, Review, Amenity
from app.persistence.repository import Repository


class SQLAlchemyRepository(Repository):
    """Implémentation SQLAlchemy du pattern Repository.

    Cette classe encapsule toute la logique d'accès aux données
    via SQLAlchemy, permettant de changer facilement de base
    de données sans impacter le reste du code.

    Args:
        model: Classe du modèle SQLAlchemy à gérer
    """
    def __init__(self, model):
        self.model = model

    def add(self, obj):
        db.session.add(obj)
        db.session.commit()

    def get(self, obj_id):
        return self.model.query.get(obj_id)

    def get_all(self):
        return self.model.query.all()

    def update(self, obj_id, data):
        obj = self.get(obj_id)
        if obj:
            for key, value in data.items():
                setattr(obj, key, value)
            db.session.commit()

    def delete(self, obj_id):
        obj = self.get(obj_id)
        if obj:
            db.session.delete(obj)
            db.session.commit()

    def get_by_attribute(self, attr_name, attr_value):
        return self.model.query.filter(getattr(self.model, attr_name) == attr_value).first()
