import telebot
from telebot import types
import datetime

token = '5650433394:AAFRMLUAXd23_s1BNYutqjkEg-mOfObHHvs'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Хочу", "учить питон")
    keyboard.row("версия", "расписание")
    keyboard.row("/help", "гитхаб")
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать свежую информацию о МТУСИ?', reply_markup=keyboard)



@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Чтобы я скинул ссылку на сайт МТУСИ, напиши "да" или "хочу"\n'
                                      'Чтобы я показал дату, напиши "дата"\n'
                                      'Чтобы я скинул ссылку на книгу по Питону, нажми "учить питон"\n'
                                      'Чтобы я скинул ссылку на расписание, нажми "расписание"\n'
                                      'Чтобы я показал версию бота, нажми "версия"\n'
                                      'Чтобы увидеть ссылку на гитхаб моего создателя, нажми "гитхаб"\n')


@bot.message_handler(commands=['гитхаб'])
def start_message(message):
    bot.send_message(message.chat.id, 'Ссылка на гитхаб - https://github.com/muzhahov?tab=repositories')

@bot.message_handler(commands=['дата'])
def start_message(message):
    bot.send_message(message.chat.id, datetime.date.today())

@bot.message_handler(commands=['раписание'])
def start_message(message):
    bot.send_message(message.chat.id, "https://mtuci.ru/time-table/")


@bot.message_handler(commands=['учить питон'])
def start_message(message):
    bot.send_message(message.chat.id, 'Хорошая книга по Питону - https://wombat.org.ua/AByteOfPython/AByteofPythonRussian-2.02.pdf')

@bot.message_handler(commands=['версия'])
def start_message(message):
    bot.send_message(message.chat.id, 'Версия бота 0.1')



@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "хочу":
        bot.send_message(message.chat.id, 'Тогда тебе сюда - https://mtuci.ru/')
    elif message.text.lower() == "дата":
        bot.send_message(message.chat.id, datetime.date.today())
    elif message.text.lower() == "учить питон":
        bot.send_message(message.chat.id, 'Хорошая книга по Питону - https://wombat.org.ua/AByteOfPython/AByteofPythonRussian-2.02.pdf')
    elif message.text.lower() == "да":
        bot.send_message(message.chat.id, 'Тогда тебе сюда - https://mtuci.ru/')
    elif message.text.lower() == "гитхаб":
        bot.send_message(message.chat.id, 'Ссылка на гитхаб - https://github.com/muzhahov?tab=repositories')
    elif message.text.lower() == "версия":
        bot.send_message(message.chat.id, 'Версия бота 0.1')
    if message.text.lower() != "хочу" and message.text.lower() != "дата" and message.text.lower() !="да" and message.text.lower() != "гитхаб" and message.text.lower() != "версия" and message.text.lower() != "учить питон":
        bot.send_message(message.chat.id, 'Команда не распознана, нажмите help для справки')



bot.infinity_polling()

