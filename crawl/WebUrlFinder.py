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
        self.urls = []

    def getPageUrls(self, is_sub_cate=True):
        self.edge.get(self.root_url)
        time.sleep(2)
        category_class, dropdown_class = self.__getCateClassName()
        
        # 取得類別的連結
        categories = self.edge.find_elements(By.CLASS_NAME, category_class)[1:] # 去除"追蹤的賣家商品"
        for cate in categories:
            self.urls.append(cate.find_element(By.TAG_NAME, "a").get_attribute("href"))

        # 取得子類別的連結
        if is_sub_cate:
            dropdown_btns = self.edge.find_elements(By.CLASS_NAME, dropdown_class)
            for button in dropdown_btns:
                self.urls += self.__getSubCateUrl(button)
        return self.urls
    
    def __openAll(self):
        buttons = self.edge.find_elements(By.CSS_SELECTOR, "button")
        for button in buttons:
            if button.text == "所有分類":
                button.click()
                time.sleep(1)
                break      

    def __getCateClassName(self):
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
        category_class = sorted_names[0][0] # 最多次的class name為category
        dropdown_class = sorted_names[1][0] # 次多的class name為可下拉的category
        return category_class, dropdown_class

    def __getSubCateUrl(self, click_element):
        href_before_click = self.edge.find_elements(By.TAG_NAME, "a")
        click_element.click()
        hrefs = self.edge.find_elements(By.TAG_NAME, "a")
        for a in href_before_click:
            if a in hrefs:
                hrefs.remove(a)
        return [href.get_attribute("href") for href in hrefs]

    def getEdge(self):
        return self.edge

if __name__=="__main__":
    start_url = "https://tw.carousell.com/categories/women-s-fashion-4/"
    urls = WebUrlFinder(start_url).getPageUrls()
    print(urls[:2], len(urls))