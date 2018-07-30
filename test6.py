import tkinter as tk
import numpy as np
import pandas as pd
import xlrd
from string import digits

window = tk.Tk()
window.title('爱尼尔统计程序')
window.geometry('800x800')
##################################################################

canvas = tk.Canvas(window, height=50, width=500)#创建画布
image_file = tk.PhotoImage(file='inier.gif')#加载图片文件
image = canvas.create_image(250,0, anchor='n', image=image_file)#将图片置于画布上
canvas.pack(side='top')#放置画布（为上端）
##################################################################

tk.Label(window, text='请输入文件名:').place(x=50, y= 80)
tk.Label(window, text='(如果不能输入中文请粘贴excel文件名)').place(x=380, y= 80)

var_excel_name = tk.StringVar()
var_excel_name.set('例如：yimeijie.xlsx')

entry_excel_name = tk.Entry(window, textvariable=var_excel_name)
entry_excel_name.place(x=170, y=80)

def print_city_name():
    global excel_name, sheets_org, sheets
    excel_name = entry_excel_name.get()
    wb = xlrd.open_workbook(excel_name)
    sheets_org = wb.sheet_names()
    sheets = [0 for x in range(0, len(sheets_org))] 
    for i in np.arange(len(sheets)):
        sheets[i] = sheets_org[i].strip()
    t1.insert("end", sheets)
    
btn_excel_name = tk.Button(window, text='确定并查看城市名称', command=print_city_name)
btn_excel_name.place(x=170, y=120)

t1 = tk.Text(window, height=6, width=80)
t1.place(x=50, y=160)
##################################################################

tk.Label(window, text='输入你想查看的城市:').place(x=50, y=280)
var_city_name = tk.StringVar()
var_city_name.set('例如：北京')
entry_city_name = tk.Entry(window, textvariable=var_city_name)
entry_city_name.place(x=200, y=280)

def print_one_city():
    global df
    city_name = var_city_name.get()
    index = sheets.index(city_name)
    df = pd.read_excel(excel_name, sheetname=sheets_org[index])
    print(df.head())
    
btn_city = tk.Button(window, text='确定并查看该城市', command=print_one_city)
btn_city.place(x=170, y=320)

t2 = tk.Text(window, height=6, width=80)
t2.place(x=50, y=360)
##################################################################

p1 = 320
tk.Label(window, text='表头在第几行:').place(x=50, y= p1)
var_f = tk.IntVar()
tk.Radiobutton(window, text='1',variable=var_f, value=1).place(x=200, y= p1)
tk.Radiobutton(window, text='2',variable=var_f, value=2).place(x=250, y= p1)
tk.Radiobutton(window, text='3',variable=var_f, value=3).place(x=300, y= p1)
tk.Radiobutton(window, text='4',variable=var_f, value=4).place(x=350, y= p1)
#################################################################

def head():
    pass
    #print(df.iloc[var_f.get()-2])
tk.Button(window, text='查看表头', command=head).place(x=50, y=320)
#################################################################


tk.Label(window, text='输入你想查看的列:').place(x=50, y= 320)

def example():
    i = 4
    excel_name = var_excel_name.get()
    wb = xlrd.open_workbook(excel_name)
    sheets = wb.sheet_names()
    df = pd.read_excel(excel_name, sheetname=sheets[i])
    df.columns = df.iloc[var_f.get()-2]
    df.index = range(len(df))
    df.drop([var_f.get()-2], axis=0, inplace=True)
    df.dropna(subset=['楼盘名称'],inplace=True)
    df = df[["楼盘名称","楼盘类型","媒体数量"]]
    t2.insert("end", df)

btn_example = tk.Button(window, text='查看所填城市', command=example)
btn_example.place(x=170, y=400)

t2 = tk.Text(window, height=20, width=80)
t2.place(x=50, y=440)





window.mainloop()