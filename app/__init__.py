from flask import Flask, url_for
from werkzeug.middleware.proxy_fix import ProxyFix
from .register import register
from middleware.handel import base_request

# init app
app = Flask("flask_demo")
# init settings
app.config.from_json("config/settings.json")

# init wsgi middleware
app.wsgi_app = ProxyFix(app.wsgi_app)
# create an app context
ctx = app.app_context()
ctx.push()
# register blueprint
register(app)
# register global middleware
app.before_request(base_request)
