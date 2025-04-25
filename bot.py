import telebot
import os

TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет, я GlowitaBot 💫")

bot.polling()
