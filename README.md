# Simple ATM Server

This project implements a **simple ATM server** with the following actions:

* **Create an Account**
* **Delete an Account**
* **Get Balance** – Retrieve the current balance of an account
* **Withdraw** – Withdraw a specified amount of money from the account
* **Deposit** – Deposit a specified amount of money into the account

---

## Running the Server

Run the server from the command line:

```bash
python ATM_Server.py
```

> The server will start and display the address it’s running on. We will refer to it as `{address}` in the examples below.

---

## API Endpoints & Usage

### 1. Create Account

**Endpoint:** `POST /accounts/{account_number}`

**Command:**

```bash
curl -X POST {address}/accounts/{account_number}
```

---

### 2. Get Balance

**Endpoint:** `GET /accounts/{account_number}/balance`

**Command:**

```bash
curl {address}/accounts/{account_number}/balance
```

> Replace {address} with the server's address, and {account_number} in the wanted account number.
---

### 3. Deposit Money

**Endpoint:** `POST /accounts/{account_number}/deposit`

**Command :**

```cmd
curl -X POST -H "Content-Type: application/json" -d "{\"amount\":{desired_amount}}" {address}/accounts/{account_number}/deposit
```

> Replace {desired_amount} with the desired deposit amount, {address} with the server's address, and {account_number} in the wanted account number.

---

### 4. Withdraw Money

**Endpoint:** `POST /accounts/{account_number}/withdraw`

**Command:**

```cmd
curl -X POST -H "Content-Type: application/json" -d "{\"amount\":{desired_amount}}" {address}/accounts/{account_number}/withdraw
```

> Replace {desired_amount} with the desired withdraw amount, {address} with the server's address, and {account_number} in the wanted account number.

---

### 5. Delete Account

**Endpoint:** `DELETE /accounts/{account_number}`

**Command:**

```bash
curl -X DELETE {address}/accounts/{account_number}
```

> Replace {address} with the server's address, and {account_number} in the wanted account number.

---