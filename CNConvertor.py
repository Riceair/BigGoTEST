import json

class CNConvertor:
    def __init__(self, path):
        self.table = json.load(open(path))

    def convert(self, text):
        for trad, simp in self.table.items():
            if trad in text:
                text = text.replace(trad, simp)
        return text

if __name__=="__main__":
    path = "CreateTable/ConversionTable.json"
    test = "翻譯測試: 只要功夫深，鐵杵磨成鏽花針、馬超、李小龍、超英趕美、作準、鐵杵磨成鏽花針"
    convertor = CNConvertor(path)
    print(convertor.convert(test))