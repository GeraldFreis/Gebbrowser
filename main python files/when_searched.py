"""Framework / Libraries importing"""
import tkinter as tk
import tkinter.font as font
from tkinter import *

"""Modular imports"""
from html_parser import HtmlParser

"""When searched is the protocol when a user searches a url"""
class WhenSearched():
    def __init__(self, search):
        # creating the main window and setting the title as the retrieved title in HtmlParser
        self.search_window = Tk()
        htmlparser = HtmlParser(search)
        self.search_title = htmlparser.returningtitle()
        self.search_window.title(self.search_title)
        self.search_window.geometry("900x600+210+0")
        self.search_window.config(bg="white")
    
    def widgets(self, url):
        """Foundational widgets"""
        # Url bar
        self.url_bar_text = StringVar()
        self.url_bar = Entry(master=self.search_window,
        textvariable=self.url_bar_text, width=35, text=url)

        def searchingurl():
            search = self.url_bar.get()
            htmlparser = HtmlParser(search)
            htmlparser.iterthroughfiles()
        
        self.url_bar_button = Button(master=self.search_window,
        text="Search Url", bg="white", command=searchingurl)

    def apply(self):
        """Foundational widgets"""
        self.url_bar.grid(row=2, column=21, columnspan=79, rowspan=10)
        self.url_bar_button.grid(row=2, column=80, columnspan=20)

        self.search_window.mainloop()

