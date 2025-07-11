# 📦 Telegram Shop Web App

A simple Telegram Web App + Bot backend to sell products inside Telegram.

## 📁 Project Structure

- **frontend/** — Telegram Web App (HTML/JS/CSS)
- **backend/** — Python Flask backend to receive orders
- **.env.example** — Example environment config

## 🚀 Setup Instructions

1. **Create your Telegram bot** via [@BotFather](https://t.me/botfather)
2. Set your bot token and admin chat ID in a `.env` file based on `.env.example`

### Frontend

Host the `frontend/` folder using Netlify, Vercel, or any static host.

### Backend

Deploy `backend/` using Render, Railway, or locally:

```bash
pip install -r requirements.txt
python app.py
```

## 📲 Telegram Integration

Send a message with a Web App button:

```bash
curl -X POST https://api.telegram.org/bot<token>/sendMessage \-d chat_id=<chat_id> \-d text="🛍️ Open our shop!" \-d reply_markup='{
  "keyboard": [[{"text": "🛍️ Open Shop", "web_app": {"url": "https://your-frontend-url"}}]],
  "resize_keyboard": true
}'
```

Done! 🎉