from ControllerClass.ControllerBot import ControllerBot;
from meuip.ClassMeuip import ControllerIP
import telebot
from telebot import types
#URL https://api.telegram.org/botBOTKEY/getUpdates


from dotenv import load_dotenv
load_dotenv()
import os
token = os.getenv("BOT_TOKEN")
chat_id = os.getenv("CHAT_ID")

bot = telebot.TeleBot(token)

#bot.send_message(chat_id, "Sou o Contador Samuel Rocha")

'''
@bot.message_handler(commands=["start"])
def inicio(message):
    bot.reply_to(message, "Sou o Contador Samuel Rocha")

bot.polling(none_stop=True)
'''

#Command /foto
@bot.message_handler(commands=['teclado'])
def teclado(message):
    bot.send_photo(chat_id, open("foto.png"))

#Command /start
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("💻 Buttom 1")
    item2 = types.KeyboardButton("📉 Buttom 2")
    item3 = types.KeyboardButton("Buttom 3")
    item4 = types.KeyboardButton("Buttom 4")
    item5 = types.KeyboardButton("Buttom IP")
    markup.add(item1, item2, item3, item4, item5)
    
    bot.send_message(message.chat.id, "Selecione uma Opção:", reply_markup=markup)

#Buttom 1
@bot.message_handler(func=lambda message: message.text == "💻 Buttom 1")
def button1(message):
    bot.send_message(message.chat.id, "U select buttom 1")

#Buttom 2
@bot.message_handler(func=lambda message: message.text == "📉 Buttom 2")
def button2(message):
    bot.send_message(message.chat.id, "U select buttom 2")

#Buttom 3
@bot.message_handler(func=lambda message: message.text == "Buttom 3")
def button3(message):
    bot.send_message(message.chat.id, "U select buttom 3")

#Buttom 4
@bot.message_handler(func=lambda message: message.text == "Buttom 4")
def button4(message):
    bot.send_message(message.chat.id, "U select buttom 4")
    
#Buttom 5
@bot.message_handler(func=lambda message: message.text == "Buttom IP")
def buttonIP(message):
    bot.send_message(message.chat.id, f'IP Publico: {ControllerIP.meuip()}')
    
#Start bot
if __name__ == '__main__':
    bot.polling(none_stop=True)

