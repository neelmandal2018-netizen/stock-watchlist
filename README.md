# Stock Watchlist

A simple Python script that fetches real-time stock prices and daily percentage changes for a configurable list of tickers using Yahoo Finance.

## Features

- Fetches current price and daily change (both $ and %) for each ticker
- Clean, color-coded terminal output
- Easy to customize ticker list
- Uses `yfinance` (no API key required)
- **Configurable price alerts** — get notified when a stock crosses above/below a threshold

## Installation

```bash
pip install yfinance
```

## Usage

```bash
python stock_watchlist.py
```

Example output:
```
AAPL:  $189.50  (+1.23%)
TSLA:  $248.30  (-0.45%)
INFY:  $32.15   (+0.67%)
```

## Configuration

Edit the `TICKERS` list at the top of `stock_watchlist.py`:

```python
TICKERS = ["AAPL", "TSLA", "INFY", "GOOGL", "MSFT"]
```

Add any valid Yahoo Finance ticker symbols (stocks, ETFs, crypto like `BTC-USD`, etc.).

## Price Alerts

Configure alerts per ticker using the `ALERTS` dictionary at the top of `stock_watchlist.py`. Each ticker can have `"above"` and/or `"below"` thresholds:

```python
ALERTS = {
    "AAPL": {"below": 400},      # Alert if AAPL drops below $400
    "TSLA": {"above": 350},      # Alert if TSLA rises above $350
    "INFY": {"above": 20, "below": 10},  # Alert both ways
}
```

When a threshold is crossed, the output includes a clear warning:

```
AAPL:  $333.74  (+0.14%)
  ALERT: AAPL is below $400!
TSLA:  $380.84  (-2.61%)
  ALERT: TSLA is above $350!
INFY:  $11.49  (-0.35%)
```

Tickers not listed in `ALERTS` are silently skipped (no alerts checked).

## How It Works

- Uses `yfinance` to fetch 2 days of historical data
- Calculates daily change from yesterday's close to current price
- Handles invalid tickers gracefully with error messages

## What I Learned

- `yfinance` is a lightweight wrapper around Yahoo Finance's API — no API key needed
- Fetching 2 days of history (`period="2d"`) lets you compute daily change without a separate "previous close" endpoint
- Python's `yf.Ticker().history()` returns a pandas DataFrame, making price extraction straightforward
- Simple scripts like this are great for learning API integration, error handling, and CLI output formatting

## License

MIT