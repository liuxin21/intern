import tkinter as tk
import numpy as np
import pandas as pd
import xlrd
from string import digits

window = tk.Tk()
window.title('爱尼尔统计程序')
window.geometry('800x800')

canvas = tk.Canvas(window, height=50, width=500)#创建画布
image_file = tk.PhotoImage(file='inier.gif')#加载图片文件
image = canvas.create_image(250,0, anchor='n', image=image_file)#将图片置于画布上
canvas.pack(side='top')#放置画布（为上端）

tk.Label(window, text='请输入文件名:').place(x=50, y= 80)

var_excel_name = tk.StringVar()
var_excel_name.set('example.xls 或 example.xlsx')

entry_excel_name = tk.Entry(window, textvariable=var_excel_name)
entry_excel_name.place(x=170, y=80)

def print_excel_name():
    name = entry_excel_name.get()
    wb = xlrd.open_workbook(name)
    sheets = wb.sheet_names()
    for i in sheets:
        i = i.strip()
    t.insert(2.2, sheets)
    
btn_excel_name = tk.Button(window, text='查看表格', command=print_excel_name)
btn_excel_name.place(x=170, y=110)

t = tk.Text(window, height=6, width=110)
t.place(x=0, y=140)

tk.Label(window, text='表头在第几行:').place(x=50, y= 250)


window.mainloop()
