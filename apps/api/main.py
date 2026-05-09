from fastapi import FastAPI

app = FastAPI(
    title="MailOps AI",
    version="0.1.0"
)


@app.get("/")
async def root():
    return {
        "message": "MailOps AI API running"
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }
