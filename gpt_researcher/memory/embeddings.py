from langchain.vectorstores import FAISS
from langchain_community.embeddings import XinferenceEmbeddings

xinference_server_url = "http://127.0.0.1:9997"

class Memory:
    def __init__(self, **kwargs):
        pass

    def get_embedding(self):
        embeddings = XinferenceEmbeddings(server_url=xinference_server_url, model_uid="mistral-instruct-v0.1")
        return embeddings

