from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import uvicorn
import requests

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up Agent...")
    yield
    print("Shutting down Agent...")

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SUPPORTED_COINS = ["btc", "eth", "ltc", "xrp", "bch", "ada", "dot", "sol", "doge"]

@app.get("/assistant")
async def get_assistant(message: str = Query(..., description="Message for the assistant")):
    response_data = {}
    lower_message = message.lower()

    found_coin = None
    for coin in SUPPORTED_COINS:
        if coin in lower_message:
            found_coin = coin
            break

    # If user typed something like "price" or "btc" or "What's the price of ETH?"
    if "price" in lower_message or found_coin:
        coin_param = found_coin if found_coin else "btc"  # default to btc if we can't parse
        try:
            price_resp = requests.get(f"http://localhost:8000/price?coin={coin_param}")
            response_data["price"] = price_resp.json()
        except Exception as e:
            response_data["price_error"] = str(e)

    if "news" in lower_message or "crypto" in lower_message:
        try:
            news_resp = requests.get("http://localhost:8001/news")
            response_data["news"] = news_resp.json()
        except Exception as e:
            response_data["news_error"] = str(e)

    if "alert" in lower_message:
        try:
            alert_resp = requests.get("http://localhost:8002/alert")
            response_data["alert"] = alert_resp.json()
        except Exception as e:
            response_data["alert_error"] = str(e)

    # default fallback
    if not response_data:
        response_data["response"] = f"Assistant received your message: '{message}'"

    return {"response": response_data}

if __name__ == "__main__":
    uvicorn.run("assistant_agent:app", host="0.0.0.0", port=8003, reload=True)