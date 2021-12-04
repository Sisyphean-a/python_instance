## 导入及初始化

### 导入

- import bs4

- from bs4 import BeautifulSoup

### 初始化

- soup = BeautifulSoup(html , "html.parst")
- soup = BeautifulSoup(html , "lxml")

## 搜索

### 使用find or find_all

- find：获取第一个满足条件的标签之后立即返回，获得一个元素
- find_all：获取所有满足条件的元素

### 使用select（css选择器）

- 通过标签名查找：

  soup.select("a")

- 通过类名查找，class前面需要加一个 . ：

  soup.select(".sister")

- 通过id查找，id面前需要加一个 # ：

  soup.select("#link1")

- 通过属性查找，需要使用中括号[]：

  soup.select(' [ href = "http://****.com" ] ')

- 组合查找

  - 在tag中进行两个属性的查找

    soup.select("a#link2")

  - 树状查找，获取每一层中下一层的所有信息

    soup.select("div ul a#link2")

### 返回值

- 属性：find_all和select返回的是一个列表，里面的元素的类型：

  bs4.element.Tag

- 获取值：可以直接对bs4.element.Tag属性的元素进行处理

  - 获取内容，可以直接使用get_text：

    soup_list[0].get_text

  - 获取文本：

    - 使用next_element

      soup_list[0].next_element

    - 使用string(常用)

      soup_list[0].string

  - 获取href，使用["href"]:

    soup_list[0]\["href"]

  - 获取id，使用["id"]:

  - 获取class，使用["class"]:

> 注意，一般使用迭代的方式输出，例如：
> soup_list = soup.select(" div a#link2 ")
> for a soup_list:
> ​	print(a.string)

