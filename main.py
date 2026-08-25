from fastapi import FastAPI

app = FastAPI(title="UA Platform", version="1.0.0")

@app.get("/")
def home():
    return {"message": "Verified Device & User-Agent Platform is running", "status": "ok"}

@app.get("/health")
def health():
    return {"status": "healthy"}
