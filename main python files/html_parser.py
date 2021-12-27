
from os import defpath, write
from typing import Literal
import urllib
from urllib.request import urlopen
try:
    from bs4 import BeautifulSoup
except Exception:
    pass

"""Globals"""
base_url = "http://www.blankwebsite.com/"
google_url = "https://www.google.com"

class UrlParser():
    def __init__(self, urltoparse):
        self.url_to_parse = urltoparse
    
    def contenttofile(self):
        with urlopen(self.url_to_parse) as f:
            text = str(f.read())
            temptext = open("urltext.html", "w")
            temptext.write(text)
    
    def findingtitle(self):
        temp_html_file = open("urltext.html", "r")
        line_spacer_1 = r'<'
        line_spacer_2 = r'>'
        content_list = list()
        for line in temp_html_file: 
            if line_spacer_1 and line_spacer_2 in line:
                content_list.append(line.split(line_spacer_1))
            
    
    def findingtitle2(self):
        """Setting up the doc and making it prettier"""
        html_doc = open("urltext.html", "r")
        soup = BeautifulSoup(html_doc, 'html.parser')
        html_doc_write = open("urltext.html", "w")
        html_doc_write.write(soup.prettify())

        # print(soup.prettify())
        
        # if "<TITLE>" in content_list:
        #     print(content_list)

def urlparser_compiled():
    urlparser = UrlParser(google_url)
    urlparser.contenttofile()
    urlparser.findingtitle2()

urlparser_compiled()


