#!/usr/bin/python3
from app import create_app, db
from app.models.user import User

app = create_app()

with app.app_context():
    db.create_all()  

    if not User.query.filter_by(email="admin@example.com").first():
        admin = User(email="admin@example.com", is_admin=True)
        admin.hash_password("admin123")
        db.session.add(admin)
        db.session.commit()
        print("✅ Admin created")
    else:
        print("ℹ️ Admin already exists")




