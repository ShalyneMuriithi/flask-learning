from flask import request, jsonify
from app.users_data import users

def create_user():
    new_user = request.get_json()
    if not new_user or 'name' not in new_user or 'email' not in new_user:
        return jsonify({"error": "Missing name or email"}), 400

    new_id = max([u['id'] for u in users]) + 1 if users else 1
    new_user['id'] = new_id
    users.append(new_user)
    return jsonify(new_user), 201
