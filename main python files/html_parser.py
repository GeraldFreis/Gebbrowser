
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

"""Parser to find the main text elements"""
class UrlParser():
    def __init__(self, urltoparse):
        self.url_to_parse = urltoparse
    
    def contenttofile(self):
        with urlopen(self.url_to_parse) as f:

            self.text = str(f.read())
            self.temptext = open("urltext.html", "w")
            self.temptext.write(self.text)
            self.temptext.close()

            self.html_doc = open("urltext.html", "r")
            self.soup = BeautifulSoup(self.html_doc, 'html.parser')
            self.html_doc_write = open("urltext.html", "w")
            self.html_doc_write.write(self.soup.prettify())

    def findingtitle(self):
        """Returning the title"""
        self.page_title = self.soup.title.string
        print(self.page_title)
    
    def findingtext(self):
        self.textvars = self.soup.text
        print(self.textvars)

def urlparser_compiled():
    urlparser = UrlParser(base_url)
    urlparser.contenttofile()
    urlparser.findingtitle()
    urlparser.findingtext()

urlparser_compiled()


