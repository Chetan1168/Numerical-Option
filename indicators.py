import numpy as np
import pandas as pd

def atr_daily(df_daily, n=20):
    # df_daily indexed by date with columns high, low, close
    high = df_daily['high']
    low = df_daily['low']
    close = df_daily['close']
    tr1 = high - low
    tr2 = (high - close.shift(1)).abs()
    tr3 = (low - close.shift(1)).abs()
    tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
    return tr.rolling(n).mean()

def ema(series, span):
    return series.ewm(span=span, adjust=False).mean()

def vwap(df):
    pv = df['close'] * df['volume']
    return pv.cumsum() / df['volume'].cumsum()

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
    atr = tr.rolling(n).mean()
    plus_di = 100 * pd.Series(plus_dm, index=df.index).rolling(n).sum() / atr
    minus_di = 100 * pd.Series(minus_dm, index=df.index).rolling(n).sum() / atr
    dx = (abs(plus_di - minus_di) / (plus_di + minus_di)) * 100
    adx = dx.rolling(n).mean()
    return adx

def is_breakout_from_prev5(df_5min):
    # df_5min includes current closed candle as last row
    if len(df_5min) < 6:
        return None
    prev5 = df_5min.iloc[-6:-1]  # 5 completed candles before current
    highest = prev5['high'].max()
    lowest = prev5['low'].min()
    last_close = df_5min.iloc[-1]['close']
    if last_close > highest:
        return 'call'
    if last_close < lowest:
        return 'put'
    return None

def avg_volume_prev_n(df_5min, n=20):
    if len(df_5min) < n+1:
        return df_5min['volume'].mean()
    prev = df_5min.iloc[-n-1:-1]
    return prev['volume'].mean()