from fastapi import FastAPI
from web_api import cart_api

app = FastAPI()


@app.get("/health-check")
async def health():
    return {"status": "OK"}


app.include_router(cart_api.router)