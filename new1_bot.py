import telebot
from telebot import apihelper
import requests
import apiai
import json

TOKEN = '1187232177:AAHwgtMxicM0U9bcd2P4tu2yObjr4CQvDWc'
def main(): 
    bot = telebot.TeleBot(TOKEN)

    

    @bot.message_handler(commands=['start', 'go'])
    def start_handler(message):
            #text=message.text.lower()
            chat_id=message.chat.id
            msg=bot.send_message(chat_id,'Салют! Что скажешь?')
        

    @bot.message_handler(content_types=['text'])
    def text_handler(message):
        text=message.text.lower()
        chat_id=message.chat.id

        request=apiai.ApiAI('ac825c1f8d82438092800fc8972e8571').text_request() #токен к dialogflow
        request.lang='ru'
        request.session_id='TestSession' #Id Сессии диалога (нужно, чтобы потом учить бота)
        request.query=text #посылаем запрос к ИИ
        responseJson=json.loads(request.getresponse().read().decode('utf-8'))
        response=responseJson['result']['fulfillment']['speech']#разбираем json и вытаскиваем ответ

        #если есть ответ от бота - присылаем юзеру, если нет - бот его не понял
        if response:
            bot.send_message(chat_id,response)
        else:
            bot.send_message(chat_id,'Не понял, чо?')
        


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