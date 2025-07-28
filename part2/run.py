# run.py

from app.api.user_routes import app  # Import the Flask application instance from user_routes module

if __name__ == '__main__':
    # Start the Flask application in debug mode, enabling live updates and detailed error messages
    app.run(debug=True)
