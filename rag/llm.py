# rag/llm.py
from langchain_community.llms import LlamaCpp
from langchain_core.callbacks import CallbackManager
from langchain_core.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

def load_llm(model_path: str):
    llm = LlamaCpp(
        model_path=model_path,
        n_gpu_layers=100,
        n_batch=512,
        n_ctx=2048,
        f16_kv=True,
        callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
        verbose=True,
    )
    return llm