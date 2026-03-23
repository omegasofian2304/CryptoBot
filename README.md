# Crypto Alert Bot

A Python bot that monitors Bitcoin price data and sends Telegram alerts
when trading opportunities are detected based on technical analysis.

This project was built for learning purposes and focuses on clean
architecture, modular design, and integration with external services
such as the Binance API, MySQL databases, and Telegram notifications.

The goal is to progressively implement real trading knowledge into the
bot over time — starting with basic price alerts and evolving toward
a full algorithmic trading assistant capable of detecting technical
setups (support/resistance, Fibonacci retracements, candlestick
patterns) and suggesting entry points with TP and SL levels.

------------------------------------------------------------------------

## Current Features

- Fetch Bitcoin OHLCV data from the Binance API
- Store price history in a MySQL database
- Analyze price movements and detect basic signals
- Send Telegram alerts when thresholds are exceeded
- Modular and extensible project structure

------------------------------------------------------------------------

## Planned Implementations (Progressive Roadmap)

The bot will evolve as my trading knowledge deepens. Here is the
planned roadmap:

**Phase 1 — Basic Alerts (current)**
- Fetch BTC/USDT price in real time
- Detect significant price movements
- Send Telegram alerts with price and % change

**Phase 2 — Technical Analysis**
- Implement RSI and moving averages (MA20, MA50)
- Detect overbought / oversold conditions
- Add candlestick pattern recognition (hammer, engulfing, doji)

**Phase 3 — Support & Resistance + Fibonacci**
- Automatically detect key support and resistance levels
- Calculate Fibonacci retracement levels (0.382, 0.5, 0.618)
- Alert when price enters the golden pocket zone (0.382–0.618)

**Phase 4 — Entry Point Detection**
- Combine confluence signals (support + Fibonacci + candle confirmation)
- Suggest entry price, TP and SL levels via Telegram
- Include Risk/Reward ratio in the alert

**Phase 5 — Dashboard & Backtesting**
- Web dashboard (Vue.js) to visualize signals and history
- Backtesting engine to validate strategy on historical data
- Performance tracking (win rate, average R:R, P&L)

------------------------------------------------------------------------

## Module Description

**config/** - Global configuration settings (API keys, thresholds)

**services/** - External service integrations
- Binance API communication
- Telegram messaging
- Database interaction

**core/** - Business logic of the bot
- Market data analysis
- Alert triggering logic

**models/** - Data structures used by the application

**utils/** - Utility functions such as logging

**main.py** - Entry point — orchestrates the entire bot workflow

------------------------------------------------------------------------

## Installation

### 1. Clone the repository

```bash
git clone <repo>
cd crypto-alert-bot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

## Configuration

Edit the file `config/settings.py`:

```python
TELEGRAM_TOKEN = "your_bot_token"
CHAT_ID        = "your_chat_id"

SYMBOL           = "BTCUSDT"
INTERVAL         = "1h"
CHECK_INTERVAL   = 300

VOLATILITY_THRESHOLD = 5
```

------------------------------------------------------------------------

## Running the Bot

```bash
python main.py
```

The bot will:
1. Fetch BTC candlestick data from Binance
2. Store the data in MySQL
3. Analyze price movements and technical signals
4. Send a Telegram alert when a setup is detected

------------------------------------------------------------------------

## Tech Stack

- **Python** — core logic
- **Binance API** — market data (OHLCV candles)
- **MySQL** — price history storage
- **Telegram Bot API** — real-time alerts
- **Vue.js** *(planned)* — web dashboard