"""Sainsbury's store fetcher."""

import fire
import requests

from fetchers.fetcher import Fetcher
from fetchers.sainsburry.models import SainsburryData


class SainsburryFetcher(Fetcher):
    """Fetcher for the Sainsbury's API."""

    def search(self, query: str, limit: int = 10) -> None:
        """Fetch and print products for a query."""
        url = f"https://www.sainsburys.co.uk/groceries-api/gol-services/product/v1/product?filter[keyword]={query}"

        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/133.0.0.0 Safari/537.36"
            ),
            "sec-ch-ua": '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"macOS"',
        }

        cookies = {}
        response = requests.get(url, headers=headers, cookies=cookies)
        parsed_state = SainsburryData.model_validate_json(response.text)

        counter = 0
        print("##### SAINSBURRY RESULTS ########")

        for product in parsed_state.products:
            if not product.retail_price:
                continue

            # TODO: Pull different prices based on product.product_type. Differentiate between
            # basic (string price) and catchweight (price per weight units).
            print(f"{product.name}: {product.retail_price.price}")
            print(product.full_url + "\n")
            counter += 1
            if counter > limit:
                break


def main(search: str, limit: int = 10) -> None:
    """CLI entrypoint for Sainsbury's fetcher."""
    fetcher = SainsburryFetcher()
    fetcher.search(search, limit)


if __name__ == "__main__":
    fire.Fire(main)
