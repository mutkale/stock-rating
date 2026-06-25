# Stock Rating System

A quantitative stock rating system for Finnish equities (OMXH).  
The system automatically fetches financial data, builds a scoring model, and ranks stocks into actionable investment signals.

- The system will:
    - Fetch financial data from Yahoo Finance (yfinance)
    - Read tickers and metadata from tickers.py
    - Calculate fundamental metrics:
        - P/E ratio
        - ROE (Return on Equity)
        - Dividend yield
        - Debt-to-equity
    - Build a weighted scoring model
    - Generate:
        - Stock Score
        - Rating (0–100)
        - Signal (Strong Buy → Avoid)
    - Store results into a local SQLite database
    - Export CSV files for Power BI analysis

## Project Structure

| File | Description |
|------|-------------|
| `getStocks.py` | Main data collection and stock scoring engine |
| `tickers.py` | Stock universe, company names, and sector metadata |
| `omxh_quant.db` | SQLite database containing historical and latest ratings |
| `powerbi_latest.csv` | Latest stock rankings export for Power BI |
| `powerbi_history_export.csv` | Historical dataset export for trend analysis |
| `README.md` | Project documentation and usage instructions |

## Output files

### SQLite database
- stock_scores_history → full historical data
- stock_scores_latest → latest snapshot

### CSV exports
- powerbi_latest.csv → latest rankings (Power BI ready)
- powerbi_history_export.csv → full historical dataset

---
# Disclaimer

This project is for analytical purposes only.

---

# How to use

## 1. Install dependencies

Make sure you have python installed

```bash
pip install yfinance pandas numpy
```

## 2. Run the program 

```bash
python getStocks.py
```

## Refresh Data in Power BI

After running `getStocks.py`, open the Power BI report and select **Refresh** to import the latest generated data and update all visualizations.


