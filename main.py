from fastapi import FastAPI, File, UploadFile
from scripts.parse_data import *
from typing import Annotated

app = FastAPI()

EXCEL_FILE = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
CSV_FILE = "text/csv"

@app.get("/health", status_code=200)
async def root():
    return {"message": "health-check"}

@app.post("/upload", status_code=201)
async def upload_excel(file: UploadFile):
    return {
        "filename": file.filename,
        "filetype": file.content_type
    }


@app.get("/stats", status_code=200)
async def get_parsed_building_stats(file: UploadFile):
    if file.content_type == EXCEL_FILE:
       pass 
    return
