# BigGoTEST
BigGo Python工程師 筆試題目  

# 結果
筆試結果: 通過  
面試結果: 不通過  
面試總結: 1. 公司不缺人 2. 在不知道能不能進公司前就被要求要會LLM等AI模型 3. 論文內容沒有創新 4. 沒有長期計畫  

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
Problem1_demo.py 跑3個網頁，且每個網頁只按2次"顯示更多結果"  
結果會儲存為csv檔  
demo 影片連結: https://youtu.be/kUxyFUVyYxU  

## Problem 2
### Thread
使用 Event 方式呼叫其他 thread 執行  

### Demo
demo 影片連結: https://youtu.be/nJ2SiJF5I-A  