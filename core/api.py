import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

MISTRAL_MODEL = "mistral-medium"
OPENROUTER_MODEL = "gpt-3.5-turbo"
GROQ_MODEL = "gpt-3.5-turbo"

def query_mistral(prompt, language="en"):
    # 1. Try Mistral Direct API first
    mistral_url = os.getenv("MISTRAL_API_URL", "https://api.mistral.ai/v1/chat/completions")
    mistral_key = os.getenv("MISTRAL_API_KEY")
    mistral_headers = {
        "Authorization": f"Bearer {mistral_key}",
        "Content-Type": "application/json"
    }
    mistral_data = {
        "model": MISTRAL_MODEL,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
    try:
        response = requests.post(mistral_url, json=mistral_data, headers=mistral_headers, timeout=15)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        # 2. Fallback to OpenRouter
        openrouter_url = "https://openrouter.ai/api/v1/chat/completions"
        openrouter_key = os.getenv("OPENROUTER_API_KEY")
        openrouter_headers = {
            "Authorization": f"Bearer {openrouter_key}",
            "Content-Type": "application/json"
        }
        openrouter_data = {
            "model": OPENROUTER_MODEL,
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }
        try:
            response = requests.post(openrouter_url, json=openrouter_data, headers=openrouter_headers, timeout=15)
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"]
        except Exception as e2:
            # 3. Fallback to Groq
            groq_url = "https://api.groq.com/openai/v1/chat/completions"
            groq_key = os.getenv("GROQ_API_KEY")
            groq_headers = {
                "Authorization": f"Bearer {groq_key}",
                "Content-Type": "application/json"
            }
            groq_data = {
                "model": GROQ_MODEL,
                "messages": [
                    {"role": "user", "content": prompt}
                ]
            }
            try:
                response = requests.post(groq_url, json=groq_data, headers=groq_headers, timeout=15)
                response.raise_for_status()
                return response.json()["choices"][0]["message"]["content"]
            except Exception as e3:
                return f"[Error] All providers failed: Mistral Direct: {e} | OpenRouter: {e2} | Groq: {e3}"
