from langdetect import detect

def get_language(text):
    try:
        lang = detect(text)
        # If langdetect returns a non-English language for a message with mostly English letters, override to 'en'
        english_letters = sum(c.isalpha() and c.lower() in "abcdefghijklmnopqrstuvwxyz" for c in text)
        total_letters = sum(c.isalpha() for c in text)
        if lang != "en" and total_letters > 0 and english_letters / total_letters > 0.7:
            return "en"
        return lang
    except Exception:
        return "en"
