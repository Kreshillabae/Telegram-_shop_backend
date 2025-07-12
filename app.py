import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

BOT_TOKEN = '8036297818:AAFcg7_Akiv83HK7JcolJul7-8Qq2n2JrhY'
CHAT_ID = '6945455531'

@app.route('/')
def home():
    return "Telegram Live"

@app.route('/order', methods=['POST'])
def order():
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

    try:
        response = requests.post(url, json=payload)
        telegram_response = response.json()
        status_code = response.status_code
    except Exception as e:
        return jsonify({
            'status': 'failed',
            'error': str(e)
        }), 500

    return jsonify({
        'status': 'Order received',
        'telegram_status': status_code,
        'telegram_response': telegram_response
    }), 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
