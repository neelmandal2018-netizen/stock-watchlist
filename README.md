# Stock Watchlist

A simple Python script that fetches real-time stock prices and daily percentage changes for a configurable list of tickers using Yahoo Finance.

## Features

- Fetches current price and daily change (both $ and %) for each ticker
- Clean, color-coded terminal output
- Easy to customize ticker list
- Uses `yfinance` (no API key required)

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