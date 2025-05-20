from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up Alerts...")
    yield
    print("Shutting down Alerts...")

app = FastAPI(lifespan=lifespan)

@app.get("/alert")
async def get_alert():

    return {"alert": "Price threshold reached: BTC has dropped below your set threshold."}

if __name__ == "__main__":
    uvicorn.run("alerts:app", host="0.0.0.0", port=8002, reload=True)