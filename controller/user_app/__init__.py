from flask import Blueprint
from middleware.handel import base_request

login = Blueprint('app', __name__, template_folder='templates')

# register middleware for buleprint
# login.before_request(base_request)
