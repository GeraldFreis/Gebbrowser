"""Library / Framework importing"""
import tkinter as tk
from tkinter import *

"""Modular imports"""
from html_parser import HtmlParser, returninghtmllist


"""Functions"""
def atagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def atagwithoutargs(window, contents, rownumber):
    print('flip')

class HtmlRenderer():
    def __init__(self, mainwindow, searchedurl):
        self.rendering_window = mainwindow

        self.html_parser = HtmlParser(searchedurl)

        self.html_list = returninghtmllist()

    def linking_commands(self):
        for items in self.html_list:
            print(items)

