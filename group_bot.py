import os
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)

# ----------------- LOGGING -----------------
logging.basicConfig(level=logging.INFO)

# ----------------- LOAD ENV -----------------
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
GROUP_ID = int(os.getenv("GROUP_ID"))

# ----------------- MESSAGES -----------------
Message1 = """✅️P2P U HOME ACCEPTED
WE ARE A GAMING COMPANY ALSO ACCEPT P2P DEALS WE HAVE LOT OF INR AND NEED USDT.💰
Gaming & stock fund ₹98 - 107
Upfront USDT:-
1. Mix funds 122INR
2. Stock funds 116INR
3. Game funds 110INR
SUPPORTS IMPS, & BANK CARD
✅️DM ME @FPAY9
✅️JOIN OUR GROUP @uhome_buy_sell
"""

CUSTOM_MESSAGE = """🌟WE NEED USDT🌟 
✅️U-HOME P2P ACCEPTED
WE HAVE LOT OF INR AND NEED USDT 💰
✅️DM ME @FPAY9
✅️JOIN OUR GROUP @uhome_buy_sell
"""

# ----------------- COMMAND ONLY (SAFE) -----------------
async def rates(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.chat.id != GROUP_ID:
        return
    await update.message.reply_text(Message1)

# ----------------- AUTO MESSAGE + PIN -----------------
async def auto_message(context: ContextTypes.DEFAULT_TYPE):
    try:
        msg = await context.bot.send_message(
            chat_id=GROUP_ID,
            text=CUSTOM_MESSAGE
        )
        await context.bot.pin_chat_message(
            chat_id=GROUP_ID,
            message_id=msg.message_id,
            disable_notification=True
        )
    except Exception as e:
        logging.error(f"Auto message error: {e}")

# ----------------- BOT SETUP -----------------
app = ApplicationBuilder().token(BOT_TOKEN).build()

# COMMAND HANDLER ONLY
app.add_handler(CommandHandler("rates", rates))

# AUTO MESSAGE EVERY 30 MIN
app.job_queue.run_repeating(auto_message, interval=1800, first=20)

print("✅ Bot running safely (command-based)...")
app.run_polling()
