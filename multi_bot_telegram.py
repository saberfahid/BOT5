import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from sigma_bot.handler import generate_sigma_message
from math_bot.handler import generate_math_message
from fitness_bot.handler import generate_fitness_message
from travel_bot.handler import generate_travel_message
from kokobot.handler import generate_koko_message
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("SIGMA_TELEGRAM_BOT_TOKEN")  # Use one main bot token


SUPPORT_LINK = os.getenv("SUPPORT_LINK", "https://hellomydude.gumroad.com/coffee")
SUPPORT_MESSAGE = f"[Buy Me a Coffee]({SUPPORT_LINK})"

BOT_MENU = (
    "Choose a bot by typing its name or number:\n"
    "1. Sigma\n2. Math\n3. Fitness\n4. Travel\n5. Koko\n"
    "Or just type your message and I’ll auto-detect!" + "\n" + SUPPORT_MESSAGE
)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text:
        user_text = update.message.text.strip()
        text_lower = user_text.lower()
        # Simple intent detection
        if text_lower.startswith("1") or "sigma" in text_lower:
            reply = generate_sigma_message(user_text) + "\n" + SUPPORT_MESSAGE
        elif text_lower.startswith("2") or "math" in text_lower:
            reply = generate_math_message(user_text) + "\n" + SUPPORT_MESSAGE
        elif text_lower.startswith("3") or "fitness" in text_lower:
            reply = generate_fitness_message(user_text) + "\n" + SUPPORT_MESSAGE
        elif text_lower.startswith("4") or "travel" in text_lower:
            reply = generate_travel_message(user_text) + "\n" + SUPPORT_MESSAGE
        elif text_lower.startswith("5") or "koko" in text_lower:
            reply = generate_koko_message(user_text) + "\n" + SUPPORT_MESSAGE
        else:
            reply = BOT_MENU
        await update.message.reply_text(reply)

def main():
    if not TOKEN:
        print("Error: SIGMA_TELEGRAM_BOT_TOKEN is missing in .env file.")
        return
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Multi-Bot Telegram is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
