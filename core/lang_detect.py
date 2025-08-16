from langdetect import detect

def get_language(text):
    try:
        return detect(text)
    except Exception:
        return "en"
