"""Unit tests for search engine and fetchers."""

from fetchers.ocado.fetcher import OcadoFetcher
from fetchers.ocado.models import Product
from search_engine import SearchEngine


class _Recorder:
    """Simple test double to record search calls."""

    def __init__(self) -> None:
        """Initialize call log."""
        self.calls = []

    def search(self, query: str, limit: int) -> None:
        """Record search calls."""
        self.calls.append((query, limit))


def test_search_engine_calls_all_fetchers() -> None:
    """SearchEngine delegates to all fetchers."""
    engine = SearchEngine()
    first = _Recorder()
    second = _Recorder()
    engine.fetchers = [first, second]

    engine.search("eggs", 3)

    assert first.calls == [("eggs", 3)]
    assert second.calls == [("eggs", 3)]


def test_ocado_normalize_product_url() -> None:
    """OcadoFetcher builds expected product URL."""
    fetcher = OcadoFetcher()
    product = Product(sku="123", name="Chicken Breast")

    assert (
        fetcher.normalize_product_url(product)
        == "https://www.ocado.com/products/chicken-breast-123"
    )
