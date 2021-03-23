'''
@Author: Randy
@Date: 2020-10-22
@LastEditTime: 2020-10-22
@Description: API test for Pin
@FilePath: pin_write_read_stress.py

EC100YCN平台引脚对应关系如下：
GPIO1 – 引脚号22
GPIO2 – 引脚号23
GPIO3 – 引脚号178
GPIO4 – 引脚号199
GPIO5 – 引脚号204
'''

from machine import Pin
import utime

interval = 7200    #运行持续时长



print('[start] pin_write_read_stress: write&read;')
runtimes = 0
start_time = utime.time()
gpio1 = Pin(Pin.GPIO1, Pin.OUT, Pin.PULL_DISABLE, 0)
while 1:
    duration = utime.time()-start_time
    if duration > interval:
        print('[end] pin_write_read_stress: write&read;')
        break
    try:
        a = gpio1.read()
        b = gpio1.write(1)
        c = gpio1.read()
        d = gpio1.write(0)
        if not(b == d == 0):
            print('runtimes:%s,write&read::GPIO1 read()%s %s||result_api:: False;' % (runtimes,b,d))
        if not(a == 0):
            print('runtimes:%s,write&read::GPIO1 write(0) fail %s||result_api:: False;' %(runtimes,a))
        if not(c == 1):
            print('runtimes:%s,write&read::GPIO1 write(1) fail %s||result_api:: False;' %(runtimes,c))
    except Exception as e:
        print('runtimes:%s,write&read::[error]%s||result_api:: False;'% (runtimes,e))
    if duration%600 == 0:
        print('keep running... current duration: %sH current runtimes:%s;'%(duration/3600,runtimes))
        utime.sleep(1)
    runtimes += 1