#!/usr/bin/python3

# Import necessary components from Flask-RESTx and the application's service layer
from flask_restx import Namespace, Resource, fields
from app.services import facade

# Create a namespace for user-related API endpoints
api = Namespace('users', description='User related operations')

# Define the structure of the User model for request validation and Swagger documentation
user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'email': fields.String(required=True, description='Email of the user')
})


@api.route('/')
class UserList(Resource):
    @api.expect(user_model)
    @api.response(201, 'User successfully created')
    @api.response(400, 'Email already registered')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new user"""
        # Extract user data from the request payload
        user_data = api.payload

        # Check if a user with the same email already exists
        existing_user = facade.get_user_by_email(user_data['email'])
        if existing_user:
            return {'error': 'Email already registered'}, 400

        try:
            # Create and return the new user
            new_user = facade.create_user(user_data)
        except (TypeError, ValueError) as e:
            # Handle validation or data errors
            return {'error': str(e)}, 400

        # Return created user data with a 201 Created status
        return new_user.to_dict(), 201

    @api.response(200, 'List of users retrieved successfully')
    def get(self):
        """Retrieve a list of all users"""
        # Get all users from the service layer
        users = facade.get_all_users()

        # Return the list of users with selected attributes
        return {
            'users': [{
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email
            } for user in users]
        }, 200


@api.route('/<user_id>')
class UserResource(Resource):
    @api.response(200, 'User details retrieved successfully')
    @api.response(404, 'User not found')
    def get(self, user_id):
        """Get user details by ID"""
        # Retrieve user by ID
        user = facade.get_user(user_id)
        if not user:
            # Return error if user is not found
            return {'error': 'User not found'}, 404

        # Return user details
        return {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
        }, 200

    @api.expect(user_model, validate=True)
    @api.response(200, 'User updated successfully')
    @api.response(400, 'Invalid input data')
    def put(self, user_id):
        """Update a user's information"""
        # Get updated user data from request payload
        user_data = api.payload
        try:
            # Attempt to update the user
            updated_user = facade.update_user(user_id, user_data)
        except (TypeError, ValueError) as e:
            # Handle validation or type errors
            return {'error': str(e)}, 400

        if not updated_user:
            # Return error if user not found
            return {'error': 'User not found'}, 404

        # Return updated user details
        return {
            'id': updated_user.id,
            'first_name': updated_user.first_name,
            'last_name': updated_user.last_name,
            'email': updated_user.email
        }, 200
