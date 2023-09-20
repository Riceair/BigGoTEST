from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

class WebExtender:
    def __init__(self) -> None:
        options = Options()
        options.add_argument("--disable-popup-blocking")
        options.add_argument('--disable-default-apps')
        options.add_argument('--disable-notifications')
        self.edge = webdriver.Edge(options=options)
    
    # 將單一網頁延伸 (把顯示更多結果按完)
    def extend(self, url):
        self.edge.get(url)
        time.sleep(3)

        while True:
            buttons = self.edge.find_elements(By.CSS_SELECTOR, "button")
            if buttons[-1].text == "顯示更多結果":
                buttons[-1].click()
                time.sleep(2)
            else:
                break

    def extendTimes(self, url, times):
        self.edge.get(url)
        time.sleep(3)

        for _ in range(times):
            buttons = self.edge.find_elements(By.CSS_SELECTOR, "button")
            if buttons[-1].text == "顯示更多結果":
                buttons[-1].click()
                time.sleep(2)
            else:
                break

    def getPage(self):
        return self.edge.page_source

if __name__=="__main__":
    from ProductParserbs4 import ProductParserbs4

    url = "https://tw.carousell.com/categories/women-s-fashion-4/"
    extender = WebExtender()
    extender.extendTimes(url, 1)
    html_text = extender.getPage()

    parser = ProductParserbs4()
    parser.recordNamePrice(html_text)
    print(len(parser.products), parser.products)