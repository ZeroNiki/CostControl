# Cost Control Django API
## About
Application for managing expense categories and transactions using Django REST Framework and JWT authentication. Users can create, view and filter categories and transactions through the API.

## Install
### Installing dependencies
1. Clone repo:
```sh
git clone https://github.com/ZeroNiki/CostControl.git

cd CostControl
```

2. Create and activate a virtual environment:
```sh
python3 -m venv venv
source venv/bin/activate  
```

3. Install dependencies:
```sh
pip install -r requirements.txt
```

4. Go to `expense_tracker`:
```sh
cd expense_tracker/
```

### Setting up the .env file
```
# Django secret token
SECRET=your_secret_key_here

# PostgreSQL 
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASS=your_database_password
DB_HOST=your_database_host
DB_PORT=your_database_port

DB_TEST_NAME=test_your_database_name
```
Replace your_secret_key_here, your_database_name, and other parameters with real values.
Make sure the `.env` contains the correct details to connect to your PostgreSQL database.

### Applying Migrations
```sh
python manage.py migrate
```
### Run server
```
python3 manage.py runserver
```

go to *http://127.0.0.1:8000/*

## Example routes
### Categories
- GET `/api/categories/`: list all user categories
- POST `/api/categories/`: add category
- GET `/api/categories/{id}/`: find category by id
- PUT | PATCH `/api/categories/{id}/`: update category 
- DELETE `/api/categories/{id}/`: delete category by id

### Login
- POST `/api/login`: login user (and get jwt token) 
- POST `/api/login/refresh`: refresh jwt

### Authentication 
- POST `/api/register/`: register new user

### Transactions:
- GET `/api/transactions/`: get all transactions
- POST `/api/transactions/`: add transaction
- GET `/api/transactions/{id}/`: find transaction by id
- PUT | PATCH `/api/transactions/{id}/`: update transaction
- DELETE `/api/transactions/{id}/`: delete transaction by id

## Usage
go to *http://127.0.0.1:8000/api/docs/*

go to `Authentication` `/api/register`. Register new user
```json
{
  "Message": "User registered successfully!",
  "Refresh": "smth",
  "Access": "smth"
}
```
copy `Access` token. Click on the button `Authorize` and paste token into value.
Now, you can usage Categories API and Transactions API 

## Tests
to run tests use:
```sh
python3 manage.py test
```
