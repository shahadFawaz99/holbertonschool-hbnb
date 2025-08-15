# create_admin.py
from app import create_app
from app.extensions import db
from app.models.user import User

app = create_app()

with app.app_context():
    existing_admin = User.query.filter_by(email="admin@example.com").first()
    if existing_admin:
        print("⚠️ Admin user already exists.")
    else:
        admin_user = User(
            email="admin@example.com",
            is_admin=True
        )
        admin_user.hash_password("admin123")  # كلمة المرور
        db.session.add(admin_user)
        db.session.commit()
        print("✅ Admin user created: admin@example.com / admin123")

