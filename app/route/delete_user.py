from flask import jsonify
from app.users_data import users

def delete_user(user_id):
    for user in users:
        if user['id'] == user_id:
            users.remove(user)
            return jsonify({"message": f"User {user_id} deleted"})
    return jsonify({"error": "User not found"}), 404
