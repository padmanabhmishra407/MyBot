# from Main import main
from Main import main


import Main
import tkinter as tk
from tkinter import Canvas, filedialog, Text
import os, sys
from subprocess import *
import time

root = tk.Tk()

# def Open():
#     def OpenMain():
#         main
#     return OpenMain

# OpenMain = Open()
    # Popen('python -u "d:\Projects\MyBot\main.py')


    # filename= (r"D:\Projects\MyBot\main.py")

# def OpenMain():
#     Popen('python -u "d:\Projects\MyBot\Nain.py"')
#     time.sleep(5)


def new_func():
    def ExitMain():
        sys.exit(r"D:\Projects\MyBot\main.py")
    return ExitMain

ExitMain = new_func()


canvas = tk.Canvas(root, height=500, width=500)
canvas.pack()

frame = tk.Frame(root, bg="red", bd=5)
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

background_image= tk.PhotoImage(file="Hey.png")
background_label= tk.Label(frame, image=background_image)
background_label.place(relheight=1,relwidth=1)



RunBot = tk.Button(frame, text="Run Bot", padx=10, 
                    pady=5, fg="red", bg="black" ,command=main)
RunBot.place(relheight=0.05,relwidth=0.15,relx=0.10,rely=0.95)

ExitBot = tk.Button(frame, text="Exit Bot", padx=10, 
                    pady=5, fg="red", bg="black",command=ExitMain)
ExitBot.place(relheight=0.05,relwidth=0.15,relx=0.75,rely=0.95)

root.mainloop()
