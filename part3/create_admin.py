from app import create_app
from app.extensions import db
from app.models.user import User

app = create_app()
with app.app_context():
    user = User(
        email="admin@example.com",
        is_admin=True
    )
    user.hash_password("admin123")
    db.session.add(user)
    db.session.commit()
    print("✅ Admin user created: admin@example.com / admin123")

