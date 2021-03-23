'''
@Author: Randy
@Date: 2020-09-27
@LastEditTime: 2020-11-19
@Description: API test for thread
@FilePath: thread_bulid_lock_api_test.py
'''
'''
备注：
    1.当前版本暂无结束线程的接口，无法结束线程
    2.本脚本测试创建16个线程,最多可同时创建46个线程
'''
import _thread
import utime

a = 0
b = 'b'
c = 'c'
lock = _thread.allocate_lock()
c = _thread.stack_size()  # 设置创建新线程使用的堆栈大小（以字节为单位）
if c != 8192:
    print('stack_size:: %s||result_api:: False;' % c)

def th_func(delay, id):
    global a
    b = _thread.get_ident()  # 获取当前线程号
    while True:
        lock.acquire() # 获取锁
        if a >= 10:
            print('thread %d ident %s exit;' % (id,b))
            lock.release() # 释放锁
            a += 1
            print(a)
            break
        a += 1
        print('[thread %d] a is %d;' % (id, a))
        lock.release()  # 释放锁
        utime.sleep(delay)

try:
    for i in range(16):
        a1 = _thread.start_new_thread(th_func, (i + 1, i))

except Exception as error:
    print('thread.start_new_thread::[error]%s||result_api:: False;'%error)
print('thread:: True||result_api:: True;')
while 1:  ##主线程持续运行`
    if a >= 26:
        h = _thread.get_heap_size()
        if h:
            print('get_heap_size:: %s||result_api:: True;' % h)
        else:
            print('get_heap_size:: %s||result_api:: False;' % h)
        break
# exit()接口已删除，不开放使用
# _thread.exit()
# print('thread.exit(): True,result_api: True')