import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Setup logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# YOUR CHANNEL LINK
CHANNEL_LINK = "https://t.me/+QvCFEopP3r9hY2Q0"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Respond with channel link when /start is used"""
    user = update.effective_user
    await update.message.reply_text(
        f"Welcome {user.first_name}! 👋\n\n"
        f"Join our channel:\n{CHANNEL_LINK}\n\n"
        f"Click the link above to join! 🔗"
    )

def main():
    """Start the bot"""
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    
    if not token:
        logger.error("No token found! Set TELEGRAM_BOT_TOKEN environment variable.")
        return
    
    # Create and run bot
    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    
    logger.info("Bot is running...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
