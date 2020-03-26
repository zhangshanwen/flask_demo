from flask import Flask

app = Flask("flask_demo")

app.config.from_json("config/settings.json")
ctx = app.app_context()
ctx.push()

from .user_app import login, user

app.register_blueprint(login)