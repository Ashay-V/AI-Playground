from langchain_community.llms import Ollama
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

def get_llm(model_name="mistral"):
    return Ollama(model=model_name, streaming=True)

def get_streaming_llm(model_name="mistral"):
    return Ollama(
        model=model_name,
        callbacks=[StreamingStdOutCallbackHandler()]
    )