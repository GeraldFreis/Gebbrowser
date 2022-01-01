import tkinter as tk
from tkinter import *

"""Modular imports"""
from random_functions import openingurl
"""Functions"""

# html tags with arguments
def atagwithargs(window, contents, rownumber):
    individual_contents = contents.split()
    for elements in individual_contents:
        if "href=" in elements:
            stripped = elements.strip(">")
            stripped_2 = stripped.strip("href=")
            new = stripped_2.strip('"')
            def quickfix():
                openingurl(new)
                print(new)
            Button(master=window, command=quickfix).grid(row=rownumber, column=40)
        else:
            pass
    # Label(master=window, text=contents).grid(row=rownumber, column=20)

def addresswithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def areatagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def articletagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def asidetagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def audiotagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def btagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def basetagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def bbtagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def bdotagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def blockquotetagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def bodytagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def brslashtagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def buttontagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def canvastagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def captiontagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def citetagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def codetagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def coltagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def colgrouptagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def commandtagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def datagridtagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def datalisttagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def ddtagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def deltagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def detailstagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def dfntagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def dialogtagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def dirtagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def divtagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def dltagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def dttagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def emtagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def embedtagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def eventsourcetagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def fieldsettagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def figcaptiontagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def figuretagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def footertagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def formtagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def h1tagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def h2tagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def h3tagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def h4tagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def h5tagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def h6tagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def headtagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def headertagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def hgrouptagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def hrslashtagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def htmltagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def itagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def iframetagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def imgtagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def inputtagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def instagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def kbdtagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def keygentagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def labeltagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def legendtagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def litagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def linktagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def maptagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def marktagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def menutagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def metatagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def metertagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def navtagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def noscripttagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def objecttagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def oltagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def optgrouptagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def optiontagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def ptagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def paramtagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def pretagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def progresstagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def qtagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def rptagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def rttagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def rubytagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def stagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def samptagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def scripttagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def sectiontagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def smalltagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def sourcetagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def spantagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def strongtagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def styletagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def subtagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def suptagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def tabletagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def tbodytagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def tdtagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def textareatagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def tfoottagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def thtagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def theadtagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def timetagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def titletagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def trtagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def tracktagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def utagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def ultagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def vartagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def videotagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)

def wbrtagwithargs(window, contents, rownumber):
    Label(master=window, text=contents).grid(row=rownumber, column=40)
