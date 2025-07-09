from app.extensions import db, bcrypt

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def hash_password(self, password):
        """Hashes the password before storing."""
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        """Verifies if the provided password matches the stored hash."""
        return bcrypt.check_password_hash(self.password, password)

    def to_dict(self):
        """Return user data excluding the password."""
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email
        }
