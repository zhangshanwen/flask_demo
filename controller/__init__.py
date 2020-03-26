from flask import Flask

from .user_app import login

app = Flask(__name__)
app.register_blueprint(login)
