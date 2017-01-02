import re
from unittest import TestCase
from requests.models import Response
from bs4 import BeautifulSoup

from crawler import Crawler
from scripts import is_valid_url

class TestCrawler(TestCase):

    def setUp(self):

        self.html = """
        <html>
            <head><title>Some page title</title></head>
            <body>
                <h1>Some title</h1>
                <p>
                    some text
                </p>
                <p class="links">
                    <a href="http://link1.com">Link 1</a>
                    <a href="http://link2.com">Link 2</a>
                    <a href="https://link3.com">Link 3</a>
                </p>
                <a href="http://otherlink1.com">Other Link 1</a>
                <a href="http://otherlink2.com">Other Link 2</a>
                <a href="http://otherlink3.com">Other Link 3</a>
            </body>
        </html>
        """
        self.crawler = Crawler()
        self.regex_url = re.compile(r'^(http|https)://(\w+)\.(\w+)')

    def test_crawler_object_has_a_base_url(self):
        # TODO: The url must be validated at the moment the object is instantiated
        self.assertTrue(is_valid_url(self.crawler.base_url))

    def test_get_response(self):
        response = self.crawler.get_response(url="http://localhost")
        self.assertIsInstance(response, Response)

    def test_parse_html(self):
        parsed_html = self.crawler.parse_html(self.html)
        self.assertIsInstance(parsed_html, BeautifulSoup)

    def test_get_urls_from_css_class(self):
        parsed_html = self.crawler.parse_html(self.html)
        links = self.crawler.get_urls(parsed_html, "links")
        self.assertIs(len(links), 3)
        self.assertTrue(all(re.search(self.regex_url, link) for link in links))

    def test_get_urls_from_page(self):
        parsed_html = self.crawler.parse_html(self.html)
        links = self.crawler.get_urls(parsed_html)
        self.assertIs(len(links), 6)
        self.assertTrue(all(re.search(self.regex_url, link) for link in links))

    def test_get_product_url(self):
        pass

    def test_get_product_details(self):
        pass

    def test_product_details_to_csv_line(self):
        pass

    def test_generate_csv_file(self):
        pass
