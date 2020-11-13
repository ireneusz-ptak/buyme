import demjson as demjson
import requests

from Parser import Parser


class ParserEuro(Parser):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 '
                      'Safari/537.36'}

    def __init__(self, url):
        self.url = url

    def parse(self, item):
        page = requests.get(self.url, headers=self.headers)

        prd_start = page.text.find("{", page.text.find('UA.productDetails(')) + 1
        prd_end = page.text.find("}", page.text.find('status:', prd_start))

        if prd_start > 0 and prd_end > 0:
            data = demjson.decode("{" + page.text[prd_start:prd_end] + "}")

            item.buyable = data["status"] == "1"
            item.price = data["price"]
            item.name = data["name"]

