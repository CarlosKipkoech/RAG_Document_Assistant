from src.vector_store import load_vector_store




def get_retriever(k:int=4):
    """
    create a retriever from the existing vector store.
    k  = number of chunks to retrieve.

    """

    vector_store = load_vector_store()

    retriever = vector_store.as_retriever(

        search_kwargs={"k":k}

    )

    return retriever


def retrieve_relevant_documents(query: str, k:int=4):
    """
    Retrieve relevant document chunks for a user question.

    """

    retriever = get_retriever(k=k)
    documents = retriever.invoke(query)

    return documents