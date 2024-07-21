# app.py

from flask import Flask
from flask_bcrypt import Bcrypt
from pymongo import MongoClient
from flask_cors import CORS
from database import mongo
from routes.users import users_bp
from routes.transactions import transactions_bp
from routes.summary import summary_bp

USERS_PATH = '/users'

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/finance_tracker'
mongo.init_app(app)

# Enable CORS for all routes
CORS(app)

app.register_blueprint(users_bp, url_prefix=USERS_PATH)
app.register_blueprint(transactions_bp, url_prefix=USERS_PATH)
app.register_blueprint(summary_bp, url_prefix=USERS_PATH)

if __name__ == '__main__':
    app.run(debug=True)
