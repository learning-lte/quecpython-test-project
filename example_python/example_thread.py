'''
@Author: Baron
@Date: 2020-06-22
@LastEditTime: 2020-06-22 17:16:20
@Description: example for module _thread
@FilePath: example_thread.py
'''
import _thread
import utime

a = 0
# 创建一个lock的实例
lock = _thread.allocate_lock()

def th_func(delay, id):
	global a
	while True:
		lock.acquire()  # 获取锁
		if a >= 10:
			print('thread %d exit' % id)
			lock.release()  # 释放锁
			break
		a+=1
		print('[thread %d] a is %d' % (id, a))
		lock.release()  # 释放锁
		utime.sleep(delay)

for i in range(2):
    _thread.start_new_thread(th_func, (i + 1, i))   # 创建一个线程，当函数无参时传入空的元组


while 1:
    pass