from werkzeug.security import generate_password_hash, check_password_hash
from flask import Blueprint, jsonify, request
from flask_cors import cross_origin
from pymongo import MongoClient
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth', __name__, url_prefix='/api/v1/auth')
client = MongoClient("localhost", 27017)
mongo_db = client.flask_database

# COLLECTION FOR THE USERS AND ACCIDENT...
accidents_collection = mongo_db.accidents
users_collection = mongo_db.users

# Route for the user to login...
@auth_bp.route('/login', methods=['POST', 'OPTIONS'])
@cross_origin(supports_credentials=True)
def login():
    login_details = request.get_json()
    user_from_db = users_collection.find_one({'email': login_details['email']})

    if user_from_db:
        print("🔥")
        # Check the entered password against the hashed password
        if check_password_hash(user_from_db['password'], login_details['password']):
            access_token = create_access_token(identity=user_from_db['email'])  # <-- Fixed here
            return jsonify(access_token=access_token), 200
    else:
        return jsonify({'msg': "User does not exist"}), 404
    
    return jsonify({'msg': 'The username or password is incorrect'}), 401

# Route for the user to register...
@auth_bp.route('/register', methods=['POST', 'OPTIONS'])
@cross_origin(supports_credentials=True)
def register():
    new_user = request.get_json()  # store the JSON body request
    new_user['password'] = generate_password_hash(new_user["password"])  # encrypt password
    doc = users_collection.find_one({"email": new_user["email"]})  # check if the user exists
    if not doc:
        users_collection.insert_one(new_user)
        return jsonify({'msg': 'User created successfully'}), 201
    else:
        return jsonify({'msg': 'User already exists'}), 409
