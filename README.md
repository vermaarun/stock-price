# Getting Started

Please follow below steps to get started with stock-price list APIs

1. Clone this respository : `git clone https://github.com/vermaarun/stock-price.git`
2. `cd stock-price`
3. Create virtual environment : `python3 -m venv venv`
4. Activate virtual environment : `source venv/bin/activate`
5. Install dependencies : `pip install -r requirements.txt`
6. Migrate Migrations/Models : `python manage.py migrate`
7. Run server : `python manage.py runserver`

# Consume Date
1. Put your API KEY(Please, register free account to get API key) in `djangoapi/settings.py` file under `API_KEY` parameter
2. Re-start server
3. Open browser and execute : `http://127.0.0.1:8000/consume`

# List Stock Prices
1. Open browser and execute : `http://127.0.0.1:8000/stock-price/`

To filter for any company, you can use query-parameter like this : `http://127.0.0.1:8000/stock-price?comapny=<company-name>`

**Note: Supported companies as of now - AAPL, AMZN, GOOG**

To filter on basis of date, you can use query-parameter like this : `http://127.0.0.1:8000/stock-price?start=<YYYY-MM-DD>&end=<YYYY-MM-DD>`
