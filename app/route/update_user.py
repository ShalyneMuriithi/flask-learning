from flask import request, jsonify
from app.users_data import users

def update_user(user_id):
    updated_data = request.get_json()
    for user in users:
        if user['id'] == user_id:
            user.update(updated_data)
            return jsonify(user)
    return jsonify({"error": "User not found"}), 404
