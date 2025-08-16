import sys
import os
import re
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.api import query_mistral
from core.lang_detect import get_language

def generate_math_message(user_message):
    import time
    time.sleep(1)
    lang = get_language(user_message)
    prompt = f"Reply as Math Bot: Step-by-step solutions, equations, and explanations.\nUser message: {user_message}\nReply in the user's language ({lang}). Add a nerdy, funny, attractive style."
    reply = query_mistral(prompt, language=lang)
    reply = re.sub(r'https?://\S+', '', reply)
    support_link = os.getenv("SUPPORT_LINK", "https://hellomydude.gumroad.com/coffee")
    reply += f"\n\n[Buy Me a Coffee]({support_link})"
    return reply
