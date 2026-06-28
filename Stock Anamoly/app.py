from flask import Flask, render_template, request, jsonify
from detector import detect_anomalies
from news_fetcher import get_news
from explainer import explain_anomaly

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    ticker = request.json.get('ticker', '').upper().strip()
    
    if not ticker:
        return jsonify({'error': 'Please enter a ticker symbol'}), 400
    
    df, anomalies = detect_anomalies(ticker)
    
    if df is None:
        return jsonify({'error': f'Could not fetch data for {ticker}. Check the ticker symbol.'}), 400
    
    if anomalies.empty:
        return jsonify({'error': 'No anomalies detected for this ticker'}), 400
    
    # Build chart data
    anomaly_dates_set = set(anomalies.index)
    close_prices = df['Close'].squeeze()
    chart_labels = [str(d.date()) for d in df.index]
    chart_prices = [round(float(close_prices.iloc[i]), 2) for i in range(len(df))]
    anomaly_indices = [i for i, d in enumerate(df.index) if d in anomaly_dates_set]
    
    results = []
    anomaly_dates = anomalies.index.tolist()
    news_data = get_news(ticker, anomaly_dates) # Calls news_fetcher.py once for all anomaly dates at once — more efficient than calling per anomaly.
    
    for date, row in anomalies.iterrows():
        date_str = str(date.date())
        headlines = news_data.get(date_str, ["No news found"])
        price_return = float(row['Return'].iloc[0] if hasattr(row['Return'], 'iloc') else row['Return'])
        explanation = explain_anomaly(ticker, date_str, price_return, headlines)
        results.append({
            'date': date_str,
            'return': f"{price_return:.2%}",
            'headlines': headlines,
            'explanation': explanation
        })
    
    return jsonify({
        'ticker': ticker,
        'anomalies': results,
        'chart': {
            'labels': chart_labels,
            'prices': chart_prices,
            'anomalyIndices': anomaly_indices
        }
    })

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)