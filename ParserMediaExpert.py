import requests
from lxml import html

from Parser import Parser


class ParserMediaExpert(Parser):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 '
                      'Safari/537.36'}

    def __init__(self, url):
        self.url = url

    def parse(self, item):
        page = requests.get(self.url, headers=self.headers)

        doc = html.fromstring(page.content)

        item.buyable = len(doc.xpath('//div[@class = "c-offerBox_addToCart"]//text()')) > 0
        item.price = doc.xpath('//meta[@property = "product:price:amount"]//@content')[0]
        item.name = doc.xpath('//meta[@property = "og:title"]//@content')[0]
