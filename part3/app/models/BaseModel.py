#!/usr/bin/python3

import uuid
from datetime import datetime
from app.extensions import db

class BaseModel(db.Model):
    """Base class for all models."""
    __abstract__ = True

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def save(self):
        """Save the instance to the database."""
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        """Update instance attributes from a dictionary."""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()
