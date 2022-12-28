import telebot
from telebot import types
import time

# telegram bot token
API_BOT_TOKEN = '5977162947: AAGo1MyVIQZyFWEctKU0zvCr5yCf3KTdoiA'

TON_ADDRESS = 'EQCz7yI0FdoCH0BT2Hp7m8pUTsfuGEWl3e70tMdmrNpOqmzu'

URL_TONKEEPER = 'https://app.tonkeeper.com/transfer/' + TON_ADDRESS + '?amount=250000000'
URL_TONHUB = 'https://tonhub.com/transfer/' + TON_ADDRESS + '?amount=250000000'

bot = telebot.TeleBot(API_BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id,
                     "👋 Привет! Я твой бот-помошник!", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '👋 Поздороваться':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('Tonkeeper')
        btn2 = types.KeyboardButton('Правила сайта')
        btn3 = types.KeyboardButton('Советы по оформлению публикации')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '❓ Задайте интересующий вопрос', reply_markup=markup) #ответ бота

if __name__ == '__main__':
    while True:
        try:#добавляем try для бесперебойной работы
            bot.polling(none_stop=True)#запуск бота
        except:
            time.sleep(10)#в случае падения       

"""
serverSideKey = 'your serverSide token'
headers_data = {'Authorization': 'Bearer ' + serverSideKey}"""

