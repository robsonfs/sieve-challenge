from unittest import TestCase
from requests.models import Response

from crawler import Crawler

class TestCrawler(TestCase):

    def setUp(self):

        self.crawler = Crawler()

    def test_get_response(self, http_verb, url):
        response = self.crawler.get_response()
        self.assertTrue(isinstance(response, Response))
