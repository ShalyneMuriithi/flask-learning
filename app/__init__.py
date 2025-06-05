from flask import Flask
from app.models import db
from app.route import routes_bp

def create_app():
    app = Flask(__name__)

    # MySQL connection  username, password, db name)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost/mydatabase'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app) #this connect db to the app

    app.register_blueprint(routes_bp)

    return app
