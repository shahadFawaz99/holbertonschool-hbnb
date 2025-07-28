from app.models.review import Review
from app.persistence.sqlalchemy_repository import SQLAlchemyRepository

class ReviewRepository(SQLAlchemyRepository):
    def __init__(self):
        super().__init__(Review)

