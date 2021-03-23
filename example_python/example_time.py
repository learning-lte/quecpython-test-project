'''
@Author: Baron
@Date: 2020-06-17
@LastEditTime: 2020-06-17 17:06:08
@Description: example for module utime
@FilePath: example_utime.py
'''
import utime

for i in [0,1,2,3,4,5]:
    utime.sleep(1)   # 休眠
    print(i)

# 获取本地时间，返回元组
utime.localtime())

# 返回当前时间戳，参数为元组
utime.mktime(utime.localtime()))