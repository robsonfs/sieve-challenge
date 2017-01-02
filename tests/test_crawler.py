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
                <a href="http://example.com/patterns/mypatern1">My pattern</a>
                <a href="http://example.com/patterns/mypatern2">my other pattern</a>
            </body>
        </html>
        """
        self.crawler = Crawler()
        self.regex_url = re.compile(r'^(http|https)://(\w+)\.(\w+)')

    def test_crawler_object_has_a_base_url(self):
        # TODO: The url must be validated at the moment the object is instantiated
        self.assertTrue(is_valid_url(self.crawler.base_url))

    def test_get_response(self):
        visited_urls_before = len(self.crawler.visited_urls)
        response = self.crawler.get_response(url="http://localhost")
        visited_urls_after = len(self.crawler.visited_urls)
        self.assertIs(visited_urls_before, visited_urls_after - 1)
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

    def test_get_urls_with_pattern(self):
        parsed_html = self.crawler.parse_html(self.html)
        pattern = re.compile(r'^http://example\.com/patterns/.+')
        links = self.crawler.get_urls(parsed_html, pattern=pattern)
        self.assertIs(len(links), 2)
        self.assertTrue(all(re.search(self.regex_url, link) for link in links))

    def test_get_product_details(self):
        pass
