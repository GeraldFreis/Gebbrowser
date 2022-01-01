"""Library / Framework importing"""
import tkinter as tk
from tkinter import *

"""Modular imports"""
from html_parser import HtmlParser, returninghtmllist
from html_linked_commands import *

class HtmlRenderer():
    def __init__(self, mainwindow, searchedurl):
        self.rendering_window = mainwindow

        self.html_parser = HtmlParser(searchedurl)  # this is arbitrary as it is already run in the when_searched module

        self.html_list = returninghtmllist()

        self.row_number = 0

    def linking_commands(self):

        for items in self.html_list:

            self.row_number += 1

            if items[0] == "<a ":
                atagwithargs(self.rendering_window, items[2], self.row_number)
            
            elif items[0] == "<address ":
                addresswithargs(self.rendering_window, items[2], self.row_number)
        
        self.rendering_window.mainloop()


main_window = tk.Tk()
main_window.geometry("900x600+210+0")
main_window.config(bg="white")

html_render = HtmlRenderer(main_window, "https://www.google.com")
html_render.linking_commands()