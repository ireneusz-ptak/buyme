import json
import requests

from Parser import Parser


class ParserKomputronik(Parser):
    def __init__(self, url):
        self.url = url

    def parse(self, item):
        page = requests.get(self.url, headers=self.headers)

        prd_start = page.text.find("[", page.text.find('"products":')) + 1
        prd_end = page.text.find("]", page.text.find('"availability"', prd_start))

        if prd_start > 0 and prd_end > 0:
            data = json.loads(page.text[prd_start:prd_end])

            item.buyable = data["availability"] == "available"
            item.price = data["price"]
            item.name = data["name"]
