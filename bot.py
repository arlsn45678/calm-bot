import telebot

TOKEN = "8644404485:AAF3SmWhrur9S7N6ZN21daQaQI6p560JxI8"
PRICE = 500

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(msg):
    bot.send_message(msg.chat.id, 'Привет! Я бот для ментального здоровья.\n/menu')

@bot.message_handler(commands=['menu'])
def menu(msg):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('💎 Подписка')
    bot.send_message(msg.chat.id, 'Меню:', reply_markup=markup)

@bot.message_handler(commands=['buy'])
def buy(msg):
    bot.send_invoice(
        msg.chat.id,
        'Подписка',
        '30 дней',
        'sub',
        '',
        'XTR',
        [telebot.types.LabeledPrice('Подписка', PRICE)]
    )

@bot.message_handler(func=lambda m: True)
def handler(msg):
    if msg.text == '💎 Подписка':
        bot.send_message(msg.chat.id, '/buy — купить')
    elif msg.successful_payment:
        bot.send_message(msg.chat.id, '✅ Подписка активирована')

bot.infinity_polling()
