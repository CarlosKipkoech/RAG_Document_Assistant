import streamlit as st
from pathlib import Path

from src.config import UPLOAD_DIR
from src.document_loader import load_pdf_documents
from src.text_splitter import split_documents
from src.vector_store import create_vector_store
from src.rag_chain import create_rag_chain
from src.retriever import retrieve_relevant_documents

st.set_page_config(
    page_title="RAG Document Assistant",
    layout="wide"
)

st.title("RAG Document Assistant")

uploaded_files = st.file_uploader(
    "Upload PDF Files",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:

    Path(UPLOAD_DIR).mkdir(parents=True, exist_ok=True)

    for file in uploaded_files:
        save_path = Path(UPLOAD_DIR) / file.name

        with open(save_path, "wb") as f:
            f.write(file.getbuffer())

    st.success("Files uploaded successfully")

    documents = load_pdf_documents(UPLOAD_DIR)
    chunks = split_documents(documents)

    st.write(f"Loaded {len(documents)} document pages")
    st.write(f"Created {len(chunks)} text chunks")

    if st.button("Process Documents"):

        with st.spinner("Creating vector store..."):
            create_vector_store(chunks)

        st.session_state["vector_store_ready"] = True

        st.success("Vector store created successfully!")

    with st.expander("Preview Documents"):
        for doc in chunks[:10]:
            st.markdown("### Document Chunk")
            st.write(doc.page_content[:500])
            st.write(doc.metadata)
            st.divider()

    if st.session_state.get("vector_store_ready"):

        st.subheader("Ask a Question")

        query = st.text_input(
            "Ask anything about uploaded documents"
        )

        if query:
            with st.spinner("Retrieving relevant chunks..."):
                relevant_docs = retrieve_relevant_documents(query)

            context = "\n\n".join(
                [doc.page_content for doc in relevant_docs]
            )

            rag_chain = create_rag_chain()

            with st.spinner("Generating answer..."):
                response = rag_chain.invoke({
                    "context": context,
                    "question": query
                })

            st.subheader("Answer")
            st.write(response.content)

            with st.expander("View Retrieved Chunks"):
                for doc in relevant_docs:
                    st.write(doc.page_content[:700])
                    st.write(doc.metadata)
                    st.divider()