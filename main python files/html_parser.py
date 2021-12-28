
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

"""Parser to find the main html elements"""
class HtmlParser():
    def __init__(self, urltoparse):
        self.url_to_parse = urltoparse

        with urlopen(self.url_to_parse) as f:

            self.text = str(f.read())
            self.temptext = open("urltext.html", "w")
            self.temptext.write(self.text)
            self.temptext.close()

            self.html_doc = open("urltext.html", "r")
            self.soup = BeautifulSoup(self.html_doc, 'html.parser')
            self.html_doc_write = open("urltext.html", "w")
            self.html_doc_write.write(self.soup.prettify())

            """Iterating through the html doc and printing it to a temporary text file, once text file exists it is iterated through and produces a """
            self.temporary_text_file_writeable = open("temphtml.txt", "w")
            self.temporary_text_file_writeable.write(self.soup.prettify())


        self.temporary_text_file_readable = open("temphtml.txt", "r")
        self.html_doc.close()
        self.html_doc_write.close()
        self.temporary_text_file_writeable.close()
        self.temporary_text_file_readable.close()
        


    def findingtitle(self):
        """Returning the title"""
        return self.soup.title.string

    def findingtext(self):
        """Returning text"""
        return self.soup.text
    
    def itertofindandlistcomponents(self):
        doc = open("temphtml.txt", "r")
        for row in doc:
            if "<body" in row:
                print(row)
            else:
                pass
htmlparser = HtmlParser(base_url)
htmlparser.itertofindandlistcomponents()
