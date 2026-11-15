import os
from google import genai

client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

MODEL = os.getenv('GEMINI_MODEL', 'gemini-2.5-flash')

def ask_llm(message):
    response = client.models.generate_content(
        model=MODEL,
        contents=message
    )
    return response.text or ''