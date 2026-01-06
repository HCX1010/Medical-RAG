# rag/retriever.py
class Retriever:
    def __init__(self, vectordb):
        self.retriever = vectordb.as_retriever()

    def get_retriever(self):
        return self.retriever
