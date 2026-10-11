from newsapi import NewsApiClient
from datetime import timedelta, date as date_cls
import os
from dotenv import load_dotenv

load_dotenv()

FREE_PLAN_DAYS = 29   # NewsAPI free plan only serves roughly the last 30 days

def get_news(ticker, dates):
    api = NewsApiClient(api_key=os.getenv('NEWS_API_KEY'))
    results = {}
    cutoff = date_cls.today() - timedelta(days=FREE_PLAN_DAYS)

    for date in dates:
        key = str(date.date())

        # Too old for the free plan: skip the API call (saves your daily quota)
        if date.date() - timedelta(days=2) < cutoff:
            results[key] = []
            continue

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
            results[key] = [a['title'] for a in response['articles']]
        except Exception as e:
            print("NewsAPI error:", repr(e))
            results[key] = ["Error fetching news"]   # per date, so one failure doesn't stop the rest

    return results