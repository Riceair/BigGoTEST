from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
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
    
    def recordNamePrice(self, html_text):
        pass
    
    def getProducts(self):
        return self.products

if __name__=="__main__":
    url = "https://tw.carousell.com/categories/women-s-fashion-4/"
    crawler = ProductParser()
    crawler.selenium_one_page(url)
    print(len(crawler.getProducts()), crawler.getProducts()[0])