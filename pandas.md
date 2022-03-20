安装pandas库

```shell
sudo pip3 install pandas
```

## 基础

### 库与数据帧

```python
# 导入pandas库
import pandas as pd

# DataFrame()：生成一个数据帧，数据帧是最小的数据集，二维数组
df = pd.DataFrame({"id":[1,2,3] , 			# 第一列数据
                   "name":["i","o","u"]})	# 第二列数据

# set_index()：设置索引；如果不自己设置索引的话，pandas会在开头一列加个索引
df = df.set_index("id",
                  inplace=False)	# 若为True，则在当前DataFrame上进行操作
```

### excel的导入与导出

```python
# to_excel()：表示把数据帧转换为excel导出
df.to_excel("./pandas.xlsx",	# 提供文件路径，这里使用了相对路径
            index_col="id")		# 设置索引列，可以为空，防止自动生成索引

# read_excel()：读取excel文件。
# header如果设置为None，则需要手动设置columns，否则自动生成数字
people = pd.read_excel("./pandas.xlsx", # 读取路径
                       header=0,		# 设置初始行作为列名，默认0
                       skiprows=0,		# 需要忽略或者跳过的行号列表，从0开始
                       usecols="A:C,D",	# 设置需要读取的数据子集，可以是列号
                       dtype={"ID":str}	# 设置某列的类型，否则空会设置为NaN，浮点型
                       index_col="ID")	# 设置索引列，可以为None
```

### 获取基础信息

```python
# shape：获取文件中信息，得到的是行数和列数，类型是元组
print(people.shape,type(people.shape))

# columns：获取所有的列名
print(people.columns)

# columns也可以直接生成一个列名，他会对文件直接进行修改
people.columns = ["id","type",...]

# head()：获取头信息，默认为前五行，可以通过输入数字修改
print(people.head(3))

# tail()：获取尾信息，默认为后五行
print(people.tail())
```

### pandas索引

```python
# pandas的单元格有两种属性：index,data，这与字典类似：key,value
# Series()：把一组数据转换为一维数组（序列），可以理解为一行或者一列
d = {"x":100,"y":200,"z":300}

# 转换字典为一维数组
s1 = pd.Series(d)

# 转换列表为一维数组
s1 = pd.Series(["x","y","z"],[100,200,300])	

# 直接生成序列
s2 = pd.Series([100,200,300],		# 序列内容
               index=["x","y","z"],	# 序列索引
               name="letter")		# 序列标题

# index：输出索引
print(s1.index)

# 输出的Series并不确定是行或者列，这取决于在DataFrame中的位置
s1 = pd.Series([1,2,3],index=[1,2,3],name="A")
s2 = pd.Series([10,20,30],index=[1,2,3],name="B")
s3 = pd.Series([100,200,300],index=[1,2,3],name="C")


# 如果希望把序列以行的形式加入DataFrame，需要使用字典的模式
df = pd.DataFrame({s1.name:s1 , s2.name:s2 , s3.name:s3})
# series中的index有什么用？DataFrame也有index，两者起到一个对齐的作用

# 如果希望把序列以列的形式加入DataFrame，需要使用列表的模式
df = pd.DateFrame([s1,s2,s3])
```

### 数字区域自动填充

```python
# 序列添加到数据帧中可以变成行或者列，数据帧中的行或者列提取出来也是序列
print(type(df["A"]))		# 输出显示类型为为Series

# at()：用于访问Series的某个值，同样可以修改此值
df["A"].at[0] = 100
# at():如果用于DataFrame也可以，需要使用两个数值：index,data
df.at[0,"A"] = 100

# 填充：通过循环和at()可以设置一个Series的所有值，循环个数就是index
for i in df.index:
    df["A"].at[i] = i+1
# 填充后的数据是一个浮点型，如果需要整型，则需要在读取时通过dtype设置为str(不让改为int)
```

### 填充日期序列

```python
# 导入datetime库中的两个时间函数
from datetime import date,timedelta

# date:设置一个初始日期,date.today():获取当前日期
start = date(2021,1,1)		# 类型是datetime.date

# timedelta:日期运算函数
one_day = timedelta(days=1)	
yesterday = start - one_day
tomorrow = start + one_day

# 月份进位算法函数
def add_month(d,md):	# 输入日期以及月份步数
    yd = md//12			# 计算年份步数
    m = d.month + md%12	# 计算月份
    if m!=12:			# 排除特殊情况
        yd += m//12
        m = m%12
    return date(d.year+yd,m,d.day)

# 填充日期
for i in df.index:
    df["B"].at[i] = start + timedelta(days=1)	# 填充日份
    df["B"].at[i] = date(start.year+1,start.month,start.day)	# 填充年份
    df["B"].at[i] = add_month(start,i)		# 填充月份
```

### 函数填充，计算列

```python
books = pd.read_excel("./*.xlsx",index_col="ID")

# 进行列运算，直接对序列进行操作即可
books["c"] = books["a"] * books["b"]

# 如果不是两个列，是一个列和一个值同样可以
books["c"] = books["a"] + 2

# 或者通过apply函数进行简化计算
books["c"] = books["a"].apply(lambdy x:x+2)

# 如果需要对部分序列进行计算，可以使用值计算：
for i in range[5,16]:
    books["c"].at[i] = books["a"].at[i] *books["b"].at[i]
```

### 网络数据与排序

```python
# 获取网络数据，输出是列表
url = "https://info.usd-cny.com/wti/lishi.htm"
html_data = pd.read_html(url,index_col="年份")

# 转换为DataFrame数据
df = pd.DataFrame(html_data[0])

# 清除数据中的特殊符号并转换为浮点型数字
del_head = lambda x : float(x[1:])
del_tail = lambda x : float(x[:-1])

df["最低价"] = df["最低价"].apply(del_head)
df["平均价"] = df["平均价"].apply(del_head)
df["最高价"] = df["最高价"].apply(del_head)
df["年幅度"] = df["年幅度"].apply(del_tail)

# 排序函数：sort_values()
df.sort_values(by="最低价",		# 选择排序序列
               ascending=False,    # 升序，默认为True，如果为False为倒序
               inplace=True)	   # 直接在原数据上进行改动	
# 多重排序
df.sort_values(by=["最低价"，"年幅度"], # 排序多重条件，依次进行
               ascending=[False,True],# 升降序多重条件
               inplace=True)
```

### 筛选

```python
# 设置筛选条件,年幅度大于0,以及平均价大于等于30小于80
location_amptitude = lambda x : x>0
location_mean_value = lambda x : 80>x>=50

# 筛选函数：loc[]
df = df.loc[df["年幅度"].apply(location_amptitude)]

# 多重筛选，这里一行写不完，使用了" \"进行换行
df = df.loc[df.年幅度.apply(location_amptitude)] \
	   .loc[df.平均价.apply(location_mean_value)]
```

## 绘图

### 柱状图

```python
# 导入做图库
import matplotlib.pyplot as plt

```

