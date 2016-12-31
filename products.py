from collections import namedtuple

class Products:

    def __init__(self):
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
