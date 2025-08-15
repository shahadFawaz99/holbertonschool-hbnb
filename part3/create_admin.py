# create_admin.py
from app import create_app
from app.extensions import db
from app.models.user import User

app = create_app()
with app.app_context():
    email = "admin@example.com"
    password = "admin123"

    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        print(f"⚠️ User with email {email} already exists.")
    else:
        user = User(
            email=email,
            is_admin=True
        )
        user.hash_password(password)
        db.session.add(user)
        db.session.commit()
        print(f"✅ Admin user created: {email} / {password}")

