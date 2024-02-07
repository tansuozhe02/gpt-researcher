from langchain.vectorstores import FAISS
import openai


class Memory:
    def __init__(self, **kwargs):
        self._client = openai.Client(api_key="not empty", base_url="http://127.0.0.1:9997/v1")

    def get_embeddings(self, text):
        embeddings = self._client.embeddings.create(model='mistral-instruct-v0.1', input=[text])
        return embeddings

