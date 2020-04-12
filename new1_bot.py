import telebot
from telebot import apihelper
import requests

TOKEN = '1187232177:AAHwgtMxicM0U9bcd2P4tu2yObjr4CQvDWc'
def main(): 
    bot = telebot.TeleBot(TOKEN)

    

    @bot.message_handler(commands=['start', 'go'])
    def start_handler(message):
            text=message.text.lower()
            chat_id=message.chat.id
            msg=bot.send_message(message.chat.id,'Привет, сколько лет тебе?')
            bot.register_next_step_handler(msg,askAge)
    def askAge(message):
        text=message.text.lower()
        chat_id=message.chat.id
        if not text.isdigit():
            msg=bot.send_message(chat_id,'Возраст должен быть числом, введи ещё раз')
            bot.register_next_step_handler(msg,askAge)
            return
        msg = bot.send_message(chat_id,'Так тебе всего '+text+'лет? Ладно, пойдет')
        

    @bot.message_handler(content_types=['text'])
    def text_handler(message):
        text=message.text.lower()
        chat_id=message.chat.id
        if text == "привет":
            bot.send_message(chat_id,'Привет, я бот')
        elif text =="как дела?":
            bot.send_message(chat_id,'Хорошо, а у тебя?')
        else:
            bot.send_message(chat_id, 'Не понял')
    @bot.message_handler(content_types=['photo','video','sticker'])
    def text_handler1(message):
        stiс=open('stic.webp','rb')
        chat_id=message.chat.id
        bot.send_sticker(chat_id,stiс)


    bot.polling(none_stop=True, interval=0)


if __name__ == '__main__':  
    try:
        main()
    except KeyboardInterrupt:
        exit()