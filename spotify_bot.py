import telebot
import main_func
from telebot import types
import threading
from os import system
from bob_telegram_tools.utils import TelegramTqdm
from bob_telegram_tools.bot import TelegramBot
import time

bot = telebot.TeleBot('5537306204:AAHiqqkUb9aMSrX1hz6Y1eerLzITxA94fwA')

def load(driver,message1,message):
    while driver == None:
        bot.edit_message_text(chat_id = message.chat.id , message_id = message1.id , text = "Идет загрузка \\" )
        bot.edit_message_text(chat_id = message.chat.id , message_id = message1.id , text = "Идет загрузка |" )
        bot.edit_message_text(chat_id = message.chat.id , message_id = message1.id , text = "Идет загрузка /" )
        bot.edit_message_text(chat_id = message.chat.id , message_id = message1.id , text = "Идет загрузка ―" )
        bot.edit_message_text(chat_id = message.chat.id , message_id = message1.id , text = "Идет загрузка \\" )
        bot.edit_message_text(chat_id = message.chat.id , message_id = message1.id , text = "Идет загрузка |" )
        bot.edit_message_text(chat_id = message.chat.id , message_id = message1.id , text = "Идет загрузка /" )
        bot.edit_message_text(chat_id = message.chat.id , message_id = message1.id , text = "Идет загрузка ―" )
        bot.edit_message_text(chat_id = message.chat.id , message_id = message1.id , text = "Идет загрузка \\" )
        bot.edit_message_text(chat_id = message.chat.id , message_id = message1.id , text = "Идет загрузка |" )
        bot.edit_message_text(chat_id = message.chat.id , message_id = message1.id , text = "Идет загрузка /" )
        bot.edit_message_text(chat_id = message.chat.id , message_id = message1.id , text = "Идет загрузка ―" )
        bot.edit_message_text(chat_id = message.chat.id , message_id = message1.id , text = "Идет загрузка \\" )
        bot.edit_message_text(chat_id = message.chat.id , message_id = message1.id , text = "Идет загрузка |" )
        bot.edit_message_text(chat_id = message.chat.id , message_id = message1.id , text = "Идет загрузка /" )
        bot.edit_message_text(chat_id = message.chat.id , message_id = message1.id , text = "Идет загрузка ―" )
        bot.edit_message_text(chat_id = message.chat.id , message_id = message1.id , text = "Идет загрузка \\" )
        bot.edit_message_text(chat_id = message.chat.id , message_id = message1.id , text = "Идет загрузка |" )
        bot.edit_message_text(chat_id = message.chat.id , message_id = message1.id , text = "Идет загрузка /" )
        bot.edit_message_text(chat_id = message.chat.id , message_id = message1.id , text = "Идет загрузка ―" )
        bot.edit_message_text(chat_id = message.chat.id , message_id = message1.id , text = "Идет загрузка \\" )
        bot.edit_message_text(chat_id = message.chat.id , message_id = message1.id , text = "Идет загрузка |" )
        bot.edit_message_text(chat_id = message.chat.id , message_id = message1.id , text = "Идет загрузка /" )
        bot.edit_message_text(chat_id = message.chat.id , message_id = message1.id , text = "Идет загрузка ―" )
        time.sleep(2)

songs = {}
for_user = {}
driver = None 
number = 1
id_to_user = {}
song_name = ""
while True:
    @bot.message_handler(commands=['start'])
    def start(message):
        global driver
        if driver == None:
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton("Как пользоваться ботом?")
            item2 = types.KeyboardButton("Добавить песню")
            item3 = types.KeyboardButton("Просмотреть весь плейлист")
            markup.add(item1 , item2 , item3)
            bot.send_message(message.from_user.id , "Привет!" , reply_markup=markup)
            message1 = bot.send_message(message.from_user.id, "Идет загрузка");
            t = threading.Thread(target=load , args = (driver,message1,message))
            t.start()
            driver = main_func.prepering()
            bot.send_message(message.from_user.id , "Бот готов к работе" , reply_markup=markup)
            bot.delete_message(message.chat.id , message1.id)
    @bot.message_handler(content_types=['text'])
    def start(message):
        global songs
        global number
        global song_name
        global for_user
        if driver != None and message.text == "Как пользоваться ботом?":
            bot.send_message(message.from_user.id, "Как пользоваться ботом❓")
            bot.send_message(message.from_user.id, "Этот бот возвращает ссылку на песню в спотифай , перейдя по которой вы можете послушать ее без рекламы и без необходимости листать до нее , теряя пропуски🙂 Также вы можете создавать здесь плейлист из своих любимых песен и слушать его когда захочется😀")
            bot.send_message(message.from_user.id, 'Чтобы начать работу нажмите на кнопку "Добавить песню"')
            bot.send_message(message.from_user.id, 'После этого вы можете вводить название своей песни. Бот в свое время возвращает вам ссылку на эту песню и присваивает ей порядковый номер , по которому потом вы сможете сразу получить ссылку на эту песню. Все ваши добавленные песни с их номеров можно будет посмотреть по кнопке "Просмотреть весь плейлист"')
        elif driver != None and  message.text == "Добавить песню":
            bot.send_message(message.from_user.id, 'Введите название песни , в течении 5 секунд вы получите ссылку на нее')
        elif driver != None and message.text == "Просмотреть весь плейлист":     
            if number==1 :
                bot.send_message(message.from_user.id , "Плейлист пустой")
            else:
                for index in range(number-1):
                    bot.send_message(message.from_user.id , str(index+1)+ ":" + for_user[index+1])
        elif (driver!=None and ((len(message.text)==1 or len(message.text)==2) and (int(message.text)>=1 and int(message.text)<=99))):
            bot.send_message(message.from_user.id , songs[int(message.text)])
        else:
            if driver != None :
                song_name = message.text 
                song = main_func.listen(message.text , driver)
                songs[number] = song
                for_user[number] = song_name
                bot.send_message(message.from_user.id, str(number) + " : " + for_user[number])
                bot.send_message(message.from_user.id , songs[number])
                number+=1
            else:
                bot.send_message(message.from_user.id , "Подождите окончания загрузки")
    bot.polling(non_stop=True)


