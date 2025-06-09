# Telegram Admin Relay Bot

A simple yet powerful Telegram bot built with Python that acts as a communication bridge between users and a designated admin. It supports forwarding all types of messages — including text, stickers, media, documents, and more — and enables two-way conversation via replies.

## 🚀 Features

- Forwards user messages (text, photo, sticker, audio, video, etc.) to a predefined admin.
- Automatically stores and tracks conversation threads using message IDs.
- Allows admin to reply directly to forwarded messages — responses are sent back to the original user.
- Supports bi-directional conversation via reply-based threading.

## ⚙️ Setup
- Create a Telegram Bot: Go to @BotFather on Telegram and create a bot. Copy the API token it gives you.
- Get Your Telegram User ID: To receive forwarded messages and reply, you need your Telegram user ID. You can get it by messaging @userinfobot on Telegram.
- Update the Script: Open bot.py and replace the placeholder values with your actual credentials of TOKEN and YOUR_USER_ID.
- Run the Bot.

## 🛠️ Requirements

- Python 3.8+
- `python-telegram-bot` v20+

Install dependencies using:

```bash
pip install python-telegram-bot --upgrade
