import csv
from collections import namedtuple
from crawler import Crawler

class Products:

    def __init__(self, crawler):
        if not isinstance(crawler, Crawler):
            raise ValueError("crawler must be a Crawler object.")
        self._crawler = crawler
        self._products = []
        self.Product = namedtuple(
            "Product", ["name", "title", "url"]
        )

    def __len__(self):
        return len(self._products)

    def load_products(self):
        self._crawler.load_site_urls()

    def add(self, name, title, url):
        p = self.Product(name, title, url)
        if p not in self._products:
            self._products.append(
                self.Product(name, title, url)
            )
            return True
        return False

    def to_csv(self, output_path="outputs/products.csv"):
        with open(output_path, 'a') as csvfile:
            fieldnames = ['name', 'title', 'url']
            writer = csv.DictWriter(
                csvfile, fieldnames=fieldnames, delimiter=';'
            )

            writer.writeheader()

            for product in self._products:
                writer.writerow(
                    {
                        'name': product.name,
                        'title': product.title,
                        'url': product.url
                    }
                )
