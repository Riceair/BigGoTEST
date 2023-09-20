from selenium import webdriver
from bs4 import BeautifulSoup
import requests

class WebCrawler:
    def __init__(self):
        self.products = []

    def request_one_page(self, url):
        req = requests.get(url)
        self.recordNamePrice(req)
    
    def recordNamePrice(self, req):
        soup = BeautifulSoup(req.text, "html.parser")
        blocks = soup.find_all("div", attrs={"class":"D__N D__v"}) # get product-blocks
        for block in blocks:
            block = str(block)
            p_starts = self.findAllSubStr(block, "<p")
            p_ends = self.findAllSubStr(block, "</p>")
            name = self.getPText(block[p_starts[2]:p_ends[2]])
            price = self.getPText(block[p_starts[3]:p_ends[3]])
            self.products.append((name, price))

    def findAllSubStr(self, string, target):
        return [i for i in range(len(string)) if string.startswith(target, i)]
    
    def getPText(self, substring):
        return substring[substring.index(">")+1:]

if __name__=="__main__":
    url = "https://tw.carousell.com/categories/women-s-fashion-4/"
    crawler = WebCrawler()
    # crawler.request_one_page(url)