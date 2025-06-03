from flask import jsonify
from app.users_data import users

def get_user_by_id(user_id):
    for user in users:
        if user["id"] == user_id:
            return jsonify(user)
    return jsonify({"error": "User not found"}), 404
