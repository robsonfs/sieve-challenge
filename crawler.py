import requests

class Crawler:

    def __init__(self, base_url="http://www.epocacosmeticos.com.br/"):
        self.base_url = base_url

    def get_response(self, url="http://www.epocacosmeticos.com.br/"):
        response = requests.get(url)
        return response

    def get_category_links(self):
        return []
