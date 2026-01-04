import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

# ----------------- LOAD ENV VARIABLES -----------------
load_dotenv()  # Load .env file
BOT_TOKEN = os.getenv("BOT_TOKEN")
GROUP_ID = int(os.getenv("GROUP_ID"))

# ----------------- MESSAGES -----------------
Message1 = """✅️P2P U HOME ACCEPTED
WE ARE A GAMING COMPANY ALSO ACCEPT P2P DEALS WE HAVE LOT OF INR AND NEED USDT.💰
Gaming & stock fund ₹98 - 107
Upfront USDT:-
1. Mix funds          122INR
2. Stock funds.     116INR
3. Game funds      110INR
SUPPORTS IMPS, & BANK CARD
✅️DM ME @FPAY9
✅️JOIN OUR GROUP @uhome_buy_sell
"""

CUSTOM_MESSAGE = """🌟WE NEED USDT🌟 

✅️U-HOME P2P ACCEPTED

WE ARE A GAMING COMPANY ALSO ACCEPT P2P DEALS WE HAVE LOT OF INR AND NEED USDT.💰

P2P U HOME

      @. Stock funds.
      
       1.  107₹   (4K+ USDT MINIMUM)
       2.  106₹   (3K+ USDT MINIMUM)
       3.  105₹   (2K+ USDT MINIMUM)
       4.  104₹   (1K+ USDT MINIMUM)
       5.  103₹   (500+ USDT MINIMUM)

      @. Game funds

       1.  102₹   (4K+ USDT MINIMUM)
       2.  101₹   (3K+ USDT MINIMUM)
       3.  100₹   (2K+ USDT MINIMUM)
       4.  99₹    (1K+ USDT MINIMUM)
       5.  98₹    (500+ USDT MINIMUM)

      @. Loan repayment

       1. 103₹  (3K+ USDT MINIMUM)

ADVANCED USDT:- 
      
      @. Mix funds               122INR
      @. Stock funds.           116INR 
      @. Game funds             110INR

      @. Loan repayment

       1. 105₹  (3K+ USDT MINIMUM)
 
✅️DM ME @FPAY9

✅️JOIN OUR GROUP @uhome_buy_sell
"""

# ----------------- AUTO REPLY -----------------
async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.chat.id == GROUP_ID:
        text = update.message.text.lower()
        if "hello" in text:
            await update.message.reply_text("👋 Hello! Welcome to the group")
        elif "price" in text or "help" in text:
            await update.message.reply_text(Message1)
        else:
            await update.message.reply_text(Message1)

# ----------------- AUTO MESSAGE + PIN -----------------
async def auto_message(context: ContextTypes.DEFAULT_TYPE):
    try:
        msg = await context.bot.send_message(chat_id=GROUP_ID, text=CUSTOM_MESSAGE)
        await context.bot.pin_chat_message(
            chat_id=GROUP_ID, message_id=msg.message_id, disable_notification=True
        )
    except Exception as e:
        print("Error sending message:", e)

# ----------------- BOT SETUP -----------------
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))
app.job_queue.run_repeating(auto_message, interval=1800, first=10)  # 30 min

print("✅ Bot running...")
app.run_polling()
