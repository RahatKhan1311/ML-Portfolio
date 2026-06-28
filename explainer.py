import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv('GROQ_API_KEY'))

def explain_anomaly(ticker, date, price_return, headlines):
    headlines_text = "\n".join(headlines) if headlines else "No relevant news found."

    prompt = f"""
You are a financial analyst. A stock anomaly was detected for {ticker} on {date}.

Price movement: {price_return:.2%}
News headlines around that date:
{headlines_text}

In 3-4 sentences, explain what likely caused this anomaly based on the price movement and news context. 
Be concise and specific. If no relevant news is available, suggest possible general market reasons.
"""
    
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages = [{"role":"user","content":prompt}],
        max_tokens=500
    )

    return response.choices[0].message.content.strip()