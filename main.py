from fastapi import FastAPI

app = FastAPI()


@app.get("/health-check")
async def health():
    return {"status": "OK"}
