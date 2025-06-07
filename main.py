from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
import os

# TOKEN render environment variable орқали олинади
TOKEN = os.getenv('TOKEN')

user_scores = {}

def start(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    user_scores[user_id] = 0
    keyboard = [[InlineKeyboardButton("Kenguru’ни бос!", callback_data='click')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Ассалому алайкум! Kenguru ўйинига хуш келибсиз!", reply_markup=reply_markup)

def button(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.from_user.id
    user_scores[user_id] = user_scores.get(user_id, 0) + 1
    query.answer()
    query.edit_message_text(
        text=f"Siz {user_scores[user_id]} марта Kenguru’ни босдингиз!",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Yana bos!", callback_data='click')]])
    )

def main():
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CallbackQueryHandler(button))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
