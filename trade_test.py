from make_log import make_log
from util import *
from balances import *
import time

def buy(pTicker, current_price, balances, change):
    try:
        balance = get_krw_balance(balances)
        price = current_price
        needs = change * 1.0005
        if balance < needs:
            needs = balance
            change = needs / 1.0005
        volume = change / price
        balance_index = get_balance_index(pTicker, balances)

        if balance_index is None:
            balances.append({'currency': pTicker[4:], 'balance': volume, 'avg_buy_price': price})
        else:
            old_volume = balances[balance_index]['balance']
            old_price = balances[balance_index]['avg_buy_price']
            balances[balance_index]['balance'] = old_volume + volume
            balances[balance_index]['avg_buy_price'] = (old_price*old_volume + price*volume)/(old_volume+volume)

        balances[get_index(balances,'currency','KRW')]['balance'] -= needs
        type = '매수'
        log = pTicker[4:] + ' --> ' + get_num_to_str(needs) + ' / price ' + get_num_to_str(price)
        log += ' / vol. ' + get_num_to_str(volume) + ' / balance ' + get_num_to_str(get_krw_balance(balances))
        log += ' / total ' + get_num_to_str(total_balance(balances))
        make_log(type, log)
        time.sleep(0.1)
    except Exception as ex:
        print('test_buy error!', ex)


def sell(pTicker, current_price, balances):
    try:
        price = current_price
        balance_index = get_balance_index(pTicker, balances)
        volume = balances[balance_index]['balance']
        change = price * volume * 0.9995
        balances[get_index(balances,'currency','KRW')]['balance'] += change
        sign = ' (-) '
        res = price > balances[balance_index]['avg_buy_price']
        if res:
            sign = ' (+) '
        balances.pop(balance_index)
        type = '매도'
        log = pTicker[4:] + sign + get_num_to_str(change) + ' / price ' + get_num_to_str(price)
        log += ' / vol. ' + get_num_to_str(volume) + ' / balance ' + get_num_to_str(get_krw_balance(balances))
        log += ' / total ' + get_num_to_str(total_balance(balances))
        make_log(type, log)
        time.sleep(0.1)
        return res
    except Exception as ex:
        print('test_sell error!', ex)