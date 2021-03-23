'''
@Author: Randy
@Date: 2020-11-05
@LastEditTime: 2020-11-05
@Description: API test for WDT
@FilePath: watch_dog_api_test.py
'''

import utime
from machine import WDT
from machine import Timer

mode_list = [Timer.ONE_SHOT,Timer.PERIODIC ]
def feed(t):
    wdt.feed()
    print('feed watchdog..;')
try:
    wdt = WDT(10)
    timer1 = Timer(0)  #定时器号，EC100YCN支持定时器0~3
    # timer.ONE_SHOT
    # 单次模式，定时器只执行一次
    # timer.PERIODIC
    # 周期模式，循环执行
    for m in mode_list:
        print('Current mode: %s;' % m)
        timer1.start(period=9000,mode=m,callback=feed)
        n = 0
        while 1:
            if n > 10:
                break
            utime.sleep(1)
            n += 1
        timer1.stop()
        wdt.stop()
    print('wdt.feed::pass||watch_dog_api: True;')
except Exception as e:
    print('wdt.feed::%s||watch_dog_api:: Flase;'%e)
