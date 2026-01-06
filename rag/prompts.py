# rag/prompts.py
from langchain_core.prompts import PromptTemplate

def get_rag_prompt():
    return PromptTemplate(
        input_variables=["context", "question"],
        template=
            """
                <<SYS>>
                    You are a professional doctor.
                    Use the following context to answer the question accurately.
                    If the answer is not in the context, say "I don't know based on the provided context".
                    List your answer clearly and cite the source.
                <</SYS>>

                [INST]
                    Context: {context}
                    Question: {question}
                [/INST]
            """ 
            )