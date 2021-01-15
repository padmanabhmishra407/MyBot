
import tkinter as tk
from tkinter import Canvas, filedialog, Text
import os, sys
from subprocess import *
import time

root = tk.Tk()
def OpenMain():
    Popen('python -u "d:\Projects\MyBot\main.py')
    time.sleep(5)

    # filename= (r"D:\Projects\MyBot\main.py")
def ExitMain():
    sys.exit(r"D:\Projects\MyBot\main.py")


canvas = tk.Canvas(root, height=700, width=700, bg="black")
canvas.pack()


frame = tk.Frame(root, bg="red")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

RunBot = tk.Button(root, text="Run Bot", padx=10, 
                    pady=5, fg="red", bg="black" ,command= OpenMain)
RunBot.pack()



ExitBot = tk.Button(root, text="Exit Bot", padx=10, 
                    pady=5, fg="red", bg="black",command=ExitMain)
ExitBot.pack()

root.mainloop()
