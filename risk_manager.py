import math

def compute_risk_per_contract(entry_underlying, stop_underlying, lot_size=1, contract_multiplier=1):
    # Risk per contract in INR
    distance = abs(entry_underlying - stop_underlying)
    risk = distance * lot_size * contract_multiplier
    return risk

def compute_position_size(account_value, risk_pct, risk_per_contract, lot_size=1):
    risk_amount = account_value * risk_pct
    if risk_per_contract <= 0:
        return 0
    contracts = math.floor(risk_amount / risk_per_contract)
    # round down to nearest lot
    if contracts < 1:
        return 0
    return contracts