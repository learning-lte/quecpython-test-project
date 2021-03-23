'''
@Author: Randy
@Date: 2020-09-08
@LastEditTime: 2020-09-08
@Description: API test for Timer
@FilePath: timer_start_stop_api_test.py
'''

import utime
from machine import Timer

timer_list = [Timer.Timer0, Timer.Timer1, Timer.Timer2, Timer.Timer3]
mode_list = [Timer.ONE_SHOT,Timer.PERIODIC ]
def run_test(t):
    print('run test;')
try:
    for i in timer_list:
        print('Current Timer: %s;'%i)
        timer1 = Timer(i)  #定时器号，EC100YCN支持定时器0~3
        # timer.ONE_SHOT
        # 单次模式，定时器只执行一次
        # timer.PERIODIC
        # 周期模式，循环执行
        for m in mode_list:
            print('Current mode: %s;' % m)
            timer1.start(period=1000,mode=m,callback=run_test)
            n = 0
            while 1:
                if n > 10:
                    break
                utime.sleep(1)
                n += 1
            timer1.stop()
    print('Timer.start::pass||Timer_api:: True;')
except Exception as e:
    print('Timer.start::%s||Timer_api: Flase;')
