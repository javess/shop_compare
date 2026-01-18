"""Search engine entrypoint and orchestration."""

import fire

from fetchers.fetcher import Fetcher
from fetchers.ocado.fetcher import OcadoFetcher
from fetchers.sainsburry.fetcher import SainsburryFetcher


class SearchEngine:
    """Aggregate multiple store fetchers and dispatch search queries."""

    def __init__(self) -> None:
        """Initialize fetchers used for price search."""
        self.fetchers: list[Fetcher] = [
            OcadoFetcher(),
            SainsburryFetcher(),
        ]

    def search(self, query: str, limit_per_provider: int = 5) -> None:
        """Run a search across all providers."""
        for f in self.fetchers:
            f.search(query, limit_per_provider)


def main(search: str, limit: int = 10) -> None:
    """CLI entrypoint for searching products."""
    fetcher = SearchEngine()
    fetcher.search(search, limit)


if __name__ == "__main__":
    fire.Fire(main)
