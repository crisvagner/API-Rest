from db.services import db, ma
from server import server
from controllers import controllers

app = server.app


if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)
    server.run()
