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
    for i in reversed(range(1,6)):
        print("i"+"秒钟后获取位置")
        time.sleep(1)
    print("目前位置为："+str(m.position()))
    enter = input("是否继续获取位置（Y/N）:")

# 自动获取位置，依赖于get_position()
def auto_confirm_size(m):
    enter = input("是否获取位置（Y/N）:")
    if enter == "Y":
        position = get_position(m)
    else:
        print("位置获取结束！")
    return position

# 手动获取位置，依赖于auto_confirm_size()
def confirm_size(m):
    enter = input("是否手动输入位置（Y/N）：")
    if enter == "Y":
        position = input("请输入位置，模式为（x,y）：")
    else:
        position = auto_confirm_size(m)
    return position

# 对位置随机化，避免封号
def random_position(position):
    position.x = uniform(position.x-5,position.x+5)
    position.y = uniform(position.y-5,position.y+5)

# 对时间随机化，避免封号
def random_time():
    t = 0.2
    time = uniform(t-0.1,t+0.2)
    return time

# 鼠标模拟点击
def mouse(m,random_time,random_position):
    #m.move(random_position)
    m.click(random_position,button=1)
    time.sleep(random_time)

if __name__ == "__main__":
    m = init()
    position = confirm_size(m)
    for i in range(60):
        random_position = random_position(position)
        random_time = random_time()
        mouse(m,random_time,random_position)
        print("第"+str(i)+"点击，"+"点击位置"+str(m.position))

"""

思路：
    获取位置
    一定范围的随机时间，
    一定范围的随机位置，
    重复进行点击

"""