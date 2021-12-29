# Gebbrowser
Webbrowser but my name is Gerald

// Dependencies: 
tkinter, tkinter.font, os, urllib, beautiful soup, sqlite3

This will be my first prototype of a webbrowser in its entirety
I will be initially focusing on the UI element but a simple UI
* UI to date will be a left frame taking up 1/5th of the screen, and then a central frame that is idle with a searchbar
* UI is minimalistic as there's no point crowding the user

Current main UI
![image](https://user-images.githubusercontent.com/91832029/147658146-386227b3-4a95-4425-b813-054fe99d1cb1.png)


// Update
I am now onto focusing on the parsing of the html side of this webbrowser in the html parser document
* To do this I am using urllib to retrieve the html, and then producing a html text
* Beautiful soup is then used to extract the title, and "prettify" the code
* After this, I institute a iterative function that catelogs the html into legible sub lists consisting of ["tag", "whether arguments exist", "arguments if exist"]
* This function returns a main list with the sub lists of all html, embedded css and embedded javascript

// Update
Now I am focusing on displaying these html commands through the production of a html rendering module
* In this module I link elements of the list generated previously to their concurrent tkinter commands
* I am ignoring the css and javascript elements of the list as I will produce css and javascript parsing and rendering modules later
*   First I want to get the html barebones into a tkinter based UI
* To link the commands I will be using an absurd amount of conditional statements and lists will be produced alongside these statements
* I will then use a for loop to display all of the commands, with the commands being retrieved iteratively from the aforementioned lists of commands
