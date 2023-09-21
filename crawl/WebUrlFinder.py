from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

class WebUrlFinder:
    def __init__(self, start_url):
        options = Options()
        options.add_argument("--disable-popup-blocking")
        options.add_argument('--disable-default-apps')
        options.add_argument('--disable-notifications')
        self.edge = webdriver.Edge(options=options)
        self.root_url = start_url[start_url.index("http"):start_url.index("com")+3]+"/"

    def getPageUrls(self):
        self.edge.get(self.root_url)
        time.sleep(2)
        categories, dropdown_btns = self.__getCategories()
        print(categories, dropdown_btns)
    
    def __openAll(self):
        buttons = self.edge.find_elements(By.CSS_SELECTOR, "button")
        for button in buttons:
            if button.text == "所有分類":
                button.click()
                time.sleep(1)
                break      

    def __getCategories(self):
        div_before_all = self.edge.find_elements(By.TAG_NAME, "div") # 在打開所有分類前的div數量
        self.__openAll() # 打開所有分類
        divs = self.edge.find_elements(By.TAG_NAME, "div")
        for div in div_before_all:
            divs.remove(div)

        # 取得出現最多、次多次的class name
        name_count = dict()
        for div in divs:
            class_name = div.get_attribute("class")
            if class_name not in name_count:
                name_count[class_name] = 1
            else:
                name_count[class_name] += 1
        sorted_names = sorted(name_count.items(), key=lambda item: item[1], reverse=True)
        categories = sorted_names[0][0] # 最多次的class name為category
        dropdown_btns = sorted_names[1][0] # 次多的class name為可下拉的category
        return categories, dropdown_btns

    def getEdge(self):
        return self.edge

if __name__=="__main__":
    start_url = "https://tw.carousell.com/categories/women-s-fashion-4/"
    urls = WebUrlFinder(start_url).getPageUrls()