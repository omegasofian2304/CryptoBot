/*
Author : Isaïe Merminod
Date : 07.08.2026
Project : CryptoBot
Desc : Centralize api calls
*/

const BASE_URL = "http://127.0.0.1:8000"

class ApiError extends Error {
    constructor(message, status) {
        super(message)
        this.name = "ApiError"
        this.status = status
    }
}

async function request(endpoint, options = {}) {
    let response

    try {
        response = await fetch(`${BASE_URL}${endpoint}`, {
            ...options,
            headers: {
                "Content-Type": "application/json",
                ...options.headers,
            },
        })
    } catch (err) {
        throw new ApiError("Can't connect to server", null)
    }

    if (!response.ok) {
        let detail = "Unknown error"
        try {
            const errorBody = await response.json()
            detail = errorBody?.detail || detail
        } catch {
        }
        throw new ApiError(detail, response.status)
    }

    return response.json()
}

export async function fetchCandles(symbol, interval, limit) {
    return request(`/candles?symbol=${symbol}&interval=${interval}&limit=${limit}`)
}

export async function fetchTrend(symbol, interval, limit) {
    return request(`/trend?symbol=${symbol}&interval=${interval}&limit=${limit}`)
}


export { ApiError }