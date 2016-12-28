import requests

class Crawler:

    def get_response(self, url="http://www.epocacosmeticos.com.br/"):
        response = requests.get(url)
        return response
