from langchain.vectorstores import FAISS
from xinference.client import Client



class Memory:
    def __init__(self, **kwargs):
        self._client = Client("http://localhost:9997")
        self._model = self._client.get_model("MODEL_UID")

    def create_embedding(self, text):
        return self._model.create_embedding(text)

