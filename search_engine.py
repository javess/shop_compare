import fire
from fetchers.ocado.fetcher import OcadoFetcher
from fetchers.sainsburry.fetcher import SainsburryFetcher


class SearchEngine:
    def __init__(self):
        self.fetchers = [
            OcadoFetcher(),
            SainsburryFetcher()
        ]

    def search(self, query: str, limit_per_provider: int = 5):
        for f in self.fetchers:
            f.search(query, limit_per_provider)


def main(search: str, limit: int = 10):
    fetcher = SearchEngine()
    fetcher.search(search, limit)


if __name__ == "__main__":
    fire.Fire(main)
