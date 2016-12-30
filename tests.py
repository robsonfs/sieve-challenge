from unittest import TestCase
from requests.models import Response
from bs4 import BeautifulSoup

from crawler import Crawler
from scripts import is_valid_url

class TestCrawler(TestCase):

    def setUp(self):

        self.crawler = Crawler()

    def test_crawler_object_has_a_base_url(self):
        self.assertTrue(is_valid_url(self.crawler.base_url))

    def test_get_response(self):
        response = self.crawler.get_response(url="http://localhost")
        self.assertIsInstance(response, Response)

    # def test_get_category_links(self):
    #     category_links = self.crawler.get_category_links()
    #     self.assertIsInstance(category_links, list)
    #     # TODO: Implementing mock
    #     # self.assertTrue(category_links)
    #     # self.assertTrue(all(is_valid_url(link) for link in category_links))

    def test_parse_html(self):
        html = """
        <html>
            <head><title>Some page title</title></head>
            <body>
                <h1>Some title</h1>
                <p>
                    some text
                </p>
            </body>
        </html>
        """
        parsed_html = self.crawler.parse_html(html)
        self.assertIsInstance(parsed_html, BeautifulSoup)

    def test_get_product_url(self):
        pass

    def test_get_product_details(self):
        pass

    def test_product_details_to_csv_line(self):
        pass

    def test_generate_csv_file(self):
        pass
