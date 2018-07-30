import numpy as np
import pandas as pd
import xlrd
from string import digits

excel_name = "yimeijie.xlsx"
wb = xlrd.open_workbook(excel_name)
sheets_org = wb.sheet_names()
sheets = [0 for x in range(0, len(sheets))] 
for i in np.arange(len(sheets)):
    sheets[i] = sheets_org[i].strip()
print(sheets)