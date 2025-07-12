from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Your Telegram bot token and chat ID
BOT_TOKEN = '8036297818:AAFcg7_Akiv83HK7JcolJul7-8Qq2n2JrhY'
CHAT_ID = '6945455531'

# Home route
@app.route('/')
def home():
    return "Telegram shop bot is running"

# Checkout route to receive orders from your website
@app.route('/checkout', methods=['POST'])
def checkout():
    data = request.get_json()

    if not data or 'items' not in data:
        return jsonify({'error': 'Invalid order format'}), 400

    # Build order message
    message = "🛍️ *New Order Received:*

"
    total = 0
    for item in data['items']:
        message += f"- {item['name']} - ₦{item['price']}
"
        total += item['price']
    message += f"\n*Total:* ₦{total}"

    # Send message to Telegram
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': message,
        'parse_mode': 'Markdown'
    }
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        return jsonify({'message': 'Order sent successfully!'}), 200
    else:
        return jsonify({'error': 'Failed to send order to Telegram'}), 500

# Run the app (only if running locally, not on Render)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
