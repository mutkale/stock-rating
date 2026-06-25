import yfinance as yf
import pandas as pd
import numpy as np
import sqlite3
import time
from datetime import datetime

from tickers import tickers

# =========================
# 1. DATABASE SETUP
# =========================

conn = sqlite3.connect("omxh_quant.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS stock_scores_latest (
    ticker TEXT PRIMARY KEY,
    company TEXT,
    sector TEXT,
    pe REAL,
    roe REAL,
    dividend REAL,
    debt REAL,
    score REAL,
    rating REAL,
    signal TEXT,
    signal_sort INTEGER
)
""")

conn.commit()

# =========================
# 2. SIGNAL ORDER
# =========================

signal_order = {
    "Strong Buy": 1,
    "Buy": 2,
    "Hold": 3,
    "Weak": 4,
    "Avoid": 5
}

# =========================
# 3. FETCH DATA
# =========================

def get_data(ticker):
    try:
        stock = yf.Ticker(ticker)
        info = stock.info

        return {
            "Ticker": ticker,
            "P/E": info.get("trailingPE"),
            "ROE": info.get("returnOnEquity"),
            "DividendYield": info.get("dividendYield"),
            "DebtToEquity": info.get("debtToEquity"),
        }
    except:
        return {
            "Ticker": ticker,
            "P/E": None,
            "ROE": None,
            "DividendYield": None,
            "DebtToEquity": None,
        }

# =========================
# 4. COLLECT DATA
# =========================

data = []

for ticker, meta in tickers.items():
    row = get_data(ticker)

    row["Company"] = meta["name"]
    row["Sector"] = meta["sector"]

    data.append(row)
    time.sleep(0.2)

df = pd.DataFrame(data)

# =========================
# 5. CLEAN DATA
# =========================

for col in ["P/E", "ROE", "DividendYield", "DebtToEquity"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df = df.replace([np.inf, -np.inf], np.nan)

df["DividendYield"] = df["DividendYield"].fillna(0)
df["DebtToEquity"] = df["DebtToEquity"].fillna(df["DebtToEquity"].median())
df["ROE"] = df["ROE"].fillna(df["ROE"].median())

# =========================
# 6. HANDLE P/E
# =========================

max_pe = df["P/E"].dropna().max()
df["P/E_adj"] = df["P/E"]

df.loc[
    (df["P/E_adj"].isna()) |
    (df["P/E_adj"] <= 0),
    "P/E_adj"
] = max_pe * 2

# =========================
# 7. WINSORIZATION
# =========================

def winsor(s):
    return s.clip(
        lower=s.quantile(0.05),
        upper=s.quantile(0.95)
    )

df["ROE"] = winsor(df["ROE"])
df["P/E_adj"] = winsor(df["P/E_adj"])
df["DividendYield"] = winsor(df["DividendYield"])
df["DebtToEquity"] = winsor(df["DebtToEquity"])

# =========================
# 8. SCORES
# =========================

df["ROE_score"] = df["ROE"].rank(pct=True)
df["PE_score"] = 1 - df["P/E_adj"].rank(pct=True)
df["Div_score"] = df["DividendYield"].rank(pct=True)
df["Debt_score"] = 1 - df["DebtToEquity"].rank(pct=True)

df["Score"] = (
    0.40 * df["ROE_score"] +
    0.30 * df["PE_score"] +
    0.15 * df["Div_score"] +
    0.15 * df["Debt_score"]
)

df["Rating"] = (df["Score"] * 100).round(1)

# =========================
# 9. SIGNALS
# =========================

def signal(x):
    if x >= 80:
        return "Strong Buy"
    elif x >= 60:
        return "Buy"
    elif x >= 40:
        return "Hold"
    elif x >= 20:
        return "Weak"
    return "Avoid"

df["Signal"] = df["Rating"].apply(signal)
df["SignalSort"] = df["Signal"].map(signal_order)

# =========================
# 10. FINAL STRUCTURE
# =========================

df = df[[
    "Ticker",
    "Company",
    "Sector",
    "P/E",
    "ROE",
    "DividendYield",
    "DebtToEquity",
    "Score",
    "Rating",
    "Signal",
    "SignalSort"
]]

# =========================
# 11. SAVE TO SQLITE (LATEST ONLY)
# =========================

for _, row in df.iterrows():

    cursor.execute("""
    INSERT INTO stock_scores_latest (
        ticker, company, sector,
        pe, roe, dividend, debt,
        score, rating, signal, signal_sort
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ON CONFLICT(ticker) DO UPDATE SET
        company=excluded.company,
        sector=excluded.sector,
        pe=excluded.pe,
        roe=excluded.roe,
        dividend=excluded.dividend,
        debt=excluded.debt,
        score=excluded.score,
        rating=excluded.rating,
        signal=excluded.signal,
        signal_sort=excluded.signal_sort
    """, (
        row["Ticker"],
        row["Company"],
        row["Sector"],
        row["P/E"],
        row["ROE"],
        row["DividendYield"],
        row["DebtToEquity"],
        row["Score"],
        row["Rating"],
        row["Signal"],
        row["SignalSort"]
    ))

conn.commit()

# =========================
# 12. EXPORT FOR POWER BI
# =========================

df.to_csv(
    "powerbi_latest.csv",
    index=False,
    encoding="utf-8",
    sep=","
)

conn.close()

# =========================
# 13. OUTPUT
# =========================

print(
    df[["Ticker", "Company", "Sector", "Rating", "Signal", "SignalSort"]]
    .sort_values("Rating", ascending=False)
)