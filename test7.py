import tkinter as tk
import numpy as np
import pandas as pd
import xlrd
from string import digits

window = tk.Tk()
window.title('爱尼尔统计程序')
window.geometry('680x800')
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
tk.Label(window, text='(一次只能查看一个城市)').place(x=410, y= 280)
var_city_name = tk.StringVar()
var_city_name.set('例如：北京')
entry_city_name = tk.Entry(window, textvariable=var_city_name)
entry_city_name.place(x=200, y=280)

tk.Label(window, text='输入你想查看的列:').place(x=50, y= 320)
tk.Label(window, text='(以逗号隔开)').place(x=410, y= 320)
var_column_name = tk.StringVar()
var_column_name.set('例如：楼盘名称,楼盘类型,媒体数量')
entry_column_name = tk.Entry(window, textvariable=var_column_name)
entry_column_name.place(x=200, y=320)


def print_one_city():
    global city_name,df
    city_name = var_city_name.get()
    index = sheets.index(city_name)
    df = pd.read_excel(excel_name, sheetname=sheets_org[index])
    df.columns = df.iloc[0]
    df.index = range(len(df))
    df.drop([0], axis=0, inplace=True)
    df.dropna(subset=['楼盘名称'],inplace=True)
    df = df[["楼盘名称","楼盘类型","媒体数量"]]
    t2.insert("end", df)
    
btn_city = tk.Button(window, text='确定并查看该城市', command=print_one_city)
btn_city.place(x=200, y=360)

t2 = tk.Text(window, height=10, width=80)
t2.place(x=50, y=400)
##################################################################
def del_location(x):
    x = x.translate(str.maketrans('', '', digits))
    x = x.translate(str.maketrans('东西南北进出左右', '无无无无无无无无'))
    return x

def print_result():
    df["媒体数量"] = df["媒体数量"].astype("float")
    sl = df["媒体数量"].sum()
    data = df[["楼盘名称","楼盘类型"]]
    data["楼盘名称"] = data["楼盘名称"].astype("str")
    data["楼盘类型"] = data["楼盘类型"].astype("str")
    data = data.applymap(del_location).drop_duplicates(subset="楼盘名称", keep='first')
    sq = len(data)
    data_a = data.loc[data["楼盘类型"].str.contains("写字楼")]
    data_b = data.loc[data["楼盘类型"].str.contains("商业")]
    data_c = data.loc[data["楼盘类型"].str.contains("商务楼")]
    data_d = data.loc[data["楼盘类型"].str.contains("办公楼")]
    data_e = data.loc[data["楼盘类型"].str.contains("大厦")]
    data_f = data.loc[data["楼盘类型"].str.contains("laza")]
    xzl = pd.concat([data_a,data_b,data_c,data_d,data_e,data_f], axis=0).shape[0]
    t3.insert("end", [city_name,"社区:",sq,"媒体数量:",np.int(sl),"写字楼:",xzl])

tk.Button(window, text='合并社区并计算', command=print_result).place(x=50, y=580)
t3 = tk.Text(window, height=1, width=55)
t3.place(x=200, y=580)
##################################################################

window.mainloop()