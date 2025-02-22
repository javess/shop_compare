import requests
from fetchers.ocado.models import InitialState, Product
import re
import fire
from fetchers.fetcher import Fetcher


class OcadoFetcher(Fetcher):

    def replace_non_alpha_and_whitespace(self, string: str):
        return re.sub(r'[^a-zA-Z\s]', ' ', string.lower()).replace(' ', '-')

    def normalize_product_url(self, product: Product):
        return f"https://www.ocado.com/products/{self.replace_non_alpha_and_whitespace(product.name)}-{product.sku}"

    def search(self, query: str, limit: int = 10):

        url = f'https://www.ocado.com/search?entry={query}'

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"'
        }

        cookies = {
        }

        response = requests.get(url, headers=headers, cookies=cookies)

        initial_state = response.text.split("window.INITIAL_STATE =")[
            1].split("</script>")[0].strip(" ;\n")
        parsed_state = InitialState.model_validate_json(initial_state)

        product_by_sku = parsed_state.products.productsBySku.root
        counter = 0
        print("##### OCADO RESULTS ########")
        for sku in product_by_sku:
            product = product_by_sku[sku]
            print(f"{product.name}: {product.catchWeight} {product.price}")
            print(self.normalize_product_url(product)+"\n")
            counter += 1
            if counter > limit:
                break


def main(search: str, limit: int = 10):
    fetcher = OcadoFetcher()
    fetcher.search(search, limit)


if __name__ == "__main__":
    fire.Fire(main)
