# routes/transactions.py

from flask import Blueprint, request, jsonify
from models import Transaction, User

transactions_bp = Blueprint('transactions', __name__)


@transactions_bp.route('/<user_id>/transactions', methods=['POST'])
def add_transaction(user_id):
    data = request.get_json()
    amount = data.get('amount')
    category = data.get('category')
    transaction_type = data.get('transaction_type')
    date = data.get('date')

    transaction = Transaction(amount, category, transaction_type, date).to_dict()
    User.add_transaction(user_id, transaction)

    return jsonify({'message': 'Transaction added successfully'}), 201


@transactions_bp.route('/<user_id>/transactions', methods=['GET'])
def get_transactions(user_id):
    user = User.find_user_by_id(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    return jsonify(user['transactions']), 200
