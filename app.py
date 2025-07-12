import telebot
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")

@app.route('/')
def home():
    return "Telegram Shop Bot is running."

@app.route('/order', methods=['POST'])
def handle_order():
    data = request.json
    print("New order received:", data)

    chat_id = os.getenv("ADMIN_CHAT_ID")
    if chat_id:
        message = f"📦 New order from {data.get('user', {}).get('first_name', 'User')}\n"
        for item in data['items']:
            message += f"- {item['name']}: ${item['price']}\n"
        send_message(chat_id, message)

    return {"status": "ok"}

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, json=payload)

if __name__ == "__main__":
    bot.polling()
    app.run(host="0.0.0.0", port=5000)
