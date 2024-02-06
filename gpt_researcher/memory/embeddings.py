from langchain.vectorstores import FAISS
from xinference.client import Client



class Memory:
    def __init__(self, **kwargs):
        self._client = Client("http://127.0.0.1:9997")
        self._model = self._client.get_model("mistral-instruct-v0.1")

    def get_embeddings(self, text):
        return self._model.create_embedding(text)

