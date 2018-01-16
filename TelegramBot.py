import telebot
from telebot import types
import const

bot = telebot.TeleBot(const.API_TOKEN)
markup_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Привет, я бот интернет-магазина")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()