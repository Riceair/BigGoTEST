# Convert the original PHP table to Python table (dictionary)
class PHPTable2py():
    def __init__(self, path, save_path):
        self.path = path
        self.save_path = save_path
        self.isProcess = False
        self.convert_tokens = []
        self.token = ""

    def run(self):
        file = open("ZhConversion.php","r", encoding="utf-8")
        for line in file.readlines():
            if self.isProcess:
                if "]" in line: # Get end symbol
                    self.convert_tokens.append(self.token+"}\n\n")
                    self.__reset()
                    continue
                self.token += line.replace("=>", ":") # replace to Python dict format

            else: # Not in processing stage
                if "[" in line: # find start symbol
                    self.isProcess = True
                    terms = line.split(" ")
                    var_name = self.__getVarName(terms)
                    self.token += var_name+" = {\n"
        file.close()

        file = open(self.save_path, "w", encoding="utf-8")
        for token in self.convert_tokens:
            file.write(token)
        file.close()

    def __getVarName(self, terms):
        # terms = ['', 'public', 'static', '$var_name', '=', '[\n'] -> want to get var_name
        var_name = ""
        for term in terms:
            if "$" in term:
                var_name = term.replace("$", "")
                return var_name

    def __reset(self): # Reset stage and token
        self.isProcess = False
        self.token = ""

if __name__=="__main__":
    processor = PHPTable2py("ZhConversion.php", "ZhConversion.py")
    processor.run()