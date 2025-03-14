from numpy import ndarray
from chromadb import ClientAPI

from src.vector_store.base_retriever import BaseRetriever


class ChromaRetriever(BaseRetriever):
    def __init__(
            self,
            client_api: ClientAPI,
            collection_name: str
    ) -> None:
        self._collection = client_api.get_collection(collection_name)

    def retrieve(
            self,
            vector: ndarray[float],
            top_n: int = 10
    ) -> dict:
        results = self._collection.query(
            query_embeddings=[vector[0].tolist()],
            n_results=top_n
        )
        return results
