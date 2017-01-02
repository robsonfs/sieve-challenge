import re
import requests
from bs4 import BeautifulSoup

class Crawler:

    def __init__(self, base_url="http://www.epocacosmeticos.com.br/"):
        self.base_url = base_url
        self.visited_urls = set()

    def get_response(self, url):
        response = requests.get(url)
        self.visited_urls.add(url)
        return response

    def parse_html(self, html_text):
        return BeautifulSoup(html_text, "html.parser")

    def get_urls(self, parsed_html, css_class=None, pattern=None):
        if css_class:
            css_class = "." + css_class
            urls = [
                url.get('href') for url in parsed_html.select(
                    css_class)[0].find_all("a")
            ]
            return urls

        if pattern:
            return [
                url.get('href') for url in parsed_html.select('a') if re.search(
                    pattern, url.get('href')
                )
            ]
        urls = [url.get('href') for url in parsed_html.select('a')]
        return urls
