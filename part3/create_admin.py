#!/usr/bin/python3

from app import create_app, db
from app.models.user import User

app = create_app()

with app.app_context():
    # إنشاء جميع الجداول إذا لم تكن موجودة
    db.create_all()

    # تحقق إذا كان admin موجود
    existing_admin = User.query.filter_by(email="admin@example.com").first()
    if not existing_admin:
        admin = User(
            email="admin@example.com",
            is_admin=True
        )
        admin.hash_password("admin123")  # ضع كلمة المرور
        db.session.add(admin)
        db.session.commit()
        print("✅ Admin created")
    else:
        print("ℹ️ Admin already exists")


