import os
import telebot
from flask import Flask, jsonify

# Load the bot token from environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

# Set up Flask app
app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return "Telegram shop bot is running"

# Products route
@app.route('/products')
def get_products():
    return jsonify([])

# Bot command handler for /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to Honey Hair Garden shop!")

# Start both Flask app and bot polling when the script is run directly
if __name__ == "__main__":
    bot.polling(non_stop=True)
