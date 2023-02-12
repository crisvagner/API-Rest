from flask import Flask, Blueprint
import dotenv
import os

dotenv.load_dotenv(dotenv.find_dotenv())
DATABASE = os.getenv("DATABASE")


class Server():
    def __init__(self):
        self.app = Flask(__name__)

        self.app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.app.config['PROPAGATE_EXCEPTIONS'] = True

        # Aprendendo a testar a API sem a nescessidade do uso do Postman ou Insomnia
        # user_router = Blueprint("user_router", __name__, url_prefix='apiUser')
        # post_router = Blueprint("post_router", __name__, url_prefix='apiPost')

        # self.app.register_blueprint(post_router)
        # self.app.register_blueprint(user_router)

    def run(self):
        self.app.run(
            port=5000,
            debug=True,
            host='0.0.0.0'
        )


server = Server()
