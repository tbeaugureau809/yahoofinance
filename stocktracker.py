import pandas as pd
import numpy as np
import yfinance as yf
import psycopg2

conn = psycopg2.connect(
    dbname="stocktrackerdb",
    user="postgres",
    password="password",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

cur.execute("SELECT ticker FROM watchlist;")
tickers = [row[0] for row in cur.fetchall()]

for t in tickers:
    stock = yf.Ticker(t)
    print(t, stock.info.get("longName"),  stock.info.get("currentPrice"))

