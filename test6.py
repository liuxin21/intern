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
tk.Label(window, text='(如果不能输入中文请粘贴excel文件名)').place(x=380, y= 80)

var_excel_name = tk.StringVar()
var_excel_name.set('example.xls 或 example.xlsx')

entry_excel_name = tk.Entry(window, textvariable=var_excel_name)
entry_excel_name.place(x=170, y=80)

def print_excel_name():
    excel_name = entry_excel_name.get()
    wb = xlrd.open_workbook(excel_name)
    sheets = wb.sheet_names()
    for i in np.arange(len(sheets)):
        sheets[i] = sheets[i].strip()
    t1.insert("end", sheets)
    
btn_excel_name = tk.Button(window, text='查看城市名称', command=print_excel_name)
btn_excel_name.place(x=170, y=120)

t1 = tk.Text(window, height=6, width=80)
t1.place(x=50, y=160)
##################################################################

tk.Label(window, text='表头在第几行:').place(x=50, y= 280)
var_f = tk.IntVar()
tk.Radiobutton(window, text='1',variable=var_f, value=1).place(x=200, y= 280)
tk.Radiobutton(window, text='2',variable=var_f, value=2).place(x=250, y= 280)
tk.Radiobutton(window, text='3',variable=var_f, value=3).place(x=300, y= 280)
tk.Radiobutton(window, text='4',variable=var_f, value=4).place(x=350, y= 280)
#################################################################

def example():
    i = 4
    excel_name = var_excel_name.get()
    wb = xlrd.open_workbook(excel_name)
    sheets = wb.sheet_names()
    df = pd.read_excel(excel_name, sheetname=sheets[i])
    t2.insert("end", df)
    df.columns = df.iloc[var_f.get()-2]
    df.index = range(len(df))
    df.drop([var_f.get()-2], axis=0, inplace=True)
    df.dropna(subset=['楼盘名称'],inplace=True)
    df = df["楼盘名称","楼盘类型","媒体数量"]

btn_example = tk.Button(window, text='查看其中一个城市', command=example)
btn_example.place(x=170, y=320)

t2 = tk.Text(window, height=20, width=80)
t2.place(x=50, y=350)





window.mainloop()