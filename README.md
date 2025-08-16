# Simple ATM Server

This project implements a **simple ATM server** with the following actions:

* **Create an Account**
* **Delete an Account**
* **Get Balance** – Retrieve the current balance of an account
* **Withdraw** – Withdraw a specified amount of money from the account
* **Deposit** – Deposit a specified amount of money into the account

---
## Approach

The ATM server is implemented as a RESTful API using Flask and Flask-RESTful, which allows clients to interact with the server over HTTP.

Each account is stored in memory as a dictionary entry (accounts) with the account number as the key and the current balance as the value.

The server reads POST request bodies as JSON using request.get_json(force=True), ensuring structured input for deposit and withdraw operations.

The server also reads the PORT environment variable to support deployment on cloud platforms, where the port is dynamically assigned.

---

## Design Decisions

1. **Separate Class per Action**

   Each main action - Account, Balance, Deposit, Withdraw - is implemented as a separate Flask-RESTful Resource class.  This decision improves modularity: each class encapsulates the logic for one type of operation, making the code easier to read, maintain, and extend.

    Future operations (e.g., transfer between accounts) can be added as new classes without modifying existing ones.


2. **Error Handling with abort()**

    All invalid operations, like withdrawing more than the balance or accessing a non-existent account, trigger proper HTTP error responses with messages.


3. **Cloud-Ready Configuration**

    Using os.environ.get("PORT", 8080) allows the server to adapt automatically to cloud environments.

---

## Challenges

1. **Learning About Servers** Understanding how to set up a server and handle requests from clients.


2. **Cloud Deployment** Figuring out how to deploy the server to a cloud platform and make it accessible online.

---

# How To Use

## Running the Server

Run the server from the command line:

```bash
python ATM_Server.py
```

> The server will start and display the address it’s running on. We will refer to it as `{address}` in the examples below.


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