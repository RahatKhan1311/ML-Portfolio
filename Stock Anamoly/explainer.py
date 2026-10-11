import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv('GROQ_API_KEY'))

NO_NEWS_MESSAGE = ("No news headlines were available for this date, so a cause cannot "
                   "be determined from the data. The day was flagged because of an unusual "
                   "combination of price return and trading volume.")

def explain_anomaly(ticker, date, price_return, headlines, volume_ratio=None):
    if not headlines:
        return NO_NEWS_MESSAGE          # no LLM call, no guessing

    headlines_text = "\n".join(f"- {h}" for h in headlines)
    volume_text = (f"Trading volume was {volume_ratio:.1f}x the 6-month median."
                   if volume_ratio else "")

    prompt = f"""
A stock anomaly was detected for {ticker} on {date}.
Price movement: {price_return:.2%}. {volume_text}

Headlines from within 2 days of that date:
{headlines_text}

Rules:
- Use ONLY the headlines above. Do not use outside knowledge and do not speculate
  about earnings, policy or the wider market.
- If a headline plausibly explains the move, name it and explain in 2-3 sentences.
- If none clearly explains it, reply exactly: "The headlines do not clearly explain this move."
- A headline near the date shows correlation, not proven cause.
"""
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1500,
        temperature=0.2,
    )
    choice = response.choices[0]
    text = choice.message.content.strip()
    if choice.finish_reason == "length":
        text += " ..."
    return text