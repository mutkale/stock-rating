import yfinance as yf
import pandas as pd
import sqlite3
import time

from tickers import tickers

# =========================
# DB CONNECTION (FIXED)
# =========================
conn = sqlite3.connect("omxh_quant.db", timeout=30)
cursor = conn.cursor()

# IMPORTANT: enables concurrent reads/writes
cursor.execute("PRAGMA journal_mode=WAL;")

# =========================
# TABLE SETUP
# =========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS stock_price_history (
    date TEXT,
    ticker TEXT,
    open REAL,
    high REAL,
    low REAL,
    close REAL,
    volume REAL
)
""")

conn.commit()

# =========================
# FETCH FUNCTION
# =========================
def get_history(ticker):
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period="1y")

        hist = hist.reset_index()

        # FIX: Timestamp -> string
        hist["Date"] = hist["Date"].dt.strftime("%Y-%m-%d")

        hist["Ticker"] = ticker

        # standardize column names
        hist = hist.rename(columns={
            "Date": "date",
            "Ticker": "ticker",
            "Open": "open",
            "High": "high",
            "Low": "low",
            "Close": "close",
            "Volume": "volume"
        })

        return hist[["date", "ticker", "open", "high", "low", "close", "volume"]]

    except:
        return pd.DataFrame()

# =========================
# LOAD DATA
# =========================
price_data = []

for ticker in tickers.keys():
    print(f"Fetching {ticker}...")

    hist = get_history(ticker)
    price_data.append(hist)

    time.sleep(0.2)

# =========================
# COMBINE DATA
# =========================
price_df = pd.concat(price_data, ignore_index=True)

# =========================
# SAVE TO SQLITE (SAFE)
# =========================
price_df.to_sql(
    "stock_price_history",
    conn,
    if_exists="append",
    index=False,
    chunksize=500 
)

conn.commit()
conn.close()

# =========================
# EXPORT FOR POWER BI
# =========================
price_df.to_csv(
    "stock_price_history.csv",
    index=False,
    encoding="utf-8",
    sep=","
)

print("Done: price history saved!")