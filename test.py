import pyupbit
import math
from deep_learning import predict_buy

# df = pyupbit.get_ohlcv(count=7, interval='minute60')

# print(df.index.hour)
# print(df.index.hour/6)
# print(math.floor(df.index[1].hour/6))

print(predict_buy("KRW-ETH"))