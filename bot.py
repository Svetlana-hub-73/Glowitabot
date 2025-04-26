import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import random
from flask import Flask, request

TOKEN = '7867244578:AAHYaQ-uG93U9XZ4zkfIjasrr_YJnxE2MPM'  # Обязательно поставь сюда токен своего бота
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        "🌟 Привет, я GlowitaBot! 🌟\n\n"
        "Я здесь, чтобы поддержать тебя, вдохновить и подсказать добрые советы! ✨\n"
        "Пиши мне в любое время! 💬🌸"
    )

# Список советов
advices = [
    "Не бойся начинать с нуля! Каждый день — новый шанс.",
    "Будь собой, все остальные роли уже заняты.",
    "Не забывай отдыхать, чтобы в следующий раз быть ещё более продуктивным!",
    "Сделай что-то доброе для себя сегодня!",
    "Каждый маленький шаг приближает тебя к цели."
]

@bot.message_handler(commands=['advice'])
def send_advice(message):
    # Выбираем случайный совет
    advice = random.choice(advices)
    
    # Создаём кнопку для нового совета
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton("Получить совет", callback_data="new_advice")
    markup.add(button)
    
    # Отправляем совет и кнопку
    bot.send_message(
        message.chat.id, 
        f"🌸 Совет для тебя: {advice}\n\nНажми кнопку, чтобы получить новый совет!", 
        reply_markup=markup
    )

# Обработка нажатия на кнопку
@bot.callback_query_handler(func=lambda call: call.data == "new_advice")
def handle_new_advice(call):
    advice = random.choice(advices)
    bot.edit_message_text(
        f"🌸 Новый совет для тебя: {advice}", 
        call.message.chat.id, 
        call.message.message_id,
        reply_markup=call.message.reply_markup
    )

# Маршрут для Telegram Webhook
@app.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return '!', 200

@app.route('/', methods=['GET'])
def home():
    return "<h1>🌸 Привет! Я GlowitaBot! 🌸</h1><p>Я здесь, чтобы поддерживать тебя, давать советы и делать день ярче! 🌞</p>"


# Запуск приложения
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    bot.remove_webhook()
    bot.set_webhook(url=f"https://glowitabot.onrender.com/{TOKEN}")
    app.run(host="0.0.0.0", port=port)
