'''
@Author: Randy
@Date: 2020-10-14
@LastEditTime: 2020-10-14
@Description: API test for thread
@FilePath: thread_lr_stress.py
'''
'''
-------------------------------------------------------------------------------
脚本逻辑:
    1.单个或成对接口循环执行2H
    2.接口包含allocate_lock,lock.acquire&lock.release，start_new_thread，get_ident&stack_size
    3.输出异常返回结果
脚本统计:
    1.接口函数调用崩溃log
测试前准备:
    无
备注：
    1.当前版本暂无结束线程的接口，无法结束线程
    2.本脚本测试创建16个线程，持续运行，最多可同时创建46个线程
-------------------------------------------------------------------------------
'''

import _thread
import utime
runtime = 1 #运行次数
a = 0
lock = _thread.allocate_lock()
b = _thread.stack_size() #返回创建新线程使用的堆栈大小（以字节为单位）
def th_func(delay, id):
    ident = _thread.get_ident()  # 获取当前线程号
    while True:
        lock.acquire() # 获取锁
        print('[thread %d ident %s] a is %d;' % (id, ident, delay))
        lock.release()  # 释放锁
        utime.sleep(delay)

try:
    for i in range(1,17):
        a = _thread.start_new_thread(th_func, (i, i))
except Exception as error:
    print('[error]'+str(error)+';')
    print('thread:: False||result_api:: False;')
start_run_time = utime.time()
while 1:  ##主线程持续运行
    duration = utime.time() - start_run_time
    if duration%3600 == 0:
        free_heap_size = _thread.get_heap_size()
        print('[memory]free_heap_size: %s;'%free_heap_size)

#反复创建、删除线程
#当前版本暂无结束线程的接口，无法结束线程