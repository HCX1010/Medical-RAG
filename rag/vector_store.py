# rag/vector_store.py
from langchain_chroma import Chroma
from langchain_core.embeddings import Embeddings

class VectorStore:
    def __init__(self, persist_dir: str, embedding: Embeddings):
        self.persist_dir = persist_dir
        self.embedding = embedding

    def build(self, documents):
        """
        一次性建立 / 更新向量資料庫
        """
        self.vectordb = Chroma.from_documents(
            documents=documents,
            embedding=self.embedding,
            persist_directory=self.persist_dir
        )
        return self.vectordb

    def load(self):
        """
        載入既有向量資料庫（不重建）
        """
        self.vectordb = Chroma(
            persist_directory=self.persist_dir,
            embedding_function=self.embedding
        )
        return self.vectordb
