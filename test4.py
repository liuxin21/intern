import numpy as np
import pandas as pd
import xlrd
from string import digits

i = 4
excel_name = "yimeijie.xlsx"
wb = xlrd.open_workbook(excel_name)
sheets = wb.sheet_names()
df = pd.read_excel(excel_name, sheetname=sheets[i])
df.columns = df.iloc[0]
df.index = range(len(df))
df.drop([0], axis=0, inplace=True)
#df.dropna(subset=['楼盘名称'],inplace=True)
#df = df["楼盘名称","楼盘类型","媒体数量"]
print(df)