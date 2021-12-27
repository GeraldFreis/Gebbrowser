"""Frameworks / Library imports"""
import tkinter as Tk
import tkinter.font as font
from tkinter import *

"""Modular imports"""
from colours import cream


"""Setting up the main window"""
main_window = Tk()
main_window.geometry("1100x730+110+0")
main_window.config(bg="white")
main_window.title("Gebbrowser")


"""Fonts"""
large_font = font.Font(family="Gothic Medium", size=100)


"""Frames"""
left_frame = Frame(master=main_window,
bg=cream, width=200, height=1100).grid(row=1, column=1, rowspan=10)

centre_frame = Frame(master=main_window,
bg="white").grid(row=1, column=2, rowspan=10, columnspan=8)


"""Labels and Buttons"""
# left frame
history_button = Button(master=left_frame,
text="History",
bg=cream).grid(row=4, column=1)

# centre frame
Gebbrowser_label = Label(master=centre_frame,
text="Gebbrowser", font=large_font,
bg="white", anchor='center').grid(row=2, column=4, rowspan=3, columnspan=4)

"""Search bar"""
search_bar = Entry(master=centre_frame)


main_window.mainloop()