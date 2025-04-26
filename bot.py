from flask import Flask, request
import telebot
import os

TOKEN = "7867244578:AAHYaQ-uG93U9XZ4zkfIjasrr_YJnxE2MPM"
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_messages([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@app.route("/", methods=['GET'])
def index():
    return "Я работаю! 🤖", 200

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=port)
