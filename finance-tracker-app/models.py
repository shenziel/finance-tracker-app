# models.py

from bson import ObjectId
from database import mongo

class User:
    @staticmethod
    def create_user(username, password):
        user = {
            "username": username,
            "password": password,
            "transactions": []
        }
        return mongo.db.users.insert_one(user)

    @staticmethod
    def find_user(username):
        return mongo.db.users.find_one({"username": username})

    @staticmethod
    def add_transaction(user_id, transaction):
        return mongo.db.users.update_one(
            {"_id": ObjectId(user_id)},
            {"$push": {"transactions": transaction}}
        )

class Transaction:
    def __init__(self, amount, category, transaction_type, date):
        self.amount = amount
        self.category = category
        self.transaction_type = transaction_type
        self.date = date

    def to_dict(self):
        return self.__dict__
