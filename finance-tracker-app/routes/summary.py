# routes/summary.py

from flask import Blueprint, jsonify
from models import User

summary_bp = Blueprint('summary', __name__)


@summary_bp.route('/<user_id>/summary', methods=['GET'])
def get_summary(user_id):
    user = User.find_user_by_id(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    transactions = user['transactions']
    income = sum(t['amount'] for t in transactions if t['transaction_type'] == 'income')
    expenses = sum(t['amount'] for t in transactions if t['transaction_type'] == 'expense')
    balance = income - expenses

    return jsonify({
        'income': income,
        'expenses': expenses,
        'balance': balance
    }), 200
