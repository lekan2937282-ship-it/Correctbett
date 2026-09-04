import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# Your channel link
CHANNEL_LINK = "https://t.me/+QvCFEopP3r9hY2Q0"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send welcome message with join button when /start is used"""
    # Create the inline button
    keyboard = [
        [InlineKeyboardButton("🔐 VERIFICĂ ȘI INTRĂ ÎN CORECTBET", url=CHANNEL_LINK)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Send welcome message with button
    await update.message.reply_text(
        "👋 **Bine ai venit în CorectBet!**\n\n"
        "De peste **7 ani construim și dezvoltăm această comunitate**, iar unul dintre lucrurile la care am ținut întotdeauna este **calitatea membrilor**, nu doar numărul lor.\n\n"
        "🛡️ Din acest motiv, accesul se realizează prin intermediul botului oficial CorectBet.\n\n"
        "Nu acceptăm **boți, conturi fake sau membri generați artificial**. Ne dorim o comunitate formată din **persoane reale și active**, interesate de conținutul pe care îl oferim.\n\n"
        "Această verificare ne ajută să păstrăm grupul curat și standardele pe care le-am construit în toți acești ani.\n\n"
        "✅ **Ești o persoană reală? Continuă mai jos pentru acces.**",
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

def main():
    """Start the bot"""
    # Get token from environment variable
    token = os.environ.get("BOT_TOKEN")
    
    if not token:
        print("ERROR: BOT_TOKEN environment variable not set!")
        return
    
    # Create the Application
    app = Application.builder().token(token).build()
    
    # Add command handler for /start
    app.add_handler(CommandHandler("start", start))
    
    # Start the bot
    print("Bot is running successfully!")
    app.run_polling()

if __name__ == "__main__":
    main()
