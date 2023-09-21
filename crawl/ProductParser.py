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
        blocks = self.getListingBlocks(html_text) # get product-blocks
        for block in blocks:
            block_ps = block.find_all("p")
            name = block_ps[2].text
            price = block_ps[3].text
            self.products.append((name, price))
    
    def getListingBlocks(self, html_text):
        soup = BeautifulSoup(html_text, "html.parser")
        sections = soup.find_all("section") # 商品在最下面的section
        listing = sections[-1].findChildren("div" , recursive=False)[0]
        listing = listing.findChildren("div", recursive=False)[0]
        listing = listing.findChildren("div", recursive=False)[0]
        listing = listing.findChildren("div", recursive=False)
        class_name = self.__getBlockClassName(listing)
        blocks = soup.find_all("div", attrs={"class":class_name})
        return blocks

    # 取得當前商品的css class name
    def __getBlockClassName(self, listing):
        name_count = dict()
        for block in listing:
            class_name = " ".join(block['class'])
            if class_name not in name_count:
                name_count[class_name] = 1
            else:
                name_count[class_name] += 1
        product_name = sorted(name_count.items(), key=lambda item: item[1], reverse=True)[0][0]
        return product_name

    def getProducts(self):
        return self.products

if __name__=="__main__":
    url = "https://tw.carousell.com/categories/mobile-phones-6406/?t-id=1om8x0ShdF_1695279455729&t-source=featured_categories_sidebar"
    crawler = ProductParser()
    # crawler.request_one_page(url)
    crawler.selenium_one_page(url)
    print(len(crawler.getProducts()), crawler.getProducts()[0])