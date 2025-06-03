from flask import jsonify
from app.users_data import users

def get_users():
    return jsonify(users)
