import requests
from lxml import html
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from Parser import Parser


class ParserNvidia(Parser):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 '
                      'Safari/537.36'}

    def __init__(self, url):
        self.url = url

    def parse(self, item):
        options = Options()
        options.headless = True
        driver = webdriver.Firefox(firefox_options=options)
        driver.get(self.url)

        try:
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[self::featured-product or self::product-details]//div[contains(@class,"price")]')))

            item.buyable = len(driver.find_elements_by_xpath('(//*[self::featured-product or self::product-details]//div[@class="buy"])[last()]//a[contains(@class, "stock-grey-out")]')) == 0
            item.price = driver.find_element_by_xpath('(//*[self::featured-product or self::product-details]//div[contains(@class,"price")])[last()]//span').text
            item.name = driver.find_element_by_xpath('(//*[self::featured-product or self::product-details]//h2[@class = "name"])[last()]').text

        except TimeoutException:
            print("Loading took too much time!")

        driver.quit()