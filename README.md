# F&O Options Breakout Simulator

This repo contains a simulator that implements the full ruleset you provided.

Overview
- 20 trading days ATR on daily candles
- 5-minute intraday filters and breakout logic
- Option ATM weekly selection with DTE >= 2
- Time windows: entries 09:30–14:30, exit all at 15:20
- Liquidity, gap, IV rank, trend, sector/index confirmations (some placeholders)
- Stops, moving stops, partial exits, trailing, position sizing, trade & loss limits

Files included:
- simulator_bot.py — orchestrator and backtest runner
- data_fetcher.py, indicators.py, option_pricer.py, risk_manager.py, broker_simulator.py
- config.yaml, requirements.txt, README.md
- scripts/generate_synthetic.py — generates synthetic daily/5min/IV CSVs for demo
- .github/workflows/ci.yml — CI that runs the synthetic demo and uploads trades_log.csv

Notes
- This is a simulator-only scaffold. Configure lot sizes, contract multipliers, and real data feeds before using in production.
