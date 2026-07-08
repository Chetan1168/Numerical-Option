import math
from scipy.stats import norm
import datetime

def bs_price(S, K, r, sigma, T, kind='call'):
    # S: spot, K: strike, r: risk-free (annual), sigma: iv (annual), T: time to expiry in years
    if T <= 0:
        if kind == 'call':
            return max(S - K, 0.0)
        else:
            return max(K - S, 0.0)
    d1 = (math.log(S / K) + (r + 0.5 * sigma * sigma) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    if kind == 'call':
        price = S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
    else:
        price = K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    return price

def time_to_expiry_days(expiry_date, current_date):
    # expiry_date and current_date are datetime.date
    delta = expiry_date - current_date
    return max(delta.days, 0)

def find_atm_strike(S, strike_step=1):
    # Round to nearest strike interval (for stocks this varies; user should set)
    return round(S / strike_step) * strike_step