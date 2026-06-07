import pdfplumber
import os
import shutil
import pytesseract
from pdf2image import convert_from_path
import chromadb
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer  # <-- Added

# 1. Automatic Reset
db_path = "./chroma_db"
if os.path.exists(db_path):
    print(f"Cleaning up old database at {db_path}...")
    shutil.rmtree(db_path)

# 2. Setup
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
client = chromadb.PersistentClient(path=db_path)
collection = client.get_or_create_collection(name="housing_docs")

# Load the exact same embedding model used for querying
model = SentenceTransformer('all-MiniLM-L6-v2')  # <-- Added

pdf_folder = "housing_pdf_ingest_pdf"
poppler_path = r'C:\Users\Parth\Downloads\Release-26.02.0-0\poppler-26.02.0\Library\bin'

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, 
    chunk_overlap=200,
    separators=["\n\n", "\n", " ", ""]
)

def ingest_pdfs():
    for filename in os.listdir(pdf_folder):
        if filename.endswith(".pdf"):
            file_path = os.path.join(pdf_folder, filename)
            print(f"Processing: {filename}...")
            
            text = ""
            # Standard extraction
            try:
                with pdfplumber.open(file_path) as pdf:
                    text = "\n".join([page.extract_text() or "" for page in pdf.pages])
            except Exception as e:
                print(f"  Standard extraction warning for {filename}: {e}")

            # OCR Fallback
            if not text.strip():
                try:
                    images = convert_from_path(file_path, poppler_path=poppler_path)
                    text = "\n".join([pytesseract.image_to_string(img) for img in images])
                except Exception as e:
                    print(f"  OCR failed for {filename}: {e}")
                    continue

            # Chunk, Embed, and Store
            if text.strip():
                chunks = text_splitter.split_text(text)
                
                # Generate embeddings for all chunks in this file at once
                embeddings = model.encode(chunks).tolist()  # <-- Added
                
                for i, chunk in enumerate(chunks):
                    collection.add(
                        documents=[chunk],
                        embeddings=[embeddings[i]],  # <-- Explicitly pass the vector
                        ids=[f"{filename}_chunk_{i}"],
                        metadatas=[{"source": filename}]
                    )
                print(f"  Successfully added {len(chunks)} smart chunks for {filename}.")

if __name__ == "__main__":
    ingest_pdfs()