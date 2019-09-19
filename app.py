from flask import Blueprint, Flask, render_template
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from util.db import DB
from controller.api.v1 import user

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'test'
jwt = JWTManager(app)
CORS(app)

app.register_blueprint(user.app)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)


