from flask import Flask, request
from flask_restful import Resource, Api, abort
import os
import threading

db_lock = threading.Lock()
app = Flask("ATM_Api")
api = Api(app)

accounts = {}


@app.route("/")
def index():
    return "ATM API is running!", 200


def get_account(account_number):
    """Checks if account_number exists, if so - returns its balance"""
    if account_number not in accounts:
        abort(404, message=f"Account {account_number} was not found.")

    return accounts[account_number]


class Account(Resource):
    def post(self, account_number):
        """Creates a new account with a balance of 0."""
        with db_lock:
            if account_number in accounts:
                abort(406, message=f"Account {account_number} already exists.")
            accounts[account_number] = 0
            return {"account_number": account_number, "balance": 0}, 201

    def delete(self, account_number):
        """Deletes an existing account."""
        with db_lock:
            if account_number not in accounts:
                abort(404, message=f"Account {account_number} was not found.")
            del accounts[account_number]
            return "", 204


class Balance(Resource):
    def get(self, account_number):
        """Retrieves the current balance of an account."""
        with db_lock:
            balance = get_account(account_number)
            return {"account_number": account_number, "balance": balance}, 200


class Withdraw(Resource):
    def post(self, account_number):
        """Withdraws a specified amount from an account."""
        with db_lock:
            balance = get_account(account_number)
            data = request.get_json(force=True)
            amount = data.get("amount")

            if amount is None or amount <= 0:
                abort(400, message="Invalid withdraw amount.")

            if balance < amount:
                abort(400, message="The specified account does not have enough money.")

            accounts[account_number] -= amount
            return {"account_number": account_number, "balance": accounts[account_number]}, 200


class Deposit(Resource):
    def post(self, account_number):
        """Deposits a specified amount into an account."""
        with db_lock:
            get_account(account_number)
            data = request.get_json(force=True)
            amount = data.get("amount")

            if amount is None or amount <= 0:
                abort(400, message="Invalid deposit amount.")

            accounts[account_number] += amount
            return {"account_number": account_number, "balance": accounts[account_number]}, 200


api.add_resource(Account, '/accounts/<account_number>')
api.add_resource(Balance, '/accounts/<account_number>/balance')
api.add_resource(Withdraw, '/accounts/<account_number>/withdraw')
api.add_resource(Deposit, '/accounts/<account_number>/deposit')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run()
