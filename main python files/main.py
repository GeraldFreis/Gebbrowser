"""Frameworks / Library imports"""
import tkinter as Tk
import tkinter.font as font
from tkinter import *

"""Modular imports"""
from colours import cream
from when_searched import WhenSearched


"""Setting up the main window"""
main_window = Tk()
main_window.geometry("1100x730+110+0")
main_window.config(bg="white")
main_window.title("Gebbrowser")


"""Fonts"""
large_font = font.Font(family="Gothic Medium", size=110)


"""Frames"""
left_frame = Frame(master=main_window,
bg=cream, width=200, height=1100).grid(row=1, column=1, rowspan=100, columnspan=20)

centre_frame = Frame(master=main_window,
bg="white").grid(row=1, column=21, rowspan=100, columnspan=80)


"""Labels and Buttons"""
# left frame
history_button = Button(master=left_frame,
text="History",
bg=cream).grid(row=4, column=1, columnspan=20)

# centre frame
Gebbrowser_label = Label(master=centre_frame,
text="Gebbrowser", font=large_font,
bg="white", anchor='center',
width=14, height=4).grid(row=1, column=22, rowspan=9, columnspan=50)

"""Search bar"""
search_text = StringVar()
search_label = Label(master=centre_frame, text="Enter URL",
bg="white", width=7).grid(row=5, rowspan=6, column=21, columnspan=10)
search_bar = Entry(master=centre_frame, textvariable=search_text,
width=70).grid(row=5, column=23, columnspan=79, rowspan=5)

def returningsearch():
    search = search_text.get()
    searchprotocol = WhenSearched(search)
    searchprotocol.widgets(url=search)
    searchprotocol.apply()

search_enter_button = Button(master=centre_frame, command=returningsearch,
bg="white", text="Enter Search", background="white", activebackground="white").grid(row=8, column=23, columnspan=79, rowspan=1)


main_window.mainloop()