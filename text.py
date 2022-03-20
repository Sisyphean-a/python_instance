import pandas as pd 
import matplotlib.pyplot as plt

url = "https://info.usd-cny.com/wti/lishi.htm"

table = pd.read_html(url)
df = pd.DataFrame(table[0]).set_index("年份")

del_head = lambda x : float(x[1:])
del_tail = lambda x : float(x[:-1])

df["最低价"] = df["最低价"].apply(del_head)
df["平均价"] = df["平均价"].apply(del_head)
df["最高价"] = df["最高价"].apply(del_head)
df["年幅度"] = df["年幅度"].apply(del_tail)

amplitude_location = lambda x : x>0
location_mean_value = lambda x : 80>x>=50

df = df.loc[df.年幅度.apply(amplitude_location)] \
      .loc[df["平均价"].apply(location_mean_value)]

print(df)

#print(type(df["年幅度"][1]))