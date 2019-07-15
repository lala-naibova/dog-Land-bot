import random
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from base import get_pic_url_st, get_pic_url_nd
import os


def send_button(bot, update):
    chat_id = update.effective_user.id
    keyboard = [
        [InlineKeyboardButton("🐶", callback_data='dog')]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.send_message(chat_id, "🦴🦴🦴 One more? 🦴🦴🦴", reply_markup=reply_markup)


def send_pic(bot, update):
    funcs = [get_pic_url_nd, get_pic_url_st]
    random_func = random.choice(funcs)
    url = random_func()
    chat_id = update.effective_user.id
    bot.send_photo(chat_id, url)


def start(bot, update):
    chat_id = update.effective_user.id
    keyboard = [
        [InlineKeyboardButton("Press here 🐶", callback_data='dog')]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.send_message(chat_id, "Welcome to 🐕Land", reply_markup=reply_markup)


def button(bot, update):
    query = update.callback_query
    if query.data == 'dog':
        send_pic(bot, update)
        send_button(bot, update)


token = os.environ["dogland_bot_token"]
updater = Updater(token)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(button))
updater.start_polling()
updater.idle()
