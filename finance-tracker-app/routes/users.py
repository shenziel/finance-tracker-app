# routes/users.py

from flask import Blueprint, request, jsonify
from models import User
from flask_bcrypt import bcrypt
import jwt
import datetime

users_bp = Blueprint('users', __name__)
SECRET_KEY = 'your_secret_key'


@users_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if User.find_user(username):
        return jsonify({'message': 'User already exists'}), 400

    User.create_user(username, password)
    return jsonify({'message': 'User registered successfully'}), 201


@users_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    print(username)
    print(password)

    user = User.find_user(username)
    if user and user['password'] == password: #improve pwd verification with bcrypt hash
        token = jwt.encode({
            'user_id': str(user['_id']),
            'exp': datetime.datetime.now(datetime.UTC) + datetime.timedelta(hours=1)
        }, SECRET_KEY, algorithm='HS256')
        print(token)
        return jsonify({'message': 'Login successful', 'user_id': str(user['_id']), 'token': token}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401



