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
    excel_name = entry_excel_name.get()
    wb = xlrd.open_workbook(excel_name)
    sheets = wb.sheet_names()
    for i in np.arange(len(sheets)):
        sheets[i] = sheets[i].strip()
    t.insert(2.2, sheets)
    
btn_excel_name = tk.Button(window, text='查看城市名称', command=print_excel_name)
btn_excel_name.place(x=600, y=80)

t = tk.Text(window, height=6, width=80)
t.place(x=50, y=140)

##################################################################
#l = tk.Label(window, bg='yellow', width=20, text='empty')
#l.place(x=50, y= 300)

def first_row():
    # l.config(text='表头在第' + np.str(var.get()) + "行")
    f = var.get()

tk.Label(window, text='表头在第几行:').place(x=50, y= 250)
var = tk.IntVar()
r1 = tk.Radiobutton(window, text='1',
                    variable=var, value=1,
                    command=first_row)
r1.place(x=200, y= 250)
r2 = tk.Radiobutton(window, text='2',
                    variable=var, value=2,
                    command=first_row)
r2.place(x=250, y= 250)
r3 = tk.Radiobutton(window, text='3',
                    variable=var, value=3,
                    command=first_row)
r3.place(x=300, y= 250)
r4 = tk.Radiobutton(window, text='4',
                    variable=var, value=4,
                    command=first_row)
r4.place(x=350, y= 250)
#################################################################
def example():
    i = 4
    excel_name = entry_excel_name.get()
    wb = xlrd.open_workbook(excel_name)
    sheets = wb.sheet_names()
    df = pd.read_excel(excel_name, sheetname=sheets[i])
    t1.insert(2.2, df)
#df.columns = df.iloc[0]
#df.index = range(len(df))
#df.drop([0], axis=0, inplace=True)
#df.dropna(subset=['楼盘名称'],inplace=True)
btn_example = tk.Button(window, text='查看其中一个城市', command=example)
btn_excel_name.place(x=170, y=260)

t1 = tk.Text(window, height=20, width=80)
t1.place(x=50, y=350)


window.mainloop()
