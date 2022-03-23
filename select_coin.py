from make_log import *
from indicator import *
from config import *
import pyupbit
import time
import operator

fixed_tickers = ['KRW-BTC', 'KRW-ETH']

# 대상 코인 판단
def sort_tickers():
    tickers = pyupbit.get_tickers(fiat="KRW")
    tickers_info = {}
    result_list = []
    for ticker in tickers:
        time.sleep(0.2)
        df = pyupbit.get_ohlcv(ticker=ticker, interval=get_base_interval(), count=2)
        if df is not None and len(df) > 1:
            tickers_info[ticker] = get_va(df,len(df)).iloc[-1]
    sorted_result = sorted(tickers_info.items(), key=operator.itemgetter(1), reverse=True)
    for item in sorted_result[:2]:
        result_list.append(item[0])
    return result_list

def get_fixed_tickers():
    return fixed_tickers