import os
import pandas as pd

def load_daily(symbol, daily_dir):
    path = os.path.join(daily_dir, f"{symbol}.csv")
    # Expect columns: date, open, high, low, close, volume, value (value = price*volume)
    df = pd.read_csv(path, parse_dates=["date"])
    df = df.sort_values("date").set_index("date")
    return df

def load_intraday_5min(symbol, intraday_dir):
    path = os.path.join(intraday_dir, f"{symbol}_5min.csv")
    # Expect columns: datetime, open, high, low, close, volume
    df = pd.read_csv(path, parse_dates=["datetime"])
    df = df.sort_values("datetime").set_index("datetime")
    return df

def load_iv_history(symbol, iv_dir):
    path = os.path.join(iv_dir, f"{symbol}_iv.csv")
    # Expect columns: date, iv (in decimal, e.g., 0.25 for 25%)
    df = pd.read_csv(path, parse_dates=["date"])
    df = df.sort_values("date").set_index("date")
    return df