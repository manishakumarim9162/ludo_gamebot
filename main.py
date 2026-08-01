import os
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# .env file se variables load karein
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
GAME_WEBAPP_URL = os.getenv("GAME_WEBAPP_URL")

if not BOT_TOKEN or not GAME_WEBAPP_URL:
    raise ValueError("Error: BOT_TOKEN ya GAME_WEBAPP_URL .env file me nahi mila!")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Personal ya Group me /start ya /ludo chalne par reaction"""
    
    # 1. Check karein ki message Group me aaya hai ya Personal chat me
    chat_type = update.effective_chat.type
    
    if chat_type in ["group", "supergroup"]:
        # GROUP KE LIYE SOLUTION: Direct URL link button banayein
        keyboard = [
            [
                InlineKeyboardButton(
                    text="🎮 Play Ludo In Group", 
                    url=GAME_WEBAPP_URL  # Group me direct 'url' kaam karega, 'web_app' nahi
                )
            ]
        ]
        text_msg = "🎲 *Ludo Game Group Me Active Hai!* \n\nNiche diye gaye button par click karke browser ya overlay me kheleing."
    else:
        # PERSONAL CHAT KE LIYE: Direct interface open hoga
        from telegram import WebAppInfo
        keyboard = [
            [
                InlineKeyboardButton(
                    text="🎮 Open Graphical Ludo", 
                    web_app=WebAppInfo(url=GAME_WEBAPP_URL)
                )
            ]
        ]
        text_msg = "🎲 *Welcome to Ludo Bot!* \n\nButton par click karke apna game start karein."

    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        text=text_msg,
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

def main():
    # Bot application initialize karein
    application = Application.builder().token(BOT_TOKEN).build()

    # Dono commands ko same function par map karein taaki group me /ludo bhi kaam kare
    application.add_handler(CommandHandler("ludo", start))
    application.add_handler(CommandHandler("start", start))

    # Bot ko start karein
    print("Telegram Bot successfully chal raha hai...")
    application.run_polling()

if __name__ == "__main__":
    main()
    
