import telebot
from telebot import types

bot = telebot.TeleBot('6945295346:AAGjUJF-iXr4aI7BbzpTRJZmFUPNPTwMGKc')
#############
@bot.message_handler(commands=['start'])
def start(message):
     bot.send_message(message.chat.id, "Выберите любимого музыканта:/bakr или /ulukmanapo")


markup = types.InlineKeyboardMarkup()
item = types.InlineKeyboardButton("Перейти по ссылке", url="https://www.youtube.com/@ulukmanapo")
markup.add(item)


@bot.message_handler(commands=['ulukmanapo'])
def ulukmanapo(message):
     bot.send_message(message.chat.id, "Хорошего прослушивания:", reply_markup=markup)

markup1 = types.InlineKeyboardMarkup()
item = types.InlineKeyboardButton("Перейти по ссылке", url="https://www.youtube.com/@BakrMusic")
markup1.add(item)


@bot.message_handler(commands=['bakr'])
def bakr(message):
     bot.send_message(message.chat.id, "Хорошего прослушивания:", reply_markup=markup1)

bot.polling()



