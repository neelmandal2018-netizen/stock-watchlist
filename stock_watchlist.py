#!/usr/bin/env python3
"""
Stock Watchlist - Fetches current prices and daily changes for a list of tickers.
"""

import yfinance as yf

# ============================================================
# CONFIGURATION - Edit this list to add/remove tickers
# ============================================================
TICKERS = ["AAPL", "TSLA", "INFY"]


def fetch_stock_data(ticker: str) -> dict | None:
    """
    Fetch current price and daily change for a single ticker.
    Returns a dict with price info or None if the ticker is invalid.
    """
    try:
        stock = yf.Ticker(ticker)
        # Get 2 days of history to calculate daily change
        hist = stock.history(period="2d")

        if hist.empty:
            print(f"  {ticker}: No data found (invalid ticker?)")
            return None

        current_price = hist["Close"].iloc[-1]
        previous_close = hist["Close"].iloc[-2] if len(hist) > 1 else current_price

        change_dollar = current_price - previous_close
        change_percent = (change_dollar / previous_close) * 100 if previous_close else 0

        return {
            "ticker": ticker,
            "price": current_price,
            "change_dollar": change_dollar,
            "change_percent": change_percent,
        }

    except Exception as e:
        print(f"  {ticker}: Error fetching data - {e}")
        return None


def format_change(change_percent: float) -> str:
    """Format the percent change with sign."""
    sign = "+" if change_percent >= 0 else ""
    return f"({sign}{change_percent:.2f}%)"


def main():
    for ticker in TICKERS:
        data = fetch_stock_data(ticker)
        if data:
            change_str = format_change(data["change_percent"])
            print(f"{data['ticker']}:  ${data['price']:.2f}  {change_str}")


if __name__ == "__main__":
    main()