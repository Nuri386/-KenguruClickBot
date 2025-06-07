import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

API_TOKEN = os.getenv('API_TOKEN')

user_scores = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    keyboard = [
        [InlineKeyboardButton("🦘 Клик қилиш", callback_data='click')],
        [InlineKeyboardButton("📊 Профиль", callback_data='profile')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        f"Салом, {user.first_name}! Мен Кенгуру Кликер ботиман. Кенгкоин йиғиш учун 🦘 тугмасини босинг.",
        reply_markup=reply_markup
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id

    if user_id not in user_scores:
        user_scores[user_id] = 0

    if query.data == 'click':
        user_scores[user_id] += 1
        await query.answer(text=f"Сизда кенгкоинлар: {user_scores[user_id]}")
    elif query.data == 'profile':
        score = user_scores.get(user_id, 0)
        await query.answer()
        await query.edit_message_text(text=f"📊 Сизнинг профил: {score} кенгкоин")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ботдан фойдаланиш учун /start ёзинг ва тугмалардан фойдаланинг.")

def main():
    app = ApplicationBuilder().token(API_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CallbackQueryHandler(button))

    print("Бот ишга тушди...")
    app.run_polling()

if __name__ == '__main__':
    main()
