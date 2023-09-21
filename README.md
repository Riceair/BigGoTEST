# BigGoTEST
BigGo Python工程師 筆試題目

## Problem 1
### 繁體轉簡體 Table 建立
在 CreateTable 資料夾中  
1_PHPTable2py.py 將 ZhConversion.php 轉成 ZhConversion.py  
2_CreateTable.py 將使用的 table 合併成一個大 table (存成ConversionTable.json)  
使用 CNConvertor 類別將繁體轉簡體  

### 爬蟲
在 crawl 資料夾中  
WebUrlFinder.py 找到商品類別的網頁連結 (多個頁面連結)  
WebExtender.py 改變排序方式 (預設排序方式不會顯示所有資料) 、 將商品頁展開 (將"顯示更多結果"按鈕按到不出現)  
ProductParser.py 解析網頁中的商品名稱、價格

### Demo
Problem1.py 跑所有內容  
Problem1_demo.py 跑5個網頁，且每個網頁只按3次"顯示更多結果"  

## Problem 2
### Thread
使用 Event 方式呼叫其他 thread 執行  