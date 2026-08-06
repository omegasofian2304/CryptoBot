# Crypto Market Analysis Tool

A market analysis tool that monitors Bitcoin price data and generates trading
signals based on Dow Theory principles, enhanced with an EMA smoothing layer
and, eventually, a machine learning layer to filter noise and improve signal
reliability.

This project is built for learning purposes and focuses on clean architecture,
modular design, and progressive integration of real trading knowledge. The
strategy is grounded in Dow Theory, codified into an algorithm using EMA-based
pivot smoothing, with both a short-term and long-term trend score computed
from the same dataset.

The tool is designed as a market analysis assistant, not an automated trading
bot. Signals are surfaced to the user via a real-time dashboard for manual
decision-making, preserving full control over execution.

This project is developed in collaboration with a friend who is learning
frontend development, making it a dual-purpose project: building a serious
market analysis tool while providing a real-world context for learning React
and modern UI development.

It is also part of a broader personal journey toward quantitative finance and
ML engineering, with the goal of deeply understanding how algorithmic
strategies are designed, validated, and deployed in production environments.

## Architecture

The first version of this project is intentionally built as a monolithic
Python backend (FastAPI) to keep the initial scope manageable and focused on
the core logic. The project is now evolving toward a microservices design:
the Dow Theory signal engine is being rewritten in C++ for performance and
run as its own service, separate from the Python service handling data
fetching and the API layer. Communication between the two will be handled
through Redis pub/sub, which will also serve as a hands-on introduction to
distributed systems concepts.

```
Python Service          C++ Service
(Binance API,            (Dow Theory engine:
 FastAPI /candles,        EMA smoothing,
 FastAPI /trend)          swing detection,
                          trend scoring)
       |                        |
       ------ Redis pub/sub -----
                 |
          React Dashboard

## Current State

- `binance_api.py` - fetches OHLCV candles from Binance
- `analyzer.py` - Dow Theory engine: EMA smoothing, swing high/low detection,
  short-term and long-term trend scoring
- `main.py` (FastAPI) - exposes `/candles` and `/trend` endpoints, with input
  validation and error handling
- C++ port of the Dow Theory engine in progress
- React frontend scaffolding in progress

## Module Description

**backend/** - Python service: Binance API integration, OHLCV fetching, and
the FastAPI layer exposing `/candles` and `/trend` to the frontend

**analysis_cpp/** - C++ microservice progressively taking over the Dow Theory
engine (EMA smoothing, swing detection, short/long-term trend scoring) for
performance

**frontend/** - React real-time interface

## Installation

### 1. Clone the repository
```bash
git clone <repo>
cd crypto-analysis-tool
```

### 2. Backend - install dependencies
```bash
pip install -r requirements.txt
```

### 3. Backend - run locally
```bash
uvicorn backend.api.main:app --reload
```

### 4. Frontend - install dependencies
```bash
cd frontend
npm install
```

### 5. Frontend - run locally
```bash
npm run dev
```

## API Endpoints

**GET /candles** - returns raw OHLCV candles
```
/candles?symbol=BTCUSDT&interval=1h&limit=100
```

**GET /trend** - returns short-term and long-term Dow Theory trend scores
```
/trend?symbol=BTCUSDT&interval=1h&limit=1000
```

## Configuration

Edit `config/settings.py`:

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
- **C++** - performance-critical Dow Theory engine (in progress)
- **Binance API** - market data (OHLCV candles)
- **FastAPI** - internal API layer
- **React + Tailwind** - real-time dashboard
- **Redis** - inter-service messaging and caching (planned)
- **MySQL** - price history and signal storage (planned)
- **scikit-learn** - ML signal filtering (planned)
- **Docker + Docker Compose** - containerisation and orchestration (planned)
- **Telegram Bot API** - real-time signal alerts (planned)