import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKENS = {
    'kokobot': os.getenv('KOKO_TELEGRAM_BOT_TOKEN'),
    'gymbot': os.getenv('GYM_TELEGRAM_BOT_TOKEN'),
    'mathbot': os.getenv('MATH_TELEGRAM_BOT_TOKEN'),
    'sigmabot': os.getenv('SIGMA_TELEGRAM_BOT_TOKEN'),
    'travelbot': os.getenv('TRAVEL_TELEGRAM_BOT_TOKEN'),
}

def test_bot(token, name):
    url = f'https://api.telegram.org/bot{token}/getMe'
    try:
        resp = requests.get(url, timeout=10)
        data = resp.json()
        if data.get('ok'):
            print(f'{name}: OK - {data["result"]["username"]}')
        else:
            print(f'{name}: ERROR - {data}')
    except Exception as e:
        print(f'{name}: Exception - {e}')

for name, token in TOKENS.items():
    if token:
        test_bot(token, name)
    else:
        print(f'{name}: No token found in .env')
