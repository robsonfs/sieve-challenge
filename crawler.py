import requests

class Crawler:

    def get_response(self, url="http://www.epocacosmeticos.com.br/"):
        response = requests.get(url)
        return response

    def get_category_links(self):
        return []
