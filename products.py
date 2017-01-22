import csv
from collections import namedtuple
from crawler import Crawler

class Products:

    def __init__(self, crawler):
        if not isinstance(crawler, Crawler):
            raise ValueError("crawler must be a Crawler object.")
        self._crawler = crawler
        self.products = []
        self.Product = namedtuple(
            "Product", ["name", "title", "url"]
        )

    def __len__(self):
        return len(self.products)

    def add(self, name, title, url):
        p = self.Product(name, title, url)
        if p not in self.products:
            self.products.append(
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

            for product in self.products:
                writer.writerow(
                    {
                        'name': product.name,
                        'title': product.title,
                        'url': product.url
                    }
                )
