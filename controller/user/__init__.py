from flask import Blueprint
from middleware.jwt_handel import jwt_request

login_bp = Blueprint('login', __name__)
users_bp = Blueprint('users', __name__)

# register middleware for buleprint
users_bp.before_request(jwt_request)
