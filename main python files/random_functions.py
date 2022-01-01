import tkinter as tk
import webbrowser as wb

def openingurl(url):
    used_url = url.strip('"')
    wb.open(url, new=1)