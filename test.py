import telebot

bot = telebot.TeleBot('1374789933:AAEHh6a8-eQTQjJfSzaJeQlfzbpcc5vDhOA')
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Вкл. уведомления')
keyboard1.row('monday_1' , 'monday_2')
keyboard1.row('tuesday_1' , 'tuesday_2')
keyboard1.row('wednesday_1','wednesday_2')
keyboard1.row('thursday_1', 'thursday_2')
keyboard1.row('friday_1','friday_2')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)




@bot.message_handler(content_types=['text'])
def start_message(message):
    text = message.text.lower()
    print(text)
    if text == 'monday_1' :
        m1 = open('photo01.jpg', 'rb')
        bot.send_photo(message.chat.id, m1)
        bot.send_message(message.chat.id, '2 пара')
        bot.send_message(message.chat.id, "3 пара"'\nhttps://meet.google.com/ctk-rndb-shh')
    if text == 'monday_2':
       m2 = open('photo02.jpg', 'rb')
       bot.send_photo(message.chat.id, m2)
       bot.send_message(message.chat.id, '2 та 3 пара ''\nhttps://meet.google.com/lookup/deyjq7d5u3')
    if text == 'tuesday_1':
       m2 = open('photo03.jpg', 'rb')
       bot.send_photo(message.chat.id, m2)
       bot.send_message(message.chat.id, '3 пара' '\nhttps://meet.google.com/lookup/herpzsywwc?authuser=1&hs=179')
       bot.send_message(message.chat.id, '4 пара' '\nhttps://meet.google.com/lookup/deyjq7d5u3')
    if text == 'tuesday_2':
       m2 = open('photo04.jpg', 'rb')
       bot.send_photo(message.chat.id, m2)
       bot.send_message(message.chat.id, '...')
       bot.send_message(message.chat.id, '...')
    if text == 'wednesday_1':
       m2 = open('photo05.jpg', 'rb')
       bot.send_photo(message.chat.id, m2)
       bot.send_message(message.chat.id, '3 та 4 пара ''\nhttps://meet.google.com/lookup/gn6xb43ylz')
    if text == 'wednesday_2':
       m2 = open('photo06.jpg', 'rb')
       bot.send_photo(message.chat.id, m2)
       bot.send_message(message.chat.id, '3 та 4 пара' '\nhttps://meet.google.com/lookup/h4q4ms6f4d')
       
    if text == 'thursday_1':
       m2 = open('photo07.jpg', 'rb')
       bot.send_photo(message.chat.id, m2)
       bot.send_message(message.chat.id, '1 пара''\nhttps://meet.google.com/lookup/glfpo7kcyl')
       bot.send_message(message.chat.id, '2 пара ''\nhttps://meet.google.com/lookup/faeipe4kdo')
    if text == 'thursday_2':
       m2 = open('photo08.jpg', 'rb')
       bot.send_photo(message.chat.id, m2)
       bot.send_message(message.chat.id, '2 пара''\nhttps://meet.google.com/lookup/glfpo7kcyl')
       bot.send_message(message.chat.id, '3 пара ''\nhttps://meet.google.com/lookup/faeipe4kdo')
    if text == 'friday_1':
       m2 = open('photo09.jpg', 'rb')
       bot.send_photo(message.chat.id, m2)
       bot.send_message(message.chat.id, '3 та 4 пара' '\nhttps://meet.google.com/lookup/h4q4ms6f4d')
    if text == 'friday_2':
       m2 = open('photo10.jpg', 'rb')
       bot.send_photo(message.chat.id, m2)
       bot.send_message(message.chat.id, '...')
       bot.send_message(message.chat.id, '2 пара' '\nhttps://meet.google.com/lookup/deyjq7d5u3')
       bot.send_message(message.chat.id, '3 пара ''\nhttps://meet.google.com/lookup/h4q4ms6f4d')


bot.polling()