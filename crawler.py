import requests
from bs4 import BeautifulSoup

class Crawler:

    def __init__(self, base_url="http://www.epocacosmeticos.com.br/"):
        self.base_url = base_url

    def get_response(self, url):
        response = requests.get(url)
        return response

    def get_category_links(self):
        links = []
        base_response = self.get_response(self.base_url)
        return links

    def parse_html(self, html_text):
        return BeautifulSoup(html_text, "html.parser")
