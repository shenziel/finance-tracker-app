# routes/__init__.py

from flask import Blueprint
from .users import users_bp
from .transactions import transactions_bp
from .summary import summary_bp

def register_blueprints(app):
    app.register_blueprint(users_bp, url_prefix='/users')
    app.register_blueprint(transactions_bp, url_prefix='/users')
    app.register_blueprint(summary_bp, url_prefix='/users')
