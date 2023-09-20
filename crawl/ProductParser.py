from selenium.webdriver.edge.options import Options
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time

class ProductParser:
    def __init__(self):
        self.products = []

    def selenium_one_page(self, url):
        options = Options()
        options.add_argument("--disable-popup-blocking")
        options.add_argument('--disable-default-apps')
        options.add_argument('--disable-notifications')
        edge = webdriver.Edge(options=options)
        edge.get(url)
        time.sleep(3)
        self.recordNamePrice(edge.page_source)

    def request_one_page(self, url):
        req = requests.get(url)
        self.recordNamePrice(req.text)
    
    def recordNamePrice(self, html_text):
        soup = BeautifulSoup(html_text, "html.parser")
        blocks = soup.find_all("div", attrs={"class":"D__N D__v"}) # get product-blocks
        for block in blocks:
            block_ps = block.find_all("p")
            name = block_ps[2].text
            price = block_ps[3].text
            self.products.append((name, price))
    
    def getProducts(self):
        return self.products

if __name__=="__main__":
    url = "https://tw.carousell.com/categories/women-s-fashion-4/"
    crawler = ProductParser()
    # crawler.request_one_page(url)
    crawler.selenium_one_page(url)
    print(len(crawler.getProducts()), crawler.getProducts()[0])