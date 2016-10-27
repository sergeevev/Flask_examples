# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

__author__ = 'sergeevev'

db = SQLAlchemy()


def create_app():
    from models import db
    from views import product_views, order_views, base_views

    app = Flask(__name__)
    app.config.update({
        'DEBUG': True,
        'SECRET_KEY': 'SOME s addsdas d',
        'SQLALCHEMY_TRACK_MODIFICATIONS': True,
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///test.db',
    })

    app.register_blueprint(product_views)
    app.register_blueprint(order_views)
    app.register_blueprint(base_views)

    db.init_app(app=app)

    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()
