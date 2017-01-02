import requests
from bs4 import BeautifulSoup

class Crawler:

    def __init__(self, base_url="http://www.epocacosmeticos.com.br/"):
        self.base_url = base_url

    def get_response(self, url):
        response = requests.get(url)
        return response

    def parse_html(self, html_text):
        return BeautifulSoup(html_text, "html.parser")

    def get_urls(self, parsed_html, css_class=None):
        if css_class:
            css_class = "." + css_class
            urls = [
                url.get('href') for url in parsed_html.select(
                    css_class)[0].find_all("a")
            ]
            return urls

        urls = [url.get('href') for url in parsed_html.select('a')]
        return urls
