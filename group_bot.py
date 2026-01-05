import os
import time
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

# ----------------- LOGGING -----------------
logging.basicConfig(level=logging.INFO)

# ----------------- LOAD ENV VARIABLES -----------------
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
GROUP_ID = int(os.getenv("GROUP_ID"))

# ----------------- COOLDOWN SETTINGS -----------------
COOLDOWN = 30  # seconds
last_reply_time = 0

# ----------------- MESSAGES -----------------
Message1 = """✅️P2P U HOME ACCEPTED
WE ARE A GAMING COMPANY ALSO ACCEPT P2P DEALS WE HAVE LOT OF INR AND NEED USDT.💰
Gaming & stock fund ₹98 - 107
Upfront USDT:-
1. Mix funds        122INR
2. Stock funds     116INR
3. Game funds      110INR
SUPPORTS IMPS, & BANK CARD
✅️DM ME @FPAY9
✅️JOIN OUR GROUP @uhome_buy_sell
"""

CUSTOM_MESSAGE = """🌟WE NEED USDT🌟 

✅️U-HOME P2P ACCEPTED

WE ARE A GAMING COMPANY ALSO ACCEPT P2P DEALS WE HAVE LOT OF INR AND NEED USDT.💰

P2P U HOME

@ Stock funds
107₹ (4K+)
106₹ (3K+)
105₹ (2K+)
104₹ (1K+)
103₹ (500+)

@ Game funds
102₹ (4K+)
101₹ (3K+)
100₹ (2K+)
99₹  (1K+)
98₹  (500+)

ADVANCED USDT:
Mix funds   122INR
Stock funds 116INR
Game funds  110INR

✅️DM ME @FPAY9
✅️JOIN OUR GROUP @uhome_buy_sell
"""

# ----------------- AUTO REPLY (SAFE) -----------------
async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global last_reply_time

    if not update.message:
        return

    if update.message.chat.id != GROUP_ID:
        return

    # Ignore bot's own messages
    if update.message.from_user.is_bot:
        return

    now = time.time()
    if now - last_reply_time < COOLDOWN:
        return  # cooldown active

    text = update.message.text.lower()

    KEYWORDS = ["price", "rate", "usdt", "help", "p2p"]

    if any(word in text for word in KEYWORDS):
        await update.message.reply_text(Message1)
        last_reply_time = now

# ----------------- AUTO MESSAGE + PIN -----------------
async def auto_message(context: ContextTypes.DEFAULT_TYPE):
    try:
        msg = await context.bot.send_message(chat_id=GROUP_ID, text=CUSTOM_MESSAGE)
        await context.bot.pin_chat_message(
            chat_id=GROUP_ID,
            message_id=msg.message_id,
            disable_notification=True
        )
    except Exception as e:
        logging.error(f"Auto message error: {e}")

# ----------------- BOT SETUP -----------------
app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(
    MessageHandler(filters.TEXT & filters.Chat(GROUP_ID), auto_reply)
)

app.job_queue.run_repeating(auto_message, interval=1800, first=15)

print("✅ Bot running safely...")
app.run_polling()
