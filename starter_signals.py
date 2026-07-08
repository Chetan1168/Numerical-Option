import pandas as pd
import numpy as np

def atr(df, n=20):
    high = df['high']
    low = df['low']
    close = df['close']
    tr1 = high - low
    tr2 = (high - close.shift(1)).abs()
    tr3 = (low - close.shift(1)).abs()
    tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
    return tr.rolling(n).mean()

def ema(df, span):
    return df['close'].ewm(span=span, adjust=False).mean()

def vwap(df):
    pv = (df['close'] * df['volume'])
    return pv.cumsum() / df['volume'].cumsum()

# ADX helper (simplified)
def adx(df, n=14):
    high = df['high']; low = df['low']; close = df['close']
    up = high.diff()
    down = -low.diff()
    plus_dm = np.where((up > down) & (up > 0), up, 0.0)
    minus_dm = np.where((down > up) & (down > 0), down, 0.0)
    tr1 = high - low
    tr2 = (high - close.shift(1)).abs()
    tr3 = (low - close.shift(1)).abs()
    tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
    atr_ = tr.rolling(n).mean()
    plus_di = 100 * pd.Series(plus_dm).rolling(n).sum() / atr_
    minus_di = 100 * pd.Series(minus_dm).rolling(n).sum() / atr_
    dx = (abs(plus_di - minus_di) / (plus_di + minus_di)) * 100
    return dx.rolling(n).mean()

def is_breakout(df):
    # df is resampled on 5-min timeframe and includes last closed candle
    # Get previous 5 completed candles (exclude current)
    if len(df) < 7:
        return None
    prev5 = df.iloc[-6:-1]  # 5 completed candles before current
    highest = prev5['high'].max()
    lowest = prev5['low'].min()
    last_close = df.iloc[-1]['close']
    if last_close > highest:
        return 'call'
    if last_close < lowest:
        return 'put'
    return None

# Example usage:
# df = fetch_5min_ohlcv(symbol, limit=200) # implement fetch_5min_ohlcv
# df should have columns: ['open','high','low','close','volume'] indexed by datetime
# compute indicators:
# df['atr20'] = atr(df, 20)
# df['ema20'] = ema(df, 20); df['ema50'] = ema(df, 50)
# df['adx14'] = adx(df, 14)
# df['vwap'] = vwap(df)
# then apply your boolean checks in sequence (volume, trend, index, sector, gap, IV)