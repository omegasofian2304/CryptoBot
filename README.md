# Crypto Alert Bot

A Python bot that monitors the Bitcoin price and sends Telegram alerts
when significant market movements are detected.

This project was built for learning purposes and focuses on clean
architecture, modular design, and integration with external services
such as crypto APIs, MySQL databases, and Telegram notifications.

------------------------------------------------------------------------

## Features

-   Fetch Bitcoin price data from a crypto API
-   Store price history in a MySQL database
-   Analyze price movements
-   Send Telegram alerts when thresholds are exceeded
-   Modular and extensible project structure

------------------------------------------------------------------------

## Module Description

**config/** - Contains global configuration settings for the bot

**services/** - Handles all external services - Crypto API
communication - Telegram messaging - Database interaction

**core/** - Business logic of the bot - Data analysis - Alert triggering

**models/** - Data structures used by the application

**utils/** - Utility functions such as logging

**main.py** - Entry point of the program - Orchestrates the entire bot
workflow

------------------------------------------------------------------------

## Installation

### 1. Clone the repository

git clone `<repo>`{=html} cd crypto-alert-bot

### 2. Install dependencies

pip install -r requirements.txt

------------------------------------------------------------------------

## Configuration

Edit the file:

config/settings.py

Example:

TELEGRAM_TOKEN = "your_bot_token" CHAT_ID = "your_chat_id"

COINS = \["bitcoin"\]

CHECK_INTERVAL = 300 VOLATILITY_THRESHOLD = 5

------------------------------------------------------------------------

## Running the Bot

Start the bot with:

python main.py

The bot will: 1. Fetch BTC price data 2. Store the data in MySQL 3.
Analyze price changes 4. Send Telegram alerts when thresholds are
triggered

------------------------------------------------------------------------

## Possible Improvements

-   Support for multiple cryptocurrencies
-   Store additional market indicators
-   Add technical analysis (RSI, moving averages)
-   Create a web dashboard
-   Implement strategy backtesting
