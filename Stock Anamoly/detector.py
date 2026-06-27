import yfinance as yf
import pandas as pd
from sklearn.ensemble import IsolationForest

def detect_anomalies(ticker, period='6mo'):
    # Fetch historical stock data
    df = yf.download(ticker, period=period, auto_adjust=True)

    if df.empty:
        return None, None
    
    df = df[['Close', 'Volume']].copy()
    df.dropna(inplace=True)

    df['Return'] = df['Close'].pct_change()
    df.dropna(inplace=True)

    features = df[['Return', 'Volume']]

    model = IsolationForest(contamination=0.05, random_state=42)
    df['Anomaly'] = model.fit_predict(features)

    anomalies = df[df['Anomaly'] == -1].copy()

    return df, anomalies