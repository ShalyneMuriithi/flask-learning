from flask import jsonify
from app.models import User
from app.route import routes_bp  


@routes_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])
