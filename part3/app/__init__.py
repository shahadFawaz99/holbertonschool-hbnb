# app/__init__.py
from flask import Flask
from app.extensions import db, bcrypt, jwt

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hbnb.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'supersecretkey'

    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    return app

