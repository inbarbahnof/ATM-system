# Simple ATM Server Code

This project implements a simple ATM server with the following actions:

- **Create an Account**
- **Delete an Account**
- **Get Balance** – Retrieve the current balance of an account
- **Withdraw** – Withdraw a specified amount of money from the account
- **Deposit** – Deposit a specified amount of money into the account

---

## Instructions To Use The Server

1. Run the server - in command line:
   python ATM_Server.py

   note: this will give you the address the server runs on - we will call it {address}

2. Create Account - **POST /accounts/{account_number}** - in command line:
   curl -X POST {address}/accounts/{account_number}

3. Get Balance - **GET /accounts/{account_number}/balance** - in commal line:
   curl {address}/accounts/{account_number}/balance
  
4. Deposit - **POST /accounts/{account_number}/deposit** - in command line:
   curl -X POST -H "Content-Type: application/json" -d "{\"amount\":{desired_amount}}" {address}/accounts/{account_number}/deposit

5. Withdraw - **POST /accounts/{account_number}/withdraw** - in command line:
   curl -X POST -H "Content-Type: application/json" -d "{\"amount\":{desired_amount}}" {address}/accounts/{account_number}/withdraw

6. Delete Account - **DELETE /accounts/{account_number}** - in command line:
   curl -X DELETE {address}/accounts/{account_number}

---
