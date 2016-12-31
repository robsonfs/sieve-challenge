import unittest
from products import Products

class TestProducts(unittest.TestCase):

    def setUp(self):
        self.products = Products()

    def test_add(self):
        initial_len = len(self.products)
        self.products.add("Product Name", "Product Title", "Product URL")
        final_len = len(self.products)
        self.assertIs(initial_len, (final_len - 1))

    def test_add_duplicated(self):
        self.products.add("Product Name", "Product Title", "Product URL")
        initial_len = len(self.products)
        self.products.add("Product Name", "Product Title", "Product URL")
        final_len = len(self.products)
        self.assertTrue(initial_len == final_len)

    def test_add_success_return_true(self):
        created = self.products.add("Product Name", "Product Title", "Product URL")
        self.assertTrue(created)

    def test_add_fail_return_false(self):
        self.products.add("Product Name", "Product Title", "Product URL")
        created = self.products.add("Product Name", "Product Title", "Product URL")
        self.assertFalse(created)
