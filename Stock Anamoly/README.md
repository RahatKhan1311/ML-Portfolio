# Stock Anomaly Explainer 📈

An AI-powered web app that detects unusual stock price movements and explains what likely caused them using real news headlines and a large language model.

## What It Does

- Pulls 6 months of historical stock data for any ticker (US or Indian markets)
- Detects statistically anomalous price movements using **Isolation Forest**
- Fetches relevant news headlines around each anomaly date via **NewsAPI**
- Generates a concise AI explanation of the likely cause using **Groq LLM**
- Displays everything on an interactive price chart with anomaly markers

## Tech Stack

| Layer | Technology |
|---|---|
| Anomaly Detection | Scikit-learn Isolation Forest |
| Stock Data | yfinance (Yahoo Finance) |
| News | NewsAPI |
| LLM Explanation | Groq API (GPT-OSS 20B) |
| Backend | Flask, REST API |
| Frontend | Tailwind CSS, Chart.js |

## Project Structure

```
stock-anomaly-explainer/
├── app.py              # Flask backend, API routes
├── detector.py         # Isolation Forest anomaly detection
├── news_fetcher.py     # NewsAPI integration
├── explainer.py        # Groq LLM explanation generation
├── templates/
│   └── index.html      # Frontend (Tailwind + Chart.js)
├── .env                # API keys (not committed)
└── requirements.txt
```

## How to Run

**1. Clone the repo**
```bash
git clone https://github.com/RahatKhan1311/ML-Portfolio.git
cd ML-Portfolio/Stock\ Anamoly
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Set up API keys**

Create a `.env` file:
```
GROQ_API_KEY=your_groq_key
NEWS_API_KEY=your_newsapi_key
```

Get free keys at:
- Groq: https://console.groq.com
- NewsAPI: https://newsapi.org

**4. Run the app**
```bash
python app.py
```

Open `http://127.0.0.1:5000` in your browser.

## How It Works

1. **Data Collection** — yfinance downloads daily OHLCV data for the given ticker
2. **Feature Engineering** — daily percentage return and volume are extracted as features
3. **Anomaly Detection** — Isolation Forest flags ~5% of trading days as anomalous based on unusual return/volume combinations
4. **News Fetching** — NewsAPI searches for headlines within a ±2 day window around each anomaly date
5. **LLM Explanation** — Groq receives the ticker, date, price movement, and headlines as context and generates a plain-English explanation
6. **Visualization** — Chart.js renders the full price history with anomaly points highlighted in red

## Limitations

- NewsAPI free tier covers only the last 30 days — older anomalies show no headlines
- News coverage for Indian stocks (NSE/BSE) is limited on NewsAPI
- Sentiment analysis on headlines uses keyword matching, not a trained model

## Example Tickers

- US: `AAPL`, `TSLA`, `NVDA`, `MSFT`
- India: `RELIANCE.NS`, `TCS.NS`, `INFY.NS`