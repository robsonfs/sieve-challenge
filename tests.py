from unittest import TestCase
from requests.models import Response

from crawler import Crawler

class TestCrawler(TestCase):

    def setUp(self):

        self.crawler = Crawler()

    def test_get_response(self):
        response = self.crawler.get_response(url="http://localhost")
        self.assertIsInstance(response, Response)

    def test_get_category_links(self):
        category_links = self.crawler.get_category_links()
        self.assertIsInstance(category_links, list)

    def test_get_product_url(self):
        pass

    def test_get_product_details(self):
        pass

    def test_product_details_to_csv_line(self):
        pass

    def test_generate_csv_file(self):
        pass
