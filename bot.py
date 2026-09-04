import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# YOUR CHANNEL LINK
CHANNEL_LINK = "https://t.me/+QvCFEopP3r9hY2Q0"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler for /start command"""
    try:
        user = update.effective_user
        
        # Create clickable button
        keyboard = [
            [InlineKeyboardButton("🔗 JOIN CHANNEL NOW", url=CHANNEL_LINK)]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        # Send message with button
        await update.message.reply_text(
            f"👋 Welcome {user.first_name}!\n\n"
            f"📢 Click the button below to join our Telegram channel:",
            reply_markup=reply_markup
        )
        logger.info(f"User {user.first_name} (ID: {user.id}) started the bot")
    except Exception as e:
        logger.error(f"Error in start handler: {e}")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler for /help command"""
    try:
        await update.message.reply_text(
            "🤖 This bot shares our Telegram channel link.\n\n"
            "Simply use /start to get the join link!"
        )
    except Exception as e:
        logger.error(f"Error in help handler: {e}")

def main():
    """Start the bot"""
    # Get token from environment variable
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    
    if not token:
        logger.error("❌ TELEGRAM_BOT_TOKEN not found! Please set it in Railway variables.")
        return
    
    try:
        # Create bot application
        app = Application.builder().token(token).build()
        
        # Add command handlers
        app.add_handler(CommandHandler("start", start))
        app.add_handler(CommandHandler("help", help_command))
        
        # Log bot info
        logger.info("✅ Bot is starting...")
        logger.info(f"🤖 Bot token: {token[:10]}... (hidden for security)")
        
        # Start the bot with error handling
        logger.info("🔄 Bot is polling for updates...")
        app.run_polling(allowed_updates=Update.ALL_TYPES)
        
    except Exception as e:
        logger.error(f"❌ Error starting bot: {e}")

if __name__ == '__main__':
    logger.info("🚀 Bot application started")
    main()
