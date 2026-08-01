import os
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

# .env file se variables load karein
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
GAME_WEBAPP_URL = os.getenv("GAME_WEBAPP_URL")

if not BOT_TOKEN or not GAME_WEBAPP_URL:
    raise ValueError("Error: BOT_TOKEN ya GAME_WEBAPP_URL .env file me nahi mila!")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Group me /ludo command aane par graphical game button bhejega"""
    keyboard = [
        [
            InlineKeyboardButton(
                text="🎮 Play Graphical Ludo", 
                web_app=WebAppInfo(url=GAME_WEBAPP_URL)
            )
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        text="🎲 *Ludo Game Group Me Active Hai!* \n\nNiche diye gaye button par click karke graphics ke sath game kheleing.",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

def main():
    # Bot application initialize karein
    application = Application.builder().token(BOT_TOKEN).build()

    # Commands register karein
    application.add_handler(CommandHandler("ludo", start))
    application.add_handler(CommandHandler("start", start))

    # Bot ko start karein
    print("Telegram Bot successfully chal raha hai...")
    application.run_polling()

if __name__ == "__main__":
    main()
  
