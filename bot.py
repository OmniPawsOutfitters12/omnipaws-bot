import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

WELCOME = """🐾 Welcome to OmniPaws Outfitters!

We have healthy Cats & Dogs + accessories - All prices in USD ($)

👇 Tap a number:

1️⃣ Cats & Kittens Prices
2️⃣ Dogs & Puppies Prices
3️⃣ How to Order & Delivery
4️⃣ Talk to Human

Just type 1, 2, 3 or 4"""

CATS_TEXT = """🐱 CATS & KITTENS - Prices in USD ($):

- Persian - $800
- Maine Coon - $1200
- British Shorthair - $900
- Exotic Shorthair - $750

All vaccinated + healthy + litter trained.
Free delivery box.

Type 2 for Dogs, 3 for Delivery, 4 for Human"""

DOGS_TEXT = """🐶 DOGS & PUPPIES - Prices in USD ($):

- German Shepherd - $800
- Bulldog - $1500
- Lhasa Apso - $500
- Rottweiler - $1100

All vaccinated + healthy.
Free delivery crate.

Type 1 for Cats, 3 for Delivery, 4 for Human"""

DELIVERY_TEXT = """📦 HOW TO ORDER & DELIVERY - USD ($):

- USA: $50 shipping, 2-3 days delivery
- Worldwide: $150 shipping
- Payment: PayPal, Zelle, CashApp (USD)
- All prices are in USD ($)

Type 4 to Talk to Human"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("1️⃣ Cats $", callback_data="1")],
        [InlineKeyboardButton("2️⃣ Dogs $", callback_data="2")],
        [InlineKeyboardButton("3️⃣ Delivery", callback_data="3")],
        [InlineKeyboardButton("4️⃣ Human", callback_data="4")],
    ]
    await update.message.reply_text(WELCOME, reply_markup=InlineKeyboardMarkup(keyboard))

async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "1": await query.message.reply_text(CATS_TEXT)
    elif query.data == "2": await query.message.reply_text(DOGS_TEXT)
    elif query.data == "3": await query.message.reply_text(DELIVERY_TEXT)
    elif query.data == "4": await query.message.reply_text("✅ Connecting to human... Please type your question, we reply in USD ($) prices only!")

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    t = update.message.text.strip()
    if t == "1": await update.message.reply_text(CATS_TEXT)
    elif t == "2": await update.message.reply_text(DOGS_TEXT)
    elif t == "3": await update.message.reply_text(DELIVERY_TEXT)
    elif t == "4": await update.message.reply_text("✅ Connecting to human... Type your question.")
    else: await update.message.reply_text(WELCOME)

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(handle_buttons))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
app.run_polling()
