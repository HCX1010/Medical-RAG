from langchain_huggingface import HuggingFaceEmbeddings

def get_embedder(
    model_name: str = "sentence-transformers/all-MiniLM-L6-v2",
    device: str = "cuda"
) :
    """
    Create and return a LangChain Embeddings object.
    """
    return HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs={"device": device}
    )
