"""Base fetcher interface for store integrations."""

from abc import ABC, abstractmethod


class Fetcher(ABC):
    """Abstract base class for store-specific fetchers."""

    @abstractmethod
    def search(self, query: str, limit: int = 10) -> None:
        """Search for products matching the query."""
        raise NotImplementedError
