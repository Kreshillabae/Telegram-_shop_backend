from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS so Netlify frontend can send requests

# Replace with your actual Telegram bot token and chat ID
BOT_TOKEN = '8036297818:AAFcg7_Akiv83HK7JcolJul7-8Qq2n2JrhY'
CHAT_ID = '6945455531'

@app.route('/')
def home():
    return "Telegram Live"

@app.route('/send_order', methods=['POST'])
def send_order():
    data = request.json
    order_items = data.get('order', [])
    total_price = data.get('total', 0)

    message = "🛒 *New Order Received!*\n\n"
    for item in order_items:
        message += f"- {item['product']}: ₦{item['price']}\n"
    message += f"\n*Total:* ₦{total_price}"

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': message,
        'parse_mode': 'Markdown'
    }
    response = requests.post(url, json=payload)

    return jsonify({
        'status': 'Order received',
        'telegram_status': response.status_code,
        'telegram_response': response.json()
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
