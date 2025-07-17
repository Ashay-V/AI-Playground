from langchain_core.runnables import RunnableMap
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from backend.ollama_utils import get_llm, get_streaming_llm
from backend.vector_store import load_vector_store

def stream_rag_response(user_input: str):
    retriever = load_vector_store().as_retriever()
    llm = get_streaming_llm()

    prompt = PromptTemplate.from_template(
        """You are a helpful AI assistant. Use the following context to answer the question.
        
        Context:
        {context}
        
        Question:
        {question}
        
        """
    )

    chain = (
        RunnableMap({
            "context": lambda x: retriever.get_relevant_documents(x["question"]),
            "question": lambda x: x["question"],
        })
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain.stream({"question": user_input})