from newsapi import NewsApiClient
from datetime import timedelta
import os
from dotenv import load_dotenv

load_dotenv()

def get_news(ticker, dates):
    api = NewsApiClient(api_key=os.getenv('NEWS_API_KEY'))

    results = {}

    for date in dates:
        from_date = (date - timedelta(days=2)).strftime('%Y-%m-%d')
        to_date = (date + timedelta(days=2)).strftime('%Y-%m-%d')

        try:
            response = api.get_everything(
                q=ticker,
                from_param=from_date,
                to=to_date,
                language='en',
                sort_by='relevancy',
                page_size=3
            )

            headlines = [article['title'] for article in response['articles']]
            results[str(date.date())] = headlines if headlines else ["No relevant news found."]

        except Exception as e:
            results[str(date.date())] = ["Error fetching news"]
    
    return results