
# this file prevents hardcoding values everywhere

import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

UPLOAD_DIR = "data/uploads"
QDRANT_PATH = "data/qdrant_db"

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
