from langchain_huggingface import HuggingFaceEmbeddings
from langchain_qdrant import QdrantVectorStore

from src.config import EMBEDDING_MODEL, QDRANT_PATH

COLLECTION_NAME = "rag_documents"


def get_embedding_model():
    """
    Load the embedding model.
    Embeddings convert text into vectors for semantic search.
    """
    return HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)


def create_vector_store(chunks):
    """
    Create and persist a Qdrant vector store from document chunks.
    """
    embeddings = get_embedding_model()

    vector_store = QdrantVectorStore.from_documents(
        documents=chunks,
        embedding=embeddings,
        path=QDRANT_PATH,
        collection_name=COLLECTION_NAME,
    )

    return vector_store


def load_vector_store():
    """
    Load an existing Qdrant vector store.
    """
    embeddings = get_embedding_model()

    vector_store = QdrantVectorStore.from_existing_collection(
        embedding=embeddings,
        path=QDRANT_PATH,
        collection_name=COLLECTION_NAME,
    )

    return vector_store