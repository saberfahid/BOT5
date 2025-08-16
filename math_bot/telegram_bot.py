import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
from handler import generate_math_message

load_dotenv()
TOKEN = os.getenv("MATH_TELEGRAM_BOT_TOKEN")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Received update: {update}")
    if update.message and update.message.text:
        user_text = update.message.text
        print(f"Received message: {user_text}")
        reply = generate_math_message(user_text)
        await update.message.reply_text(reply)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_message:
        await update.effective_message.reply_text("Welcome to Math Bot! Send any math question or message.")

def main():
    if not TOKEN:
        print("Error: MATH_TELEGRAM_BOT_TOKEN is missing in .env file.")
        return
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    app.add_handler(MessageHandler(filters.COMMAND & filters.Regex('^/start$'), start))
    print("Math Telegram Bot is running...")
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
from handler import generate_math_message
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("MATH_TELEGRAM_BOT_TOKEN")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Received update: {update}")
    if update.message and update.message.text:
        user_text = update.message.text
        print(f"Received message: {user_text}")
        reply = generate_math_message(user_text)
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
    from math_bot.handler import generate_math_message

    load_dotenv()
    TOKEN = os.getenv("MATH_TELEGRAM_BOT_TOKEN")

    async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
        if update.message and update.message.text:
            user_text = update.message.text
            reply = generate_math_message(user_text)
            await update.message.reply_text(reply)

    def main():
        if not TOKEN:
            print("Error: MATH_TELEGRAM_BOT_TOKEN is missing in .env file.")
            return
        app = ApplicationBuilder().token(TOKEN).build()

        async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
            if update.effective_message:
                await update.effective_message.reply_text("Welcome to Math Bot! Send any math question or message.")

        app.add_handler(MessageHandler(filters.TEXT, handle_message))
        app.add_handler(MessageHandler(filters.COMMAND & filters.Regex('^/start$'), start))
        print("Math Telegram Bot is running...")
        try:
            app.run_polling()
        except Exception as e:
            print(f"Telegram API error: {e}")

    if __name__ == "__main__":
        main()
