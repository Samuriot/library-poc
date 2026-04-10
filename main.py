from fastapi import FastAPI

app = FastAPI()


@app.get("/health", status_code=200)
async def root():
    return {"message": "health-check"}
