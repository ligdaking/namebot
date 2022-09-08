# -*- coding: utf8 -*-
import telebot


bot = telebot.TeleBot('5514577445:AAHkIfQt_UbAwhWNscbgFXRamRGiFz18eEc')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Натисніть на /help для ознайомлення з наявними командами', parse_mode='html')

@bot.message_handler(commands=['help'])
def start(message):
    bot.send_message(message.chat.id, '/dl -  посилання на dlnure\n/bd - посилання на пару Бази даних\n/csh - посилання на пару Цифрова схемотехніка\n/tvel - посилання на пару Твердотільна електроніка\n/log - посилання на пару Логіка\n/fv -  посилання на відповіді з Фізичного виховання\n/myv - список групи\n/mails - електронні адреси викладачів', parse_mode='MarkDown')

@bot.message_handler(commands=['dl'])
def start(message):
    bot.send_message(message.chat.id, 'dl.nure.ua', parse_mode='html')


@bot.message_handler(commands=['fv'])
def start(message):
    bot.send_message(message.chat.id, '<a href="bit.ly/slivtestov"> Відповіді до тестів з ФВ </a>', parse_mode='html')

@bot.message_handler(commands=['myv'])
def start(message):
    bot.send_message(message.chat.id, "*СПИСОК ГРУПИ ЕСТМ-20-1*\n\n*1.* Бабіков Ігор\n*2.* Бєлякова Євгенія\n*3.* Давидова Лілія\n*4.* Дорошенко Вікторія\n*5.* Іванісов Андрій  \n*6.* Костров Євгеній\n*7.* Логвиненко Денис\n*8.* Манченко Андрій\n*9.* Мельчаковський Вячеслав\n*10.* Нефьодова Ірина\n*11.* Римаренко Олексій\n*12.* Сидоров Євген\n*13.* Скірко Руслан\n*14.* Сльозкіна Єлизавета\n*15.* Удовиченко Кирило\n*16.* Шевчук Михайло\n*17.* Шеїн Станіслав\n*18.* Шутєєв Назар", parse_mode='MarkDown')

@bot.message_handler(commands=['bd'])
def start(message):
    bot.send_message(message.chat.id, 'Пара: <a href="meet.google.com/vwu-ajbb-wwh">Бази даних</a>\nВідвідування: <a href="dl.nure.ua/mod/attendance/view.php?id=313810">тицяй</a>\nКурс: <a href="dl.nure.ua/course/view.php?id=15303">тицяй</a>\nВикладач: Цехмістро Роман Іванович', parse_mode="html")

@bot.message_handler(commands=['csh'])
def start(message):
    bot.send_message(message.chat.id, 'Пара: <a href="https://meet.google.com/tuh-uayt-hfr">Цифрова схемотехніка</a>\nВідвідування: <a href="dl.nure.ua/mod/attendance/view.php?id=313558">тицяй</a>\nКурс: <a href="dl.nure.ua/course/view.php?id=15261">тицяй</a>\nВикладач: Тимошенко Леонід Петрович', parse_mode="html")

@bot.message_handler(commands=['tvel'])
def start(message):
    bot.send_message(message.chat.id, 'Пара: <a href="meet.google.com/eei-unrr-crn">Твердотільна електроніка</a>\nВідвідування: <a href="dl.nure.ua/mod/attendance/view.php?id=318086">тицяй</a>\nКурс: <a href="dl.nure.ua/course/view.php?id=14891">тицяй</a>\nВикладач: Галат Олександр Борисович', parse_mode="html")

@bot.message_handler(commands=['log'])
def start(message):
    bot.send_message(message.chat.id, 'Пара: <a href="meet.google.com/erd-pxjo-ofy">Логіка*</a>\nВідвідування: <a href="dl.nure.ua/mod/attendance/view.php?id=306729">тицяй</a>\nКурс: <a href="dl.nure.ua/course/view.php?id=14147">тицяй</a>\nВикладач: Старікова Галина Геньївна', parse_mode='html')

@bot.message_handler(commands=['tek_kr'])
def start(message):
    file = open('tek.pdf','rb')
    bot.send_document(message.chat.id, file, 'ТЕК КР1')

@bot.message_handler(commands=['bebra'])
def start(message):
    file = open('ESTMGO.png', 'rb')
    bot.send_photo(message.chat.id, file, 'bober')

@bot.message_handler(commands=['mails'])
def start(message):
    bot.send_message(message.chat.id, "поки юзлесс", parse_mode='MarkDown')

@bot.message_handler(commands=['ppmm'])
def start(message):
    bot.send_message(message.chat.id, 'Пара: <a href=meet.google.com/ndf-zibj-jwe">Проектування пристроїв на мікроконтролерах і ПЛІС. Мікроконтролери*</a>\nВідвідування ЛК: <a href="https://dl.nure.ua/mod/attendance/view.php?id=314251">тицяй</a>\nВідвідування ЛБ: <a href="https://dl.nure.ua/mod/attendance/view.php?id=314253">тицяй</a>\nКурс: <a href="https://dl.nure.ua/course/view.php?id=15358#section-0">тицяй</a>\nВикладач: Зубков Олег Вікторович', parse_mode='html')

bot.polling(none_stop=True)
