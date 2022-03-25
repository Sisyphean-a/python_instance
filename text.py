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

df.sort_values(by="平均价",inplace=True,ascending=False)


df.plot(y=["平均价","最高价"],
    kind="bar",
    color=["red","orange"],
    title="US油价",
    rot=60)

plt.title("us油价",fontsize=18,fontweight="bold")

plt.xlabel("年份",fontweight="bold")
plt.ylabel("价格",fontweight="bold")

plt.show()
