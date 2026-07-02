-- Create database
CREATE DATABASE IF NOT EXISTS crypto_bot;

-- Use the database
USE crypto_bot;

-- Table storing price history
CREATE TABLE IF NOT EXISTS price_history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    coin VARCHAR(20) NOT NULL,
    price DECIMAL(18,8) NOT NULL,
    change_24h FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Optional: table storing alerts sent by the bot
CREATE TABLE IF NOT EXISTS alerts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    coin VARCHAR(20) NOT NULL,
    alert_type VARCHAR(50),
    message TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);