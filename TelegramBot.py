import telebot
from telebot import types
import const


bot = telebot.TeleBot(const.API_TOKEN)

markup_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
btn_adress = types.KeyboardButton('Адреса магазинов', request_location=True)
btn_payment = types.KeyboardButton('Способы оплаты')
btn_delivery = types.KeyboardButton('Способы доставки')
markup_menu.add(btn_adress, btn_delivery, btn_payment)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Привет, я бот интернет-магазина", reply_markup = markup_menu)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	if message.text == "Способы доставки":
		bot.reply_to(message, "Доставка курьером, самовывоз, почта России", reply_markup = markup_menu)
	elif message.text == "Способы оплаты":
		bot.reply_to(message, "Наличные, по карте, Банковский перевод", reply_markup = markup_menu)
	else:
		bot.reply_to(message, message.text, reply_markup = markup_menu)

@bot.message_handler(func=lambda message: True, content_types=['location'])
def magazin_location(message):
	lon = message.location.longitude
	lat = message.location.latitude

	print('Широта {} Долгота {}'.format(lon, lat))

bot.polling()