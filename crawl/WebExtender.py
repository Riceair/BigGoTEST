from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

class WebExtender:
    def __init__(self, is_all=False, open_time=3, extend_time=3):
        self.is_all = is_all
        self.open_time = open_time
        self.extend_time = extend_time
        options = Options()
        options.add_argument("--disable-popup-blocking")
        options.add_argument('--disable-default-apps')
        options.add_argument('--disable-notifications')
        self.edge = webdriver.Edge(options=options)
    
    # 將單一網頁延伸 (把顯示更多結果按完)
    def extend(self, url):
        self.edge.get(url)
        time.sleep(self.open_time)
        if self.is_all: # "最佳匹配"排序拿不到所有資料，改成"近期"排序拿的資料比較多
            self.__changeSort()

        while True:
            buttons = self.edge.find_elements(By.CSS_SELECTOR, "button")
            if buttons[-1].text == "顯示更多結果":
                buttons[-1].click()
                time.sleep(self.extend_time)
            else:
                break

    def extendTimes(self, url, times):
        self.edge.get(url)
        time.sleep(self.open_time)
        if self.is_all: # "最佳匹配"排序拿不到所有資料，改成"近期"排序拿的資料比較多
            self.__changeSort()

        for _ in range(times):
            buttons = self.edge.find_elements(By.CSS_SELECTOR, "button")
            btn_texts = [button.text for button in buttons]
            if "顯示更多結果" in btn_texts: # 不確定該按鈕是否一定出現在最後一個
                buttons[btn_texts.index("顯示更多結果")].click()
                time.sleep(self.extend_time)
            else:
                break

    # 改成用近期排序
    def __changeSort(self):
        sections = self.edge.find_elements(By.CSS_SELECTOR, "section")
        # 排序按鈕在這 (用class name抓不到，會噴錯)
        buttons = sections[2].find_elements(By.CSS_SELECTOR, "button")
        buttons[1].click()
        time.sleep(1)
        dropdown = self.edge.find_elements(By.CSS_SELECTOR, ".D_bck label") # 下拉式選單
        dropdown[1].click() # 使用近期排序
        time.sleep(2)

    def getPage(self):
        return self.edge.page_source

if __name__=="__main__":
    from ProductParser import ProductParser

    url = "https://tw.carousell.com/categories/women-s-fashion-4/"
    extender = WebExtender(is_all=True)
    # extender.extend(url)
    extender.extendTimes(url, 3)
    html_text = extender.getPage()

    parser = ProductParser()
    parser.recordNamePrice(html_text)
    print(parser.products[:5])
    print(len(parser.products))