require("dotenv").config();
const TelegramBot = require("node-telegram-bot-api");

// ----------------- ENV -----------------
const BOT_TOKEN = process.env.BOT_TOKEN;
const GROUP_ID = Number(process.env.GROUP_ID);

// ----------------- BOT INIT -----------------
const bot = new TelegramBot(BOT_TOKEN, { polling: true });

// ----------------- MESSAGES -----------------
const Message1 = `✅️P2P U HOME ACCEPTED
WE ARE A GAMING COMPANY ALSO ACCEPT P2P DEALS WE HAVE LOT OF INR AND NEED USDT.💰
Gaming & stock fund ₹98 - 107
Upfront USDT:-
1. Mix funds       122INR
2. Stock funds     116INR
3. Game funds      110INR
SUPPORTS IMPS, & BANK CARD
✅️DM ME @FPAY9
✅️JOIN OUR GROUP @uhome_buy_sell
`;

const CUSTOM_MESSAGE = `🌟WE NEED USDT🌟 

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
`;

// ----------------- PIN STATE -----------------
let pinnedMessageId = null;

// ----------------- AUTO REPLY -----------------
bot.on("message", async (msg) => {
  try {
    if (msg.chat.id !== GROUP_ID || !msg.text) return;

    const text = msg.text.toLowerCase();

    if (text.includes("hello")) {
      await bot.sendMessage(GROUP_ID, "👋 Hello! Welcome to the group", {
        reply_to_message_id: msg.message_id
      });
    } else if (text.includes("price") || text.includes("help")) {
      await bot.sendMessage(GROUP_ID, Message1, {
        reply_to_message_id: msg.message_id
      });
    } else {
      await bot.sendMessage(GROUP_ID, Message1, {
        reply_to_message_id: msg.message_id
      });
    }
  } catch (err) {
    console.error("Reply error:", err.message);
  }
});

// ----------------- PIN / EDIT LOGIC -----------------
const sendOrEditPinnedMessage = async () => {
  try {
    // First time → send & pin
    if (!pinnedMessageId) {
      const msg = await bot.sendMessage(GROUP_ID, CUSTOM_MESSAGE);
      await bot.pinChatMessage(GROUP_ID, msg.message_id, {
        disable_notification: true
      });
      pinnedMessageId = msg.message_id;
      console.log("📌 Message pinned");
    } 
    // Next times → edit same message
    else {
      await bot.editMessageText(CUSTOM_MESSAGE, {
        chat_id: GROUP_ID,
        message_id: pinnedMessageId
      });
      console.log("✏️ Pinned message edited");
    }
  } catch (err) {
    console.error("Pinned message error:", err.message);
  }
};

// ----------------- INTERVAL (1 HOUR) -----------------
setTimeout(sendOrEditPinnedMessage, 5000); // first run after 5 sec
setInterval(sendOrEditPinnedMessage, 60 * 60 * 1000);

// ----------------- START -----------------
console.log("✅ Telegram bot is running safely...");


// ----------------- DUMMY HTTP SERVER (FOR RENDER WEB SERVICE) -----------------
const express = require("express");
const app = express();

const PORT = process.env.PORT || 3000;

app.get("/", (req, res) => {
  res.send("Telegram bot is running safely");
});

app.listen(PORT, () => {
  console.log(`🌐 HTTP server listening on port ${PORT}`);
});
