# Convert the Python table to several tables to be used by the method
'''
zh2Hant => (Generic Terms) Simplified Chinese to Traditional Chinese.
zh2Hans => (Generic Terms) Traditional Chinese to Simplified Chinese.
zh2TW => (Tech/IT/Country-Terms) Simplified Chinese to Taiwan::Traditional Chinese.
[not use] zh2HK => (Tech/IT/Country-Terms) Simplified Chinese to Hong Kong::Traditional Chinese.
zh2CN => (Tech/IT/Country-Terms) Traditional Chinese to China::Simplified Chinese.
'''
from ZhConversion import *
import json

# 簡繁對調
zh2Hant = {v:k for k, v in zh2Hant.items()}
zh2TW = {v:k for k, v in zh2TW.items()}

# Merge all tables to one
dict_list = [zh2Hant, zh2Hans, zh2TW, zh2CN]
big_table = dict()
for table in dict_list:
    for key, value in table.items():
        big_table[key] = value

# 依照文字長度排序 (由長到短)
big_table = dict(sorted(big_table.items(), key=lambda x: len(x[0]), reverse=True))
json.dump(big_table, open("ConversionTable.json", "w"))

# 讀檔測試
data = json.load(open("ConversionTable.json"))
print(data)