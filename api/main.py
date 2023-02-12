from src.controllers.UserController import *
from src.controllers.PostController import *
from server.instance import server
from db.services import db, ma


app = server.app


@app.before_first_request
def create_tables():
    db.create_all()


@app.route('/')
def index():
    return jsonify({'message': 'Not Found'}), 404


if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)
    server.run()
