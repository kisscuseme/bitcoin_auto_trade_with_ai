import threading
import copy

from check_time import *
from conditions import *
from select_coin import *
from trade_test import *

tempBuyList = []
buyList = []
sellList = []

# 매도 판단
def loop_sell():
    global sellList
    while True:
        if get_running():
            if target_time(0):
                try:
                    for ticker in sellList:
                        current_price = pyupbit.get_current_price(ticker)
                        time.sleep(1)
                        if sell_conditions(ticker, current_price):
                            sell_price = pyupbit.get_orderbook(ticker)['orderbook_units'][0].get('bid_price') # for test
                            time.sleep(1)
                            sell(ticker, sell_price, get_balances())
                    sellList = []
                except Exception as ex:
                    type = '에러'
                    log = 'loop_sell error! ' + str(ex)
                    make_log(type, log, detail=True)
        time.sleep(1)

#타겟 코인 선정
def loop_select_ticker():
    global tempBuyList
    while True:
        if get_running():
            if target_time(2):
                tempBuyList = list(set(sort_tickers() + get_fixed_tickers()))
                make_log('정보', str(tempBuyList))
        time.sleep(1)

# 매수 판단
def loop_buy():
    global buyList
    while True:
        if get_running():
            if target_time(5):
                try:
                    buyList = copy.deepcopy(tempBuyList)
                    krw_balance = get_krw_balance(get_balances())
                    for ticker in buyList:
                        if ticker not in sellList:
                            balance_index = get_index(get_balances(), 'currency', ticker[4:])
                            if  krw_balance >= 5000 and balance_index is None:
                                if buy_conditions(ticker):
                                    buy_price = pyupbit.get_orderbook(ticker)['orderbook_units'][0].get('ask_price') # for test
                                    time.sleep(1)
                                    buy(ticker, buy_price, get_balances(), krw_balance/len(buyList))
                                    sellList.append(ticker)
                except Exception as ex:
                    type = '에러'
                    log = 'loop_buy error! ' + str(ex)
                    make_log(type, log, detail=True)
        time.sleep(1)

def main():
    sell = threading.Thread(target=loop_sell, daemon=True)
    buy = threading.Thread(target=loop_buy, daemon=True)
    select = threading.Thread(target=loop_select_ticker, daemon=True)
    sell.start()
    buy.start()
    select.start()
    sell.join()
    buy.join()
    select.join()

main()