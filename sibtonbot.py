import telebot
from telebot import types

# You can set parse_mode by default. HTML or MARKDOWN
bot = telebot.TeleBot('5951597049:AAE6e0lHOzahxsAED1RgrNs7051C2ystZs8')

# buttons Inline
''' @bot.message_handler(commands=['start'])
def url(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(
        text='Наш сайт', url='https://habr.com/ru/all/')
    markup.add(btn1)
    bot.send_message(message.from_user.id,
                     "По кнопке ниже можно перейти на сайт хабра", reply_markup=markup)
'''
# buttons Keyboard
''' @bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🇷🇺 Русский")
    btn2 = types.KeyboardButton('🇬🇧 English')
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id,
                     "🇷🇺 Выберите язык / 🇬🇧 Choose your language", reply_markup=markup)
'''


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
        btn1 = types.KeyboardButton('Как стать автором на Хабре?')
        btn2 = types.KeyboardButton('Правила сайта')
        btn3 = types.KeyboardButton('Советы по оформлению публикации')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '❓ Задайте интересующий вопрос', reply_markup=markup) #ответ бота
        