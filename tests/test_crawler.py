import re
from unittest import TestCase
from requests.models import Response
from bs4 import BeautifulSoup

from crawler import Crawler
from scripts import is_valid_url

class TestCrawler(TestCase):

    def setUp(self):
        self.crawler = Crawler()
        self.regex_url = re.compile(r'^(http|https)://(\w+)\.(\w+)')

    def test_crawler_object_has_a_base_url(self):
        # TODO: The url must be validated at the moment the object is instantiated
        self.assertTrue(is_valid_url(self.crawler.base_url))

    # def test_scrapping(self):
    #     self.crawler.scrapping("http://localhost")

    def test_parse_html(self):
        parsed_html = self.crawler.parse_html("http://localhost/tests/")
        self.assertIsInstance(parsed_html, BeautifulSoup)

    def test_get_urls_from_css_class(self):
        parsed_html = self.crawler.parse_html("http://localhost/tests/")
        links = self.crawler.get_urls(parsed_html, "links")
        self.assertIs(len(links), 3)
        self.assertTrue(all(re.search(self.regex_url, link) for link in links))

    def test_get_urls_from_page(self):
        parsed_html = self.crawler.parse_html("http://localhost/tests/")
        links = self.crawler.get_urls(parsed_html)
        self.assertIs(len(links), 9)
        self.assertTrue(all(re.search(self.regex_url, link) for link in links))

    def test_get_urls_with_pattern(self):
        parsed_html = self.crawler.parse_html("http://localhost/tests/")
        pattern = re.compile(r'^http://(\w+\.|)example\.com/patterns/.+')
        links = self.crawler.get_urls(parsed_html, pattern=pattern)
        self.assertIs(len(links), 2)
        self.assertTrue(all(re.search(self.regex_url, link) for link in links))

    # TODO: Mock this test
    # def test_get_product_details(self):
    #     p = self.crawler.get_product_details(
    #         "http://www.epocacosmeticos.com.br/effaclar-bb-blur-la-roche-posay-base-facial-corretiva/p"
    #     )
    #     self.assertTrue(p[0] == "Effaclar BB Blur La Roche Posay - Base Facial Corretiva - 30ml")
    #     self.assertTrue(p[1] == "Effaclar BB Blur La Roche-Posay - Base Facial Corretiva - Época Cosméticos - Época Cosméticos")
    #     self.assertTrue(
    #         p[2] == "http://www.epocacosmeticos.com.br/effaclar-bb-blur-la-roche-posay-base-facial-corretiva/p"
    #     )

    def test_product_urls_has_no_duplicable_elements(self):
        len_before_add = len(self.crawler.product_urls)
        self.crawler.product_urls.add("http://epocacosmeticos.com.br/product1/p")
        self.crawler.product_urls.add("http://epocacosmeticos.com.br/product1/p")
        len_after_add = len(self.crawler.product_urls)
        self.assertIs(len_before_add, len_after_add - 1)

    # def test_load_products_urls(self):
    #     # Extrai produtos da url base
    #     # Extrai produtos das urls de categorias
    #     # Extrai produtos das urls de subcategorias
    #     pass
