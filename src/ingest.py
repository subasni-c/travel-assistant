from fastapi import UploadFile
import fitz  # PyMuPDF
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
from src.config import COLLECTION_NAME

async def ingest_pdf(file: UploadFile):
    print(f"📄 Processing PDF file: {file.filename}")
    content = await file.read()
    
    # Load PDF directly from memory
    docs = []
    pdf = fitz.open(stream=content, filetype="pdf")
    page_count = len(pdf)
    print(f"📑 PDF loaded successfully. Found {page_count} pages")
    
    try:
        for page_num in range(page_count):
            page = pdf[page_num]
            text = page.get_text()
            docs.append(Document(
                page_content=text,
                metadata={"page": page_num, "source": file.filename}
            ))
    finally:
        pdf.close()
    
    print("✂️ Splitting document into chunks...")
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = splitter.split_documents(docs)
    print(f"📚 Created {len(chunks)} text chunks")
    print(chunks)

    return chunks
