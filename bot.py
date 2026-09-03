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

# YOUR CHANNEL LINK - Edit this if needed
CHANNEL_LINK = "https://t.me/+QvCFEopP3r9hY2Q0"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler for /start command"""
    user = update.effective_user
    
    # Create clickable button
    keyboard = [
        [InlineKeyboardButton("🔗 JOIN CHANNEL NOW", url=CHANNEL_LINK)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Send message with button
    await update.message.reply_text(
        f"👋 Welcome {user.first_name}!\n\n"
        f"📢 Click the button below to join our Telegram channel:\n",
        reply_markup=reply_markup
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler for /help command"""
    await update.message.reply_text(
        "🤖 This bot shares our Telegram channel link.\n\n"
        "Simply use /start to get the join link!",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("🔗 Join Channel", url=CHANNEL_LINK)]
        ])
    )

async def channel_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler for /channel command"""
    await update.message.reply_text(
        f"📢 Our Channel:\n{CHANNEL_LINK}",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("🔗 Click to Join", url=CHANNEL_LINK)]
        ])
    )

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
        app.add_handler(CommandHandler("channel", channel_command))
        
        # Start the bot
        logger.info("✅ Bot is running successfully!")
        logger.info("🤖 Bot username: @" + app.bot.username if hasattr(app.bot, 'username') else "Unknown")
        
        app.run_polling(allowed_updates=Update.ALL_TYPES)
        
    except Exception as e:
        logger.error(f"❌ Error starting bot: {e}")

if __name__ == '__main__':
    main()
