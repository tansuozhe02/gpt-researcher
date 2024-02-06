from langchain.vectorstores import FAISS
from openai import Client



class Memory:
    def __init__(self, **kwargs):
        self._client = openai.Client(
            api_key="cannot be empty",
            base_url="http://127.0.0.1:9997/v1"
        )
    def get_embeddings(self, text):
        result = self._client.embeddings.create(
            model= "mistral-instruct-v0.1",
            input=text
        )
        embedding=result["data"][0]["embedding"]
        return embedding

