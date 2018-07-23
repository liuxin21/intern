import numpy as np 
import pandas as pd 

data = {"a":[2,3,4,5], "b":[3,4,5,6], "c":[4,5,6,7]}
df = pd.DataFrame(data)
print(df)
print(len(df) == df.shape[0])
print(range(1,len(df)+1))
df.index = range(1,len(df)+1)
print(df)
print(df["c"]>5)
df = df.loc[df["c"]>5, ["a","b"]]
print(df)