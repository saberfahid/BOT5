import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
from handler import generate_fitness_message

load_dotenv()
TOKEN = os.getenv("GYM_TELEGRAM_BOT_TOKEN")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Received update: {update}")
    if update.message and update.message.text:
        user_text = update.message.text
        print(f"Received message: {user_text}")
        reply = generate_fitness_message(user_text)
        await update.message.reply_text(reply)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_message:
        await update.effective_message.reply_text("Welcome to Fitness Bot! Send any message for workout tips.")

def main():
    if not TOKEN:
        print("Error: GYM_TELEGRAM_BOT_TOKEN is missing in .env file.")
        return
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    app.add_handler(MessageHandler(filters.COMMAND & filters.Regex('^/start$'), start))
    print("Fitness Telegram Bot is running...")
    try:
        app.run_polling()
    except Exception as e:
        print(f"Telegram API error: {e}")

if __name__ == "__main__":
    main()
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
import sys
from handler import generate_fitness_message
from dotenv import load_dotenv

load_dotenv()

from telegram import Update
from telegram.ext import ContextTypes
TOKEN = os.getenv("GYM_TELEGRAM_BOT_TOKEN")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Received update: {update}")
    if update.message and update.message.text:
        user_text = update.message.text
        print(f"Received message: {user_text}")
        reply = generate_fitness_message(user_text)
        await update.message.reply_text(reply)

def main():
    import os
    import sys
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
    from telegram import Update
    from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
    from dotenv import load_dotenv
    from fitness_bot.handler import generate_fitness_message

    load_dotenv()
    TOKEN = os.getenv("GYM_TELEGRAM_BOT_TOKEN")

    async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
        if update.message and update.message.text:
            user_text = update.message.text
            reply = generate_fitness_message(user_text)
            await update.message.reply_text(reply)

    def main():
        if not TOKEN:
            print("Error: GYM_TELEGRAM_BOT_TOKEN is missing in .env file.")
            return
        app = ApplicationBuilder().token(TOKEN).build()

        async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
            if update.effective_message:
                await update.effective_message.reply_text("Welcome to Fitness Bot! Send any message for workout tips.")

        app.add_handler(MessageHandler(filters.TEXT, handle_message))
        app.add_handler(MessageHandler(filters.COMMAND & filters.Regex('^/start$'), start))
        print("Fitness Telegram Bot is running...")
        try:
            app.run_polling()
        except Exception as e:
            print(f"Telegram API error: {e}")

    if __name__ == "__main__":
        main()
