import os
import logging

# ✅ TEMP FIX (add your API key here for testing)
os.environ["OPENAI_API_KEY"] = "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"

from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, OpenAI

def load_rag():
    try:
        # ✅ Correct file path
        file_path = os.path.join("data", "finance_docs.txt")

        with open(file_path, "r", encoding="utf-8") as f:
            texts = f.read().split("\n")

        texts = [t for t in texts if t.strip() != ""]

        # ❗ If file empty → error
        if len(texts) == 0:
            raise ValueError("finance_docs.txt is empty")

        embeddings = OpenAIEmbeddings()
        db = FAISS.from_texts(texts, embeddings)

        logging.info(f"RAG loaded with {len(texts)} documents.")

        return db

    except Exception as e:
        print("RAG LOAD ERROR:", e)   # 👈 will show in terminal
        return None


def ask_query(db, query):
    if db is None:
        return "Chatbot not initialized properly."

    docs = db.similarity_search(query, k=1)

    context = docs[0].page_content if docs else ""

    llm = OpenAI()

    prompt = f"""
    Answer based only on this context:
    {context}

    Question: {query}
    """

    return llm.invoke(prompt)