from util import get_index

balances = [{'currency':'KRW','balance':50000000}]

def get_balances():
    return balances

def get_balance_index(ticker, balances):
    value = 'KRW'
    if ticker != 'KRW':
        value = ticker[4:]
    return get_index(balances, 'currency', value)

def get_krw_balance(balances):
    return balances[get_balance_index('KRW', balances)]['balance']

def total_balance(balances):
    total = 0
    for balance in balances:
        if balance['currency'] == 'KRW':
            total += balance['balance']
        else:
            total += balance['balance']*balance['avg_buy_price']
    return total