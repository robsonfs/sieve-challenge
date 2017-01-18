import re
import requests
from bs4 import BeautifulSoup

class Crawler:

    def __init__(self, base_url="http://www.epocacosmeticos.com.br/"):
        self.base_url = base_url
        self.site_urls = set()

    def parse_html(self, url):
        resp = requests.get(url)
        return BeautifulSoup(resp.text, "html.parser")

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
        urls = [
            url.get('href') for url in parsed_html.select('a') if self.base_url\
            in url.get('href')]
        return urls

    def get_product_details(self, url):
        product = []
        parsed_html = self.parse_html(url)
        # parsed_html = BeautifulSoup(resp.text, 'html.parser')
        product.append(parsed_html.h1.text)
        product.append(parsed_html.title.text)
        product.append(url)
        return product

    def load_site_urls(self):
        pattern = re.compile(r'http://www\.epocacosmeticos\.com\.br/.+')
        urls = {self.base_url}

        home_page = self.parse_html(self.base_url) # Home page parseada
        depts = self.get_urls(home_page, css_class='sub_dept') # Links das categorias

        # Getting links into category pages
        for dept in depts:
            dept_page = self.parse_html(dept)
            urls.update(self.get_urls(dept_page, pattern=pattern))
            urls.add(dept)

        # Getting links into home page
        urls.update(self.get_urls(home_page, pattern=pattern))

        # Getting all links into listed pages
        all_urls = set()
        for url in list(urls):
            page = self.parse_html(url)
            links = self.get_urls(page)
            all_urls.update(links)

        self.site_urls.update(all_urls)

        return (len(all_urls) or False)
