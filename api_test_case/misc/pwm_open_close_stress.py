# coding: utf-8
"""
@Author: Randy.zhu
@Date: 2020-10-22
@LastEditTime: 2020-10-22 17:28:08
@Description: API test for pwm
@FilePath: pwm_open_close_stress.py
"""
'''
-------------------------------------------------------------------------------
脚本逻辑:
    1.单个或成对接口循环执行2H
    2.接口包含open&close
    3.输出异常返回结果
脚本统计:
    1.接口函数调用崩溃log
测试前准备:
    无
-------------------------------------------------------------------------------
'''
'''
注：EC100YCN平台，支持PWM0~PWM5，对应引脚如下：
PWM0 – 引脚号19
PWM1 – 引脚号18
PWM2 – 引脚号16
PWM3 – 引脚号17
PWM4 – 引脚号23
PWM5 – 引脚号22
'''
from misc import PWM
import utime

interval = 7200    #运行持续时长

pwm_list = [PWM.PWM0,PWM.PWM1,PWM.PWM2,PWM.PWM3,PWM.PWM4,PWM.PWM5]

runtimes = 0
print('[start] pwm_api_stress: open&close;')
start_time = utime.time()
while 1:
    duration = utime.time()-start_time
    for i in pwm_list:
        pwm = PWM(i, 100, 220)
        if duration > interval:
            print('[end] pwm_api_stress: open&close,runtimes: %s;' % runtimes)
            break
        try:
            a = pwm.open()
            b = pwm.close()
            if a == -1:
                print('runtimes:%s,pwm.open():: fail %s||result_api:: False;' % (runtimes,a))
            if b == -1:
                print('runtimes:%s,pwm.close():: fail %s||result_api:: False;' % (runtimes,b))
        except Exception as e:
            print('runtimes:%s,pwm open&close::[error]%s||result_api:: False;'% (runtimes,e))
        if duration%600 == 0:
            print('keep running... current duration: %sH,current runtimes:%s;'%(duration/3600,runtimes))
            utime.sleep(1)
    runtimes += 1
