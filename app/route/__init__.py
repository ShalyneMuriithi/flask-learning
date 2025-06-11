from flask import Blueprint

routes_bp = Blueprint('routes_bp', __name__)

# Impor
from app.route.get_users import get_users
from app.route.create_user import create_user
from app.route.get_user_by_id import get_user_by_id
from app.route.update_user import update_user
from app.route.delete_user import delete_user
