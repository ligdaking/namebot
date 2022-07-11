# -*- coding: utf8 -*-
import telebot
bot = telebot.TeleBot('5514577445:AAHkIfQt_UbAwhWNscbgFXRamRGiFz18eEc')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Для отримання посилання натисніть «/» та оберіть потрібний пункт', parse_mode='html')

@bot.message_handler(commands=['dl'])
def start(message):
    bot.send_message(message.chat.id, 'dl.nure.ua', parse_mode='html')

@bot.message_handler(commands=['en'])
def start(message):
    bot.send_message(message.chat.id, '<a href="meet.google.com/shd-ueij-pfu"> Посилання на meet з ІМ </a>', parse_mode='html')

@bot.message_handler(commands=['fv'])
def start(message):
    bot.send_message(message.chat.id, '<a href="https://cutt.ly/mKN1PwW"> Відповіді до тестів з ФВ </a>', parse_mode='html')

@bot.message_handler(commands=['myv'])
def start(message):
    bot.send_message(message.chat.id, "*СПИСОК ГРУПИ ЕСТМ-20-1*\n\n*1.* Бабіков Ігор\n*2.* Бєлякова Євгенія\n*3.* Давидова Лілія\n*4.* Дорошенко Вікторія\n*5.* Іванісов Андрій  \n*6.* Костров Євгеній\n*7.* Логвиненко Денис\n*8.* Манченко Андрій\n*9.* Мельчаковський Вячеслав\n*10.* Нефьодова Ірина\n*11.* Римаренко Олексій\n*12.* Сидоров Євген\n*13.* Скірко Руслан\n*14.* Сльозкіна Єлизавета\n*15.* Удовиченко Кирило\n*16.* Шевчук Михайло\n*17.* Шеїн Станіслав\n*18.* Шутєєв Назар", parse_mode='MarkDown')

@bot.message_handler(commands=['predmet1'])
def start(message):
    bot.send_message(message.chat.id, 'Ссылка на условную пару по предмету1', parse_mode='html')

@bot.message_handler(commands=['predmet2'])
def start(message):
    bot.send_message(message.chat.id, 'Ссылка на условную пару по предмету2', parse_mode='html')

@bot.message_handler(commands=['predmet3'])
def start(message):
    bot.send_message(message.chat.id, 'Ссылка на условную пару по предмету3', parse_mode='html')

@bot.message_handler(commands=['tek_kr'])
def start(message):
    file = open('tek.pdf','rb')
    bot.send_document(message.chat.id, file, 'ТЕК КР1')

@bot.message_handler(commands=['bebra'])
def start(message):
    file = open('ESTMGO.png', 'rb')
    bot.send_photo(message.chat.id, file, 'bober')

bot.polling(none_stop=True)
