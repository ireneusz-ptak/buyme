import requests
from lxml import html

from Parser import Parser


class ParserMorele(Parser):
    def __init__(self, url):
        self.url = url

    def parse(self, item):
        page = requests.get(self.url, headers=self.headers)

        doc = html.fromstring(page.content)

        item.buyable = len(doc.xpath('//div[@class = "prod-available" and not(contains(., " 1 ")) and contains(., "szt")]//text()')) > 0 # and not(contains(., " 30 "))
        item.price = doc.xpath('//div[@id = "product_price_brutto"]//@content')[0]
        item.name = doc.xpath('//div[@class = "prod-name"]//text()')[0]