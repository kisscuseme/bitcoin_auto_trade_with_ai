import time
from deep_learning import predict_buy
from make_log import make_log
from indicator import *
from config import *
import pyupbit
from util import get_num_to_str

# 매도 조건
def sell_conditions(pTicker, current_price):
    try:
        make_log('정보', pTicker + ': ' + str(current_price) + ': 매도 조건 항상 True', detail=True)
        return True
    except Exception as ex:
        type = '에러'
        log = 'sell_conditions error! ' + str(ex)
        make_log(type, log, detail=True)
        return False

# 매수 조건
def buy_conditions(pTicker):
    try:
        df = pyupbit.get_ohlcv(pTicker, get_base_interval(), 21)
        if len(df) > 20:
            ma5 = get_ma(df, 5)
            ma20 = get_ma(df, 20)
            va3 = get_va(df, 3)
            va5 = get_va(df, 5)
            cond_ma = ma20.iloc[-1] < ma5.iloc[-1] and ma5.iloc[-1] < df['close'].iloc[-1]
            cond_va = va5.iloc[-1] < va3.iloc[-1]
            cond_vb = get_volatility_break(df)
            time.sleep(1)
            ai = predict_buy(pTicker)
            cond_ai = ai['accuracy'] * ai['predict'] > 0.5 if ai is not None else True

            log_msg1 = 'ma20: ' + get_num_to_str(ma20.iloc[-1]) + ', ma5: ' + get_num_to_str(ma5.iloc[-1]) + ', price: ' + get_num_to_str(df['close'].iloc[-1])
            log_msg2 = 'va5: ' + get_num_to_str(va5.iloc[-1]) + ', va3: ' + get_num_to_str(va3.iloc[-1])
            log_msg3 = 'vb: ' + str(cond_vb) + ' ,ai: ' + str(ai)
            make_log('정보', pTicker[4:] + ' 매수 조건 ' + log_msg1 + ', ' + log_msg2 + ', ' + log_msg3, detail=True)
            
            return cond_ma and cond_va and cond_vb and cond_ai
        else:
            return False
    except Exception as ex:
        type = '에러'
        log = 'buy_conditions error! : ' + pTicker + ' : ' + str(ex)
        make_log(type, log, detail=True)
        return False
