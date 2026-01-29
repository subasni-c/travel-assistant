from fastapi import FastAPI, UploadFile
from contextlib import asynccontextmanager
from pydantic import BaseModel
from src.ingest import ingest_pdf

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize resources here (e.g., database connections, models)  
    yield

app = FastAPI(lifespan=lifespan)

class QueryRequest(BaseModel):
    query: str

@app.post("/ask")
async def ask_question(req: QueryRequest):
    return {"response": "your answer"}

@app.post("/upload")
async def upload_file(file: UploadFile = None):
    if not file:
        return {"message": "No file uploaded"}
        
    if not file.filename.endswith('.pdf'):
        return {"message": "Please upload a PDF file"}
    
    try:
        await ingest_pdf(file)
        return {"message": "File processed successfully"}
    except Exception as e:
        return {"message": f"Error processing file: {str(e)}"}

