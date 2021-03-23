'''
@Author: Randy
@Date: 2020-09-08
@LastEditTime: 2020-09-08
@Description: API test for Pin
@FilePath: pin_write_read_api_test.py

EC100YCN平台引脚对应关系如下：
GPIO1 – 引脚号22
GPIO2 – 引脚号23
GPIO3 – 引脚号178
GPIO4 – 引脚号199
GPIO5 – 引脚号204
'''

from machine import Pin
import utime
GPIO_list = [Pin.GPIO1, Pin.GPIO2, Pin.GPIO3, Pin.GPIO4, Pin.GPIO5]
direction_list = [Pin.IN , Pin.OUT]
pullMode_list = [Pin.PULL_DISABLE, Pin.PULL_PU, Pin.PULL_PD]
level_list = [0,1]
try:
    for i in GPIO_list: #引脚号，EC100YCN平台支持的范围（0~255）
        for m in direction_list:#0-输入模式，1-输出模式
            for n in pullMode_list:#0-PULL_DISABLE，1-PULL_PU，2-PULL_PD
                for k in level_list:#引脚电平，0-low，1-high
                    pin = Pin(i, m, n, k)
                    pin_read1 = pin.read()
                    if m == 1:
                        if k == 0:
                            pin.write(1)
                            pin_read2 = pin.read()
                            if pin_read1 == pin_read2 or pin_read2 != 1:
                                print(
                                    'machine.Pin(%s,%s,%s,%s):: Flase||Pin_api:: Flase;' % (
                                    i, m, n, k))
                        else:
                            pin.write(0)
                            pin_read2 = pin.read()
                            if pin_read1 == pin_read2 or pin_read2 != 0:
                                print(
                                    'machine.Pin(%s,%s,%s,%s):: Flase||Pin_api:: Flase;' % (
                                    i, m, n, k))
                    utime.sleep(0.5)
    else:
        print('machine.Pin::pass||Pin_api:: True;')
except Exception as e:
    print('machine.Pin::[error]%s||Pin_api: Flase;'%e)