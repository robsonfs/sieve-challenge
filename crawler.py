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

    def extract_links_from_a_css_class(self, parsed_html, css_class):
        links = []
        css_class = "." + css_class
        for link in parsed_html.select(css_class)[0].find_all("a"):
            links.append(link.get("href"))
        return links
