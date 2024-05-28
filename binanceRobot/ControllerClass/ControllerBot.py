import telebot
from telebot import types
#URL https://api.telegram.org/botBOTKEY/getUpdates
#URL https://api.telegram.org/bot6469308662:AAFP-0y3su3RbPku7WeLDDRUCzhQ-AUrt08/sendMessage?chat_id=23994455&text=hello

from dotenv import load_dotenv
load_dotenv()
import os

token = os.getenv("BOT_TOKEN")
chat_id = os.getenv("CHAT_ID")

bot = telebot.TeleBot(token)

class ControllerBot:
    def __init__(self, textMenu, textResult):
        self.textMenu = textMenu
        self.textResult = textResult
    
    #Command /start
    @bot.message_handler(commands=['start'])
    def start(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("💻 Buttom 1")
        markup.add(item1)
        bot.send_message(message.chat.id, "Selecione uma Opção:", reply_markup=markup)

    #Buttom 1
    @bot.message_handler(func=lambda message: message.text == "Buttom 1")
    def button1(message):
        bot.send_message(message.chat.id, "U Select Buttom 1")

    if __name__ == '__main__':
        bot.polling(none_stop=True)

'''
    #Command /start
    @bot.message_handler(commands=['start'])
    def start(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Buttom 1")
        markup.add(item1)
        bot.send_message(message.chat.id, "Selecione uma Opção:", reply_markup=markup)

    #Buttom 1
    @bot.message_handler(func=lambda message: message.text == "Buttom 1")
    def button1(message):
        bot.send_message(message.chat.id, "U select buttom 1")

    if __name__ == '__main__':
        bot.polling(none_stop=True)
'''