from flask import Flask
from flask_smorest import Api
from db import db
from resources.contact import blp as ContactBlueprint
from flask_migrate import Migrate


def create_app(db_url=None):
    app = Flask(__name__)
    app.config["API_TITLE"] = "Contact Manager API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or "sqlite:///data.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True
    migrate = Migrate(app, db)
    # Initialize the SQLAlchemy extension
    db.init_app(app)

    with app.app_context():
        db.create_all()

    api = Api(app)
    api.register_blueprint(ContactBlueprint)

    return app


if __name__ == '__main__':
    create_app().run(debug=True)
