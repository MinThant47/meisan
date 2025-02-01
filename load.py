from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
# from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from llm_prompt import llm, prompt
import os
import time


# os.environ["GOOGLE_API_KEY"]= "AIzaSyC87rM9xeEqJ6Rt5LhguLed6QK5mzT6XBM"

# embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

embeddings = HuggingFaceEmbeddings()
# question = input("Enter a question: ")

# if "faq" in question.lower():
#     vectors = FAISS.load_local(
#     "faiss_index", embeddings, 'YTUFAQ', allow_dangerous_deserialization=True
# )
# elif "ec" in question.lower():
#     vectors = FAISS.load_local(
#     "faiss_index", embeddings, 'YTUEC', allow_dangerous_deserialization=True
# )
# elif "mce" in question.lower():
#     vectors = FAISS.load_local(
#     "faiss_index", embeddings, 'YTUMCE', allow_dangerous_deserialization=True
# )

def load_FAISS_index(faiss_name):
    vectors = FAISS.load_local("faiss_index", embeddings, faiss_name, allow_dangerous_deserialization=True)
    return vectors

def get_context(index_path, question):
    vectors = load_FAISS_index(index_path)
    document_chain=create_stuff_documents_chain(llm,prompt)
    retriever=vectors.as_retriever()
    retrieval_chain=create_retrieval_chain(retriever,document_chain)
    response=retrieval_chain.invoke({'input':question})
    return response

# vectors = load_FAISS_index("YTUFAQ")

# document_chain=create_stuff_documents_chain(llm,prompt)
# retriever=vectors.as_retriever()
# retrieval_chain=create_retrieval_chain(retriever,document_chain)
# start=time.process_time()
# response=retrieval_chain.invoke({'input':question})
# print("Response time :",time.process_time()-start)
# print(response['answer'])