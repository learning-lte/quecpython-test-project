'''
@Author: Randy
@Date: 2020-10-22
@LastEditTime: 2020-10-22
@Description: Stress test for Timer
@FilePath: timer_start_stop_stress.py
'''
'''
-------------------------------------------------------------------------------
脚本逻辑:
    1.单个或成对接口循环执行2H
    2.接口包含start&stop
    3.输出异常返回结果
脚本统计:
    1.接口函数调用崩溃log
测试前准备:
    无
-------------------------------------------------------------------------------
'''

import utime
from machine import Timer

interval = 7200    #运行持续时长

def run_test(t):
    print('run test;')
timer_list = [Timer.Timer0, Timer.Timer1, Timer.Timer2, Timer.Timer3]


runtimes = 0
print('[start] timer_start_stop_stress: ONE_SHOT start&stop;')
start_time = utime.time()
while 1:
    duration = utime.time()-start_time
    if duration > interval:
        print('[end] timer_start_stop_stress: ONE_SHOT start&stop,runtimes:%s;'%runtimes)
        runtimes = 0
        break
    try:
        for i in timer_list:
            timer1 = Timer(i)
            timer1.start(period=1000, mode=Timer.ONE_SHOT, callback=run_test)
            n = 0
            while 1:
                if n > 5:
                    break
                utime.sleep(1)
                n += 1
            timer1.stop()
    except Exception as e:
        print('runtimes:%s,start&stop::[error]%s||result_api:: False;'% (runtimes,e))
    if duration%600 == 0:
        print('keep running... current duration: %sH current runtime:%s;'%(duration/3600,runtimes))
        utime.sleep(1)
    runtimes += 1


print('[start] timer_start_stop_stress: PERIODIC start&stop;')
start_time = utime.time()
timer1 = Timer(Timer.Timer0)
while 1:
    duration = utime.time()-start_time
    if duration > interval:
        print('[end] timer_start_stop_stress: PERIODIC start&stop,runtimes:%s;'%runtimes)
        runtimes = 0
        break
    try:
        for i in timer_list:
            timer1 = Timer(i)
            timer1.start(period=1000, mode=Timer.Timer.PERIODIC, callback=run_test)
            n = 0
            while 1:
                if n > 5:
                    break
                utime.sleep(1)
                n += 1
            timer1.stop()
    except Exception as e:
        print('runtimes:%s,start&stop::[error]%s||result_api:: False;'% (runtimes,e))
    if duration%600 == 0:
        print('keep running... current duration: %sH current runtime:%s;'%(duration/3600,runtimes))
        utime.sleep(1)
    runtimes += 1
