from re import X
import pandas as pd 
import matplotlib.pyplot as plt

url = "https://info.usd-cny.com/wti/lishi.htm"

table = pd.read_html(url)
df = pd.DataFrame(table[0]).set_index("年份")

del_head = lambda x : float(x[1:])
del_tail = lambda x : float(x[:-1])

#print(df.columns)
df.loc[:,["最低价","最高价"]] = df.loc[:,["最低价","最高价"]].apply(del_head)


'''
df["最低价"] = df["最低价"].apply(del_head)
df["平均价"] = df["平均价"].apply(del_head)
df["最高价"] = df["最高价"].apply(del_head)
df["年幅度"] = df["年幅度"].apply(del_tail)
'''
print(df.head())

