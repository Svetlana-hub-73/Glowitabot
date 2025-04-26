import os
import telebot
from flask import Flask, request

TOKEN = '7867244578:AAHYaQ-uG93U9XZ4zkfIjasrr_YJnxE2MPM'  # Обязательно поставь сюда токен своего бота
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Приветик! Я GlowitaBot — твой весёлый помощник! 🌟")

# Маршрут для Telegram Webhook
@app.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return '!', 200

# Просто главная страничка (если зайти через браузер)
@app.route("/")
def webhook():
    return "Я живой! 🌸"

# Запуск приложения
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    bot.remove_webhook()
    bot.set_webhook(url=f"https://glowitabot.onrender.com/{TOKEN}")
    app.run(host="0.0.0.0", port=port)
