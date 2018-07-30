import tkinter as tk
import numpy as np
import pandas as pd
import xlrd
from string import digits


def changeStringvar1():
    #global a
    global b,c
    a.set("1")
    print(a.get()) ## 在这print a.get()就能打印在控制台里面了
    b = np.array([1,2,3])
    c = 3
def changeStringvar2():
    #global a
    a.set("2")
    print(a.get()) ## 在这print a.get()就能打印在控制台里面了
def show():
    print(a.get())
    print(b)
    print(c)
    
root=tk.Tk()
a=tk.StringVar()
button1=tk.Button(root,text='Change1',command=changeStringvar1)
#label=tk.Label(root,textvariable=a)
button1.pack()
#label.pack()
#print(a.get()) ##　这个时候打印出来的还没变化呢
button2=tk.Button(root,text='Change2',command=changeStringvar2)
button2.pack()
button3 = tk.Button(root,text="show",command=show)
button3.pack()

tk.mainloop()