import threading
from datetime import datetime
from urllib.parse import urlparse
from time import sleep

from Action import Action
from ParserEuro import ParserEuro
from ParserKomputronik import ParserKomputronik
from ParserMediaExpert import ParserMediaExpert
from ParserMorele import ParserMorele
from ParserNvidia import ParserNvidia


class Item:

    @staticmethod
    def from_url(url: str):
        url_parsed = urlparse(url)

        if url_parsed.hostname in ['komputronik.pl', 'www.komputronik.pl']:
            if url_parsed.path.find('product/') == -1:
                raise ValueError("Not a product URL: " + url)
            else:
                parser = ParserKomputronik(url)
                shop = 'Komputronik'
        elif url_parsed.hostname in ['euro.com.pl', 'www.euro.com.pl']:
            parser = ParserEuro(url)
            shop = 'EURO'
        elif url_parsed.hostname in ['mediaexpert.pl', 'www.mediaexpert.pl']:
            parser = ParserMediaExpert(url)
            shop = 'MediaExpert'
        elif url_parsed.hostname in ['morele.net', 'www.morele.net']:
            parser = ParserMorele(url)
            shop = 'Morele'
        elif url_parsed.hostname in ['nvidia.com', 'www.nvidia.com']:
            parser = ParserNvidia(url)
            shop = 'Nvidia'
        else:
            raise ValueError("Unsupported: " + url_parsed.hostname)

        return Item(parser, url, shop)

    def __init__(self, parser, url, shop):
        self._parser = parser
        self.url = url
        self.shop = shop
        self.buyable = None
        self.name = None
        self.price = None

    def parse(self):
        self._parser.parse(self)

    def run(self, interval, action):
        job_thread = threading.Thread(target=Item.check, args=(self, interval, action))
        job_thread.start()

    @staticmethod
    def check(item, interval, action: Action):
        while 1:
            print("[" + datetime.now().__str__() + "] Checking: " + item.url)
            item.parse()

            if item.buyable:
                result = "AVAILABLE!"
            else:
                result = "No luck."

            if item.name is not None:
                print("[" + datetime.now().__str__() + "] " + result + " (" + item.shop + ": " + item.name + ")")
            else:
                print("[" + datetime.now().__str__() + "] Can't parse: " + item.url)

            if item.buyable:
                action.act(item)
                return

            sleep(interval)
