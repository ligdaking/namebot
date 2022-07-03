import telebot

bot = telebot.TeleBot('5514577445:AAHkIfQt_UbAwhWNscbgFXRamRGiFz18eEc')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Для получения ссылки нажмите / и выберите нужный предмет', parse_mode='html')

@bot.message_handler(commands=['dl'])
def start(message):
    bot.send_message(message.chat.id, 'dl.nure.ua', parse_mode='html')

@bot.message_handler(commands=['en'])
def start(message):
    bot.send_message(message.chat.id, 'meet.google.com/shd-ueij-pfu', parse_mode='html')

@bot.message_handler(commands=['fv'])
def start(message):
    bot.send_message(message.chat.id, 'https://cutt.ly/mKN1PwW', parse_mode='html')

@bot.message_handler(commands=['tek_kr'])
def start(message):
    file = open('tek.pdf','rb')
    bot.send_document(message.chat.id, file, 'ТЕК КР1')

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "Марк, кто пидарок?":
        bot.send_message(message.chat.id, 'Пидарок — Игорь Бабиков.')
    elif message.text == "Я пидарок":
        bot.send_message(message.chat.id, 'Я знаю.')
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "Стас":
        bot.send_message(message.chat.id, 'Унитаз.')
    elif message.text == "Евген":
        bot.send_message(message.chat.id, 'Мать твоя Евген, а он Евгений')
bot.polling(none_stop=True)
