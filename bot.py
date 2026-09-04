import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# Your channel link
CHANNEL_LINK = "https://t.me/+QvCFEopP3r9hY2Q0"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send ONLY the channel link when /start is used"""
    # Create the inline button - this is the ONLY way to open a link
    keyboard = [
        [InlineKeyboardButton("🔐 Intră în CorectBet", url=CHANNEL_LINK)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Minimal message - just the button
    await update.message.reply_text(
        "🔐 Click butonul pentru a intra în CorectBet:",
        reply_markup=reply_markup
    )

def main():
    """Start the bot"""
    token = os.environ.get("BOT_TOKEN")
    
    if not token:
        print("ERROR: BOT_TOKEN environment variable not set!")
        return
    
    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    
    print("Bot is running successfully!")
    app.run_polling()

if __name__ == "__main__":
    main()
