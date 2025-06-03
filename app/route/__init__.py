from flask import Blueprint
from app.route.get_users import get_users
from app.route.get_user_by_id import get_user_by_id
from app.route.create_user import create_user
from app.route.update_user import update_user
from app.route.delete_user import delete_user

routes_bp = Blueprint('routes_bp', __name__)

routes_bp.route('/users', methods=['GET'])(get_users)
routes_bp.route('/users/<int:user_id>', methods=['GET'])(get_user_by_id)
routes_bp.route('/users', methods=['POST'])(create_user)
routes_bp.route('/users/<int:user_id>', methods=['PUT'])(update_user)
routes_bp.route('/users/<int:user_id>', methods=['DELETE'])(delete_user)
