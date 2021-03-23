'''
@Author: Baron
@Date: 2020-06-17
@LastEditTime: 2020-06-17 17:06:08
@Description: example for module timer
@FilePath: example_timer.py
'''
import utime
from machine import timer

num = 0
t=timer(1)

# 创建一个执行函数，并将timer实例传入
def timer_test(t):
	global num
	print('num is %d' % num)
	num += 1
	if num > 10:
	    print('num > 10, timer exit')
	    t.deinit()

t.init(callback=timer_test, freq=1)