import json
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class DocumentObject:
    def __init__(self, document_path):
        with open(document_path, 'r') as file:
            self.doc = json.load(file)
        self.__clean_keys()
        self.__reformat_desc()

    def __clean_keys(self):
        tmp = {}
        for key, value in self.doc.items():
            tmp[key.replace("_", " ")] = value
        self.doc = tmp

    def __reformat_desc(self):
        txt = self.doc["CURATORIAL DESCRIPTION"]
        transformed = re.sub(r'\n', '<br \\>', txt)
        transformed = re.sub(r'Keywords:[ ]*(<br \\\>)*', 'Keywords:', transformed)
        txt = txt.split('\n')
        self.doc["CURATORIAL DESCRIPTION"] = txt[0] +2*'<br \>'+txt[-1]
        
    def __str__(self):
        return str(self.doc)
    
    def getDoc(self):
        return self.doc

    def rewrite_string(input_string):
        # First, replace all occurrences of "\n" with "<br \\>"
        transformed = re.sub(r'\n', '<br \\>', input_string)
        # Now, handle the special case for "Keywords: <br \\>"
        transformed = re.sub(r'Keywords: <br \\\>', 'Keywords:', transformed)
        return transformed

