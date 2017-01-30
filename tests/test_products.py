import unittest
import os
from unittest import mock
from products import Products
from crawler import Crawler

class TestProducts(unittest.TestCase):

    def setUp(self):
        crawler = Crawler()
        self.products = Products(crawler)

    def test_validate_crawler_parameter_on_product_objects(self):
        error = False

        try:
            Products("invalid_crawler")
        except ValueError:
            error = True

        if not error:
            self.fail("Call didn't throw a ValueError exception, but it should.")

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

    def test_to_csv(self):
        os.mkdir('tests/outputs/')
        self.products.add("Product Name", "Product Title", "Product URL")
        self.products.add("Product Name 2", "Product Title 2", "Product URL 2")
        self.products.to_csv('tests/outputs/products.csv')
        self.assertTrue('products.csv' in os.listdir('tests/outputs'))
        os.remove('tests/outputs/products.csv')
        os.rmdir('tests/outputs')

    @mock.patch.object(Crawler, 'load_site_urls')
    @mock.patch.object(Crawler, 'filter_urls')
    def test_load_products(self, mock_filter, mock_load_urls):
        crawler = Crawler()
        products = Products(crawler)

        # Carregar todas as urls do site
        products.load_products()
        crawler.load_site_urls.assert_called_with()

        # Filtrar as urls de produtos
        pattern = r'^http://www\.epocacosmeticos\.com/.+/p$'
        crawler.filter_urls.assert_called_with(crawler.site_urls, pattern)

        # chamar get_product_details para cada url de produto encontrada
        # armazenar o resultado da chamada em _products
