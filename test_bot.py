import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler

# Your channel link
CHANNEL_LINK = "https://t.me/+QvCFEopP3r9hY2Q0"

async def start(update, context):
    keyboard = [[InlineKeyboardButton("🔗 Join Channel", url=CHANNEL_LINK)]]
    await update.message.reply_text(
        "Welcome! Click below to join our channel:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

# Get token from environment
token = os.environ.get("TELEGRAM_BOT_TOKEN")

if not token:
    print("❌ ERROR: TELEGRAM_BOT_TOKEN not found!")
    print("Please set it using: export TELEGRAM_BOT_TOKEN='your_token_here'")
    exit(1)

print(f"✅ Token found: {token[:10]}...")
print("🚀 Starting bot...")

try:
    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    print("✅ Bot is running! Send /start to your bot on Telegram")
    app.run_polling()
except Exception as e:
    print(f"❌ ERROR: {e}")
