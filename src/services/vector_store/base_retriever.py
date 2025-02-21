from abc import ABC, abstractmethod
from numpy import ndarray


class BaseRetrieverService(ABC):
    @abstractmethod
    def find_similar(
            self,
            vector: ndarray[float],
            top_n: int = 10
    ) -> dict:
        raise NotImplemented
