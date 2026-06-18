import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

async def analyze_news(title, content):
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = f"Summarize this news: {title}\n{content[:1000]} in 3 lines."
    response = model.generate_content(prompt)
    return response.text
    