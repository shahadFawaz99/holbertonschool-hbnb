class Config:
    # Secret key used for session management and JWT security
    SECRET_KEY = 'super-secret-key'
    
    # Disable SQLAlchemy modification tracking for performance
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    # Enable debug mode to show detailed error messages and auto-reload
    DEBUG = True
    
    # Use a local SQLite database during development
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'
