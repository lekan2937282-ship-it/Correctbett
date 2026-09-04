import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import Application, CommandHandler, ContextTypes

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Configuration
CHANNEL_LINK = "https://t.me/+QvCFEopP3r9hY2Q0"
IMAGE_PATH = "assets/corectbet.jpg"

# Welcome message (exactly as provided)
WELCOME_MESSAGE = (
    "👋 **Bine ai venit în CorectBet!**\n\n"
    "De peste **7 ani construim și dezvoltăm această comunitate**, iar unul dintre lucrurile la care am ținut întotdeauna este **calitatea membrilor**, nu doar numărul lor.\n\n"
    "🛡️ Din acest motiv, accesul se realizează prin intermediul botului oficial CorectBet.\n\n"
    "Nu acceptăm **boți, conturi fake sau membri generați artificial**. Ne dorim o comunitate formată din **persoane reale și active**, interesate de conținutul pe care îl oferim.\n\n"
    "Această verificare ne ajută să păstrăm grupul curat și standardele pe care le-am construit în toți acești ani.\n\n"
    "✅ **Ești o persoană reală? Continuă mai jos pentru acces.**"
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send welcome message with image and join button"""
    try:
        user = update.effective_user
        
        # Create the channel access button
        keyboard = [
            [InlineKeyboardButton("🔐 VERIFICĂ ȘI INTRĂ ÎN CORECTBET", url=CHANNEL_LINK)]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        # Check if image exists
        if os.path.exists(IMAGE_PATH):
            # Send image with caption and button
            with open(IMAGE_PATH, 'rb') as photo:
                await update.message.reply_photo(
                    photo=photo,
                    caption=WELCOME_MESSAGE,
                    reply_markup=reply_markup,
                    parse_mode='Markdown'
                )
            logger.info(f"Sent welcome with image to user {user.id}")
        else:
            # Fallback: send text only if image not found
            await update.message.reply_text(
                WELCOME_MESSAGE,
                reply_markup=reply_markup,
                parse_mode='Markdown'
            )
            logger.warning(f"Image not found at {IMAGE_PATH}, sent text only")
            
    except Exception as e:
        logger.error(f"Error in start handler: {e}")
        await update.message.reply_text(
            "⚠️ A apărut o eroare. Te rugăm să încerci din nou.",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔐 Intră în CorectBet", url=CHANNEL_LINK)]
            ])
        )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Help command handler"""
    await update.message.reply_text(
        "🤖 **CorectBet Bot**\n\n"
        "Apasă /start pentru a accesa CorectBet.\n"
        "Dacă întâmpini probleme, contactează suportul.",
        parse_mode='Markdown'
    )

def main():
    """Start the bot"""
    # Get token from environment variable
    token = os.environ.get("BOT_TOKEN")
    
    if not token:
        logger.error("❌ BOT_TOKEN environment variable not set!")
        return
    
    try:
        # Create the Application
        app = Application.builder().token(token).build()
        
        # Add command handlers
        app.add_handler(CommandHandler("start", start))
        app.add_handler(CommandHandler("help", help_command))
        
        # Start the bot
        logger.info("✅ CorectBet Bot is running successfully!")
        app.run_polling()
        
    except Exception as e:
        logger.error(f"❌ Error starting bot: {e}")

if __name__ == "__main__":
    main()
