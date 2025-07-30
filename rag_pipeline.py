from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

loader = PyPDFLoader("rag/documents/medical_docs.pdf")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
split_docs = splitter.split_documents(docs)

embedding_model = HuggingFaceEmbeddings()
vectorstore = FAISS.from_documents(split_docs, embedding_model)
vectorstore.save_local("rag/vectorstore")

def get_rag_chain():
    retriever = FAISS.load_local("rag/vectorstore", embedding_model).as_retriever()
    return RetrievalQA.from_chain_type(llm=OpenAI(), retriever=retriever)