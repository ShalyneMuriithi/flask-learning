from flask import request, jsonify
from app.models import db, User
from . import routes_bp

@routes_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    if 'name' in data:
        user.name = data['name']
    if 'email' in data:
        user.email = data['email']

    db.session.commit()
    return jsonify(user.to_dict())
