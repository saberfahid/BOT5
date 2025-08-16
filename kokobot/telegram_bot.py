import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
from handler import generate_koko_message

load_dotenv()
TOKEN = os.getenv("KOKO_TELEGRAM_BOT_TOKEN")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Received update: {update}")
    if update.message and update.message.text:
        user_text = update.message.text
        print(f"Received message: {user_text}")
        reply = generate_koko_message(user_text)
        await update.message.reply_text(reply)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_message:
        await update.effective_message.reply_text("Welcome to KokoBot! Send any message for grammar help.")

def main():
    if not TOKEN:
        print("Error: KOKO_TELEGRAM_BOT_TOKEN is missing in .env file.")
        return
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    app.add_handler(MessageHandler(filters.COMMAND & filters.Regex('^/start$'), start))
    print("Koko Telegram Bot is running...")
    try:
        app.run_polling()
    except Exception as e:
        print(f"Telegram API error: {e}")

if __name__ == "__main__":
    main()
import os
import sys
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from handler import generate_koko_message
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("KOKO_TELEGRAM_BOT_TOKEN")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Received update: {update}")
    if update.message and update.message.text:
        user_text = update.message.text
        print(f"Received message: {user_text}")
        reply = generate_koko_message(user_text)
        await update.message.reply_text(reply)

def main():
    import os
    import sys
    sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
    sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
    from telegram import Update
    from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
    from dotenv import load_dotenv
    from kokobot.handler import generate_koko_message

    load_dotenv()
    TOKEN = os.getenv("KOKO_TELEGRAM_BOT_TOKEN")

    async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
        if update.message and update.message.text:
            user_text = update.message.text
            reply = generate_koko_message(user_text)
            await update.message.reply_text(reply)

    def main():
        if not TOKEN:
            print("Error: KOKO_TELEGRAM_BOT_TOKEN is missing in .env file.")
            return
        app = ApplicationBuilder().token(TOKEN).build()

        async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
            if update.effective_message:
                await update.effective_message.reply_text("Welcome to KokoBot! Send any message for grammar help.")

        app.add_handler(MessageHandler(filters.TEXT, handle_message))
        app.add_handler(MessageHandler(filters.COMMAND & filters.Regex('^/start$'), start))
        print("Koko Telegram Bot is running...")
        try:
            app.run_polling()
        except Exception as e:
            print(f"Telegram API error: {e}")

    if __name__ == "__main__":
        main()
