# matplotlib图例中文乱码

## 替换外源字体

- 获取微软雅黑：https://github.com/chengda/popular-fonts/blob/master/%E5%BE%AE%E8%BD%AF%E9%9B%85%E9%BB%91.ttf
- 安装此ttf
- 移动到/home/xixifu/.local/lib/python3.8/site-packages/matplotlib/mpl-data/ttf/font中
- 经测试，无效

## 使用可用字体

### 获取matplotlib可用中文字体

```python
#! /usr/bin/env python
# -*- coding: utf-8 -*-
from matplotlib.font_manager import FontManager
import subprocess

fm = FontManager()
mat_fonts

 = set(f.name for f in fm.ttflist)
#print(mat_fonts)
output = subprocess.check_output('fc-list :lang=zh -f "%{family}\n"', shell=True)
#print( '*' * 10, '系统可用的中文字体', '*' * 10)
#print (output)
zh_fonts = set(f.split(',', 1)[0] for f in output.decode('utf-8').split('\n'))
available = mat_fonts & zh_fonts
print ('*' * 10, '可用的字体', '*' * 10)
for f in available:
     print (f)
```

 获取结果

```
AR PL UKai CN
AR PL Mingti2L Big5
Unifont
Noto Sans CJK JP
AR PL KaitiM Big5
Noto Serif CJK JP
Droid Sans Fallback
AR PL UMing CN
```

### 替换字体

#### 临时替换

```python
import matplotlib.pyplot as plt

# 任选上面一个字体替换到下一行中
plt.rcParams['font.sans-serif'] = ['AR PL UKai CN'] 
```

#### 配置替换

- 找到matplotlib文件夹下的matplotlibrc配置文件：
/home/xixifu/.local/lib/python3.8/site-packages/matplotlib/mpl-data/matplotlibrc

- 或者按住Ctrl键点击下面的文件名，注意需要替换你的系统名称
[matplotlibrc](/home/xixifu/.local/lib/python3.8/site-packages/matplotlib/mpl-data/matplotlibrc) 

- 修改内容：

	删除font.family和font.sans-serif两行前的#，并在font.sans-serif后添加中文字体:

	font.sans-serif:AR PL UKai CN,

- 保存文件

### 重启python

或者重启vscode

完成