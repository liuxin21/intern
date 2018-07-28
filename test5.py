import tkinter as tk
import numpy as np
import pandas as pd
import xlrd
from string import digits


name = "yimeijie.xlsx"
wb = xlrd.open_workbook(name)
sheets = wb.sheet_names()

