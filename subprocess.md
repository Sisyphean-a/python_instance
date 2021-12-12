# subprocess

系统自带库，需要导入但不需要pip

基本使用方法，调用终端

```python
import subprocess

# 直接调用命令，返回值即是系统返回，成功返回0，错误返回1
# shell=True表示命令在shell中运行
subprocess.call(["ls","-l"] , shell = True)
subprocess.call("ls -l" , shell = True)

# 如果需要获取命令的终端输出
subprocess.check_output(["echo" , "Hello World!"])
```

如果不希望频繁输入subprocess，也可以使用另一种调用方式

```python
from subprocess import *

call("ls -l" , shell = True)
```



### subprocess.run()函数

作用：执行args参数所表示的命令，等待命令执行完毕，返回一个CompletedProcesss对象。注意：**run函数是同步函数，需要等待**

```python
from subprocess import *

run(args,			# 通过创建进程而执行的命令及参数，也就是命令行
    *,
    stdin=None, 	# 指定命令的输入途径
    input=None,		# 命令的具体输入内容，input和stdin不能同时使用
    stdout=None,	# 指定命令的输出途径
    	# 如果需要采集命令执行的结果，可以传入参数stdout=subprocess.PIPE
    stderr=None,	# 指定命令的error输出途径
    shell=False,	# 表示是否通过shell来执行命令（Linux默认为/bin/sh）
    cwd=None 		# 指示了当前工作路径
    timeout=None,	# 设置超时时间，如果超时，则终止子进程
    check=False, 	# 如果设置为True,就检查命令的返回值，当返回值为0时，抛出异常
    encoding=None,	#
    errors=None,	#
    text=None,		# 将stdin,stdout,stderr修改为string模式
    env=None)		#

# 有无shell的args输入情况
run('ls')	# 没有shell同时不是列表，不能使用参数
run(['ls','-lh'])	# 可以使用参数，但是需要使用列表来表达
run('ls -lh',shell=True)	#可以使用参数，表达形式类似于终端

#text参数
run('grep fs',shell=True,input=b'asdfs\nfdfs')
run('grep fs',shell=True,input='asdfs\nfdfs',text=True)


```



