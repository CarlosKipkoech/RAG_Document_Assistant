from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path


def load_pdf_documents(upload_path: str):

    """
    Load PDF docs from a given Path

    """
    documents = []

    pdf_files = Path(upload_path).glob("*.pdf")

    for pdf in pdf_files:
        loader = PyPDFLoader(str(pdf))
        docs = loader.load()
        
        documents.extend(docs) #adds multiple 
        
    return documents
