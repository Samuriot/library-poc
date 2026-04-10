from fastapi import FastAPI, File, UploadFile
from typing import Annotated

app = FastAPI()


@app.get("/health", status_code=200)
async def root():
    return {"message": "health-check"}

@app.post("/upload", status_code=200)
async def upload_excel(file: UploadFile):
    return {
        "filename": file.filename,
        "filetype": file.content_type
    }

