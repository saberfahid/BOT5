import sys
import os
import re
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.api import query_mistral
from core.lang_detect import get_language

def generate_sigma_message(user_message):
    import time
    time.sleep(1)
    lang = get_language(user_message)
    prompt = f"Reply as Sigma Bot: Sweet, funny, motivational messages!\nUser message: {user_message}\nReply in the user's language ({lang}). Add a witty, attractive style."
    reply = query_mistral(prompt, language=lang)
    reply = re.sub(r'https?://\S+', '', reply)
    reply += "\n\n[Buy Me a Coffee](https://hellomydude.gumroad.com/coffee)"
    return reply
