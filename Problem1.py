from crawl.WebUrlFinder import WebUrlFinder
from crawl.WebExtender import WebExtender
from crawl.ProductParser import ProductParser
from CNConvertor import CNConvertor
from pathlib import Path
import os

start_url = "https://tw.carousell.com/categories/women-s-fashion-4/"
table_path = "CreateTable/ConversionTable.json"
save_path = "products.csv"
# 取得要爬的所有網站
finder = WebUrlFinder(start_url)
urls = finder.getPageUrls(is_sub_cate=True) # 使用子類別 (example: 手機及配件的對講機)
edge = finder.getEdge()

# 類別宣告
extender = WebExtender(edge, is_sort=True, open_time=3, extend_time=3) # 功能: 用來把"顯示更多結果"按鈕按完 is_sort會改變排序(預設排序無法顯示所有產品)
parser = ProductParser() # 功能: 解析產品名稱與價格
convertor = CNConvertor(table_path) # 功能: 繁體中文轉簡體中文

# 建立紀錄檔
if Path(save_path).is_file(): # 檢查檔案是否存在
    # 如果存在，刪除該檔案
    os.remove(save_path)

# 開始抓所有資料
products = set() # 紀錄所有產品 (用set去除重複的商品)
for url in urls:
    extender.extend(url) # 展開網頁
    html_text = extender.getPage() # 取得展開後的html
    parser.recordNamePrice(html_text) # 紀錄名稱與價格
    parsed_products = parser.getProducts() # 取得名稱與價格
    
    # 將取得的產品紀錄
    for name, price in parsed_products:
        products.add((convertor.convert(name), price)) # 紀錄，並將商品繁體中文轉簡體中文
    parser.clear() # 解析器清空 (可不用做)

    # 儲存當前結果
    with open(save_path, "w", encoding='UTF-8') as f:
        f.write("name, product,\n")
        for product in products:
            f.write(f"{product[0]}, {product[1]}\n")