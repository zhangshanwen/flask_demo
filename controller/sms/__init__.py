from flask import Blueprint
from middleware.handel import base_request

sms_bp = Blueprint('sms', __name__)

# register middleware for buleprint
# login.before_request(base_request)
