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

The project follows a microservices design: the Dow Theory signal engine runs
as its own C++ service, separate from the Python service handling data
fetching and the API layer. The two services communicate through Redis
pub/sub, which also serves as a hands-on introduction to distributed systems
concepts. All three components (Python service, C++ service, Redis) are
containerised and orchestrated together with Docker Compose.

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
```

## Current State

- `binance_api.py` - fetches OHLCV candles from Binance
- `redis_publisher.py` / `redis_subscribe.py` - publish candles to Redis and
  wait for the C++ service's trend result
- `main.py` (FastAPI) - exposes `/candles` and `/trend` endpoints, with input
  validation and error handling; `/trend` delegates the actual calculation
  to the C++ service over Redis
- C++ Dow Theory engine (`dow_theory.cpp`, EMA smoothing, swing detection,
  short/long-term trend scoring) and Redis client (`redis_client.cpp`) are
  complete and tested end-to-end
- Backend and analysis services are containerised (Docker) and orchestrated
  together with Redis via `docker-compose.yml`
- React frontend scaffolding in progress

## Module Description

**backend/** - Python service: Binance API integration, OHLCV fetching, and
the FastAPI layer exposing `/candles` and `/trend` to the frontend. Publishes
candles to Redis and reads back the trend result computed by the C++ service.

**analysis_cpp/** - C++ microservice handling the Dow Theory engine (EMA
smoothing, swing detection, short/long-term trend scoring). Subscribes to
candle updates on Redis and publishes the computed trend back.

**frontend/** - React real-time interface

## Installation

### Run everything with Docker Compose (recommended)

This starts Redis, the Python backend, and the C++ analysis service together,
each in its own container.

```bash
git clone <repo>
cd CryptoBot
docker-compose up --build
```

The API is then available at `http://localhost:8000`.

### Run services individually (development)

**Backend**
```bash
cd backend
pip install -r requirements.txt
uvicorn api.main:app --reload
```

**C++ analysis service** - requires CMake, a C++ compiler, hiredis, and
nlohmann-json installed locally (see `analysis_cpp/CMakeLists.txt`).
```bash
cd analysis_cpp
cmake -B build -S .
cmake --build build
./build/analysis_cpp
```

**Frontend**
```bash
cd frontend
npm install
npm run dev
```

Running services individually requires a local Redis instance reachable at
`127.0.0.1:6379`.

## API Endpoints

**GET /candles** - returns raw OHLCV candles
```
/candles?symbol=BTCUSDT&interval=1h&limit=100
```

**GET /trend** - returns short-term and long-term Dow Theory trend scores,
computed by the C++ service
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

- **Python** - core logic, data fetching, API layer
- **C++** - Dow Theory engine (EMA smoothing, swing detection, trend scoring)
- **Binance API** - market data (OHLCV candles)
- **FastAPI** - internal API layer
- **React + Tailwind** - real-time dashboard
- **Redis** - inter-service pub/sub messaging
- **Docker + Docker Compose** - containerisation and orchestration
- **MySQL** - price history and signal storage (planned)
- **scikit-learn** - ML signal filtering (planned)
- **Telegram Bot API** - real-time signal alerts (planned)