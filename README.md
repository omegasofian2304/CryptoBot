# Crypto Market Analysis Tool

A Python-based market analysis tool that monitors Bitcoin price data and generates
trading signals based on Dow Theory principles, enhanced with a machine learning
layer to filter noise and improve signal reliability.

This project is built for learning purposes and focuses on clean architecture,
modular design, and progressive integration of real trading knowledge. The strategy
is grounded in Dow Theory, progressively codified into an algorithm and enhanced
with a machine learning layer to improve signal reliability.

The tool is designed as a market analysis assistant, not an automated trading bot.
Signals are surfaced to the user via a real-time dashboard for manual decision-making,
preserving full control over execution.

This project is developed in collaboration with a friend who is learning frontend
development, making it a dual-purpose project: building a serious market analysis
tool while providing a real-world context for learning Vue.js and modern UI development.

It is also part of a broader personal journey toward quantitative finance and ML
engineering, with the goal of deeply understanding how algorithmic strategies are
designed, validated, and deployed in production environments.

## Architecture

The first version of this project is intentionally built as a monolithic Python
application to keep the initial scope manageable and focused on the core logic.
As the project matures, the architecture will progressively evolve toward a
microservices design, with each component running in its own Docker container
and communicating via Redis pub/sub. This transition will also serve as a
hands-on introduction to distributed systems concepts.

Additionally, performance-critical components such as the Dow Theory signal engine
may be progressively rewritten in C++ to explore low-latency optimisation techniques,
reflecting the kind of architecture used in real quantitative trading systems.

```
Data Service  ->  Strategy Service  ->  ML Service
(Binance API)     (Dow Theory)          (Signal filter)
                                               |
                                           API Service
                                           (FastAPI)
                                               |
                                        Dashboard (Vue.js)
                                        + Telegram Alerts
```

## Module Description

**data_service/** - Binance API integration, OHLCV fetching

**strategy_service/** - Dow Theory implementation, pivot detection,
support/resistance identification, signal generation

**ml_service/** - Dataset management, model training, signal confidence scoring

**api_service/** - FastAPI endpoints exposing signals and history to the frontend

**dashboard/** - Vue.js + Tailwind real-time interface

**shared/** - Shared data models, utilities and configuration

## Installation

### 1. Clone the repository
```bash
git clone <repo>
cd crypto-analysis-tool
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run locally
```bash
python main.py
```

## Configuration

Edit `shared/config.py`:

```python
BINANCE_API_KEY    = "your_api_key"
BINANCE_API_SECRET = "your_api_secret"
TELEGRAM_TOKEN     = "your_bot_token"
CHAT_ID            = "your_chat_id"
SYMBOL             = "BTCUSDT"
INTERVAL           = "1h"
SIGNAL_THRESHOLD   = 0.70
```

## Tech Stack

- **Python** - core logic, data processing, ML
- **Binance API (CCXT)** - market data (OHLCV candles)
- **Redis** - inter-service messaging and caching (planned)
- **MySQL** - price history and signal storage
- **scikit-learn** - ML signal filtering
- **FastAPI** - internal API layer
- **Vue.js + Tailwind** - real-time dashboard
- **Docker + Docker Compose** - containerisation and orchestration (planned)
- **C++** - performance-critical components (planned)
- **Telegram Bot API** - real-time signal alerts
