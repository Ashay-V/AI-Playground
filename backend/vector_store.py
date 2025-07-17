from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

PERSIST_PATH = "db/vector_store"

def load_vector_store():
    embeddings = OllamaEmbeddings(model="mistral")
    vectorstore = Chroma(persist_directory=PERSIST_PATH, embedding_function=embeddings)
    return vectorstore

def create_vector_store_from_docs(doc_dir="data/documents"):
    embeddings = OllamaEmbeddings(model="mistral")
    
    # Load documents
    loader = DirectoryLoader(doc_dir, glob="**/*.txt", loader_cls=TextLoader)
    docs = loader.load()

    # Split documents into chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    split_docs = splitter.split_documents(docs)

    # Extract raw text and metadata
    texts = [doc.page_content for doc in split_docs]
    metadatas = [doc.metadata for doc in split_docs]

    vectorstore = Chroma.from_texts(
        texts=texts,
        embedding=embeddings,
        metadatas=metadatas,
        persist_directory=PERSIST_PATH
    )

    vectorstore.persist()

if __name__ == "__main__":
    create_vector_store_from_docs()
    print("Vector store created successfully!")