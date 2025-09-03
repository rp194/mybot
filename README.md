# MyBot

MyBot is a simple Telegram bot that translates text messages into English or Persian using [googletrans](https://pypi.org/project/googletrans/) and the [python-telegram-bot](https://python-telegram-bot.org/) framework. Users can choose their target language with commands and any text they send will be translated and forwarded to the bot owner.

## Features

- `/start` welcomes the user and explains how to use the bot.
- `/en` and `/fa` commands select English or Persian as the translation target.
- Any plain text message is translated to the chosen language.
- Messages and translations are forwarded to the bot owner and logged to `status.txt`.

## Requirements

- Python 3.8+
- [python-telegram-bot](https://pypi.org/project/python-telegram-bot/)
- [googletrans](https://pypi.org/project/googletrans/)

Install dependencies with:

```bash
pip install python-telegram-bot googletrans
```

## Usage

1. Create a bot with [BotFather](https://core.telegram.org/bots#botfather) and obtain the API token.
2. Replace the placeholder token in `test_overrrs.py` with your own token or export it as an environment variable and load it in the script.
3. Run the bot:

```bash
python test_overrrs.py
```

Interact with your bot on Telegram and use `/en` or `/fa` to choose the target language before sending text.

## Notes

This project is a hobby experiment and is provided as-is. Remember to keep your bot token secret and avoid committing it to version control.

