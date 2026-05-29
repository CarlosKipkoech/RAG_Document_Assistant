RAG_PROMPT = """

You are a helpful AI assistant.
Answer the user's questions using only the provided Context.

If the answer is not founf in the context, Say: 
I could not find the answer in the uploaded documents

context:
{context}

Question:
{question}


Answer:

"""