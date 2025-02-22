from abc import ABC, abstractmethod


class Fetcher(ABC):
    @abstractmethod
    def search(self, query: str, limit: int = 10):
        pass
