import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from fastapi import FastAPI
from pydantic import BaseModel
from rag.pipeline import RAGPipeline

app = FastAPI(title="Local RAG API")

# 輸入資料模型
class Query(BaseModel):
    question: str

rag = RAGPipeline.init_pipeline()

# ---- API route ----
@app.post("/ask")
def ask_question(query: Query):
    answer = rag.run(query.question)
    return {"answer": answer}