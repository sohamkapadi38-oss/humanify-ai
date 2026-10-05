from fastapi import FastAPI

app = FastAPI(title="Humanify AI")


@app.get("/")
def home():
    return {
        "status": "online",
        "message": "Humanify AI is running"
    }