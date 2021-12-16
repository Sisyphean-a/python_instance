from pymouse import *
import time
from random import random,uniform

# 初始化，并获取全屏尺寸
def init():
    m = PyMouse()
    print("全屏尺寸：",m.screen_size())     # 获取全屏尺寸
    return m

# 获取位置基本模块
def get_position(m):
    for i in reversed(range(1,3)):
        print(str(i)+"秒钟后获取位置")
        time.sleep(1)
    print("目前位置为："+str(m.position()))
    return m.position()

# 自动获取位置，依赖于get_position()
def auto_confirm_size(m):
    position = get_position(m)
    return position

# 手动获取位置，依赖于auto_confirm_size()
def confirm_size(m):
    #enter = input("是否手动输入位置（Y/N）：")
    enter = "N"
    if enter == "Y":
        position = input("请输入位置，模式为（x,y）：")
    else:
        position = auto_confirm_size(m)
    return position

# 对位置随机化，避免封号
def random_position(position):
    new_position = ()
    x = uniform(position[0]-5,position[0]+5)
    y = uniform(position[1]-5,position[1]+5)
    new_position = x + y
    return position

# 对时间随机化，避免封号
def random_time():
    t = 0.2
    time = uniform(t-0.1,t+0.2)
    return round(time,2)

# 鼠标模拟点击
def mouse(m,timee,position):
    print("开始模拟点击")
    m.click(position[0],position[1],button=1)
    time.sleep(timee)

if __name__ == "__main__":
    m = init()
    position = confirm_size(m)
    for i in range(61):
        position = random_position(position)
        timee = random_time()
        mouse(m,timee,position)
        print("第"+str(i)+"点击，"+"点击位置"+str(m.position()))
