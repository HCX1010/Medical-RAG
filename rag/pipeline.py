from langchain_classic.chains import RetrievalQA
from rag.loader import load_csv
from rag.splitter import split_documents
from rag.embedder import get_embedder
from rag.vector_store import VectorStore
from rag.retriever import Retriever
from rag.llm import load_llm
from rag.prompts import get_rag_prompt
import os

class RAGPipeline:
    def __init__(self, llm, retriever, prompt):
        """
        llm: LLM 物件
        retriever: LangChain retriever 物件
        prompt: PromptTemplate
        """
        self.qa = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=retriever,
            chain_type_kwargs={"prompt": prompt},
            verbose=True
        )

    def run(self, query: str):
        return self.qa.invoke(query)

    @staticmethod
    def init_pipeline(
        csv_path: str = r"D:\@Product\RAG_Project\data\raw\medquad.csv",
        embedding_device: str = "cuda",
        embedding_path: str = r"D:\@Product\RAG_Project\data\embeddings",
        llm_path: str = r"D:\@Product\RAG_Project\model\llm\llama-2-7b-chat.Q4_0.gguf"
    ):
        """靜態方法：初始化整個 pipeline"""
        # 讀取資料
        docs = load_csv(csv_path)
        chunks = split_documents(docs)

        # embedding
        embedding = get_embedder(device=embedding_device)

        # vector store
        vs = VectorStore(embedding_path, embedding)
        if os.path.exists(embedding_path) and os.listdir(embedding_path):
            vectordb = vs.load()
        else:
            vectordb = vs.build(chunks)

        # retriever
        retriever = Retriever(vectordb).get_retriever()

        # llm + prompt
        llm = load_llm(llm_path)
        prompt = get_rag_prompt()

        # 返回完整的 pipeline 物件
        return RAGPipeline(llm, retriever, prompt)
