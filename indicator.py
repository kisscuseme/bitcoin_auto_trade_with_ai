# 이동평균선
def get_ma(df, n):
    return df['close'].rolling(window=n).mean()

# 거래량평균선
def get_va(df, n):
    return df['value'].rolling(window=n).mean()

# 노이즈 비율
def get_noise_ratio(df, n=None):
    if n is None:
        n = 10
    noise_ratio = 1 - abs(df['open']-df['close'])/(df['high']-df['low'])
    return noise_ratio.rolling(window=n).mean()

# 변동성 돌파 매수 여부
def get_volatility_break(df, k=None):
    if k is None:
        k = get_noise_ratio(df).iloc[-2]
    target_price = (df['close'] + (df['high'] - df['low'])*k).iloc[-2]
    current_price = df['close'].iloc[-1]
    if current_price > target_price:
        return True
    else:
        return False