"""Library / Framework importing"""
import tkinter as tk
from tkinter import *

"""Modular imports"""
from html_parser import HtmlParser

class HtmlRenderer():
    def __init__(self, mainwindow, searchedurl):
        self.rendering_window = mainwindow

        self.html_parser = HtmlParser(searchedurl)

        self.html_list = self.html_parser.iterthroughfiles()

    def linking_commands(self):
        for items in self.html_list:
            print(items)

