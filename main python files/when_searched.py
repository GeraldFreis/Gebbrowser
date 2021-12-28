"""Framework / Libraries importing"""
import tkinter as tk
import tkinter.font as font
from tkinter import *

"""Modular imports"""
from html_parser import HtmlParser

"""When searched is the protocol when a user searches a url"""
class WhenSearched():
    def __init__(self, search):
        self.search_window = Tk()
        htmlparser = HtmlParser(search)
        self.search_title = htmlparser.findingtitle()
        self.search_window.title(self.search_title)
        self.search_window.geometry("900x600+210+0")
        self.search_window.config(bg="white")

    def apply(self):
        self.search_window.mainloop()

