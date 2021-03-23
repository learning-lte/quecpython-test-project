"""
@Author: trent.zhang
@Date: 2020-10-12
@LastEditTime: 2020-10-12 16:48:08
@Description: API test for RTC
@FilePath: rtc_datetime_stress.py
"""
'''
-------------------------------------------------------------------------------
脚本逻辑:
    1.单个或成对接口循环执行2H
    2.接口包含.datetime
    3.输出异常返回结果
脚本统计:
    1.接口函数调用崩溃log
测试前准备:
    无
-------------------------------------------------------------------------------
'''
from machine import RTC
import utime
interval = 7200    #运行持续时长
rtc = RTC()


def api_stress():
    print('[start] rtc_datetime_stress: ONE_SHOT start&stop;')
    start_time = utime.time()
    m = 0
    while 1:
        duration = utime.time() - start_time
        if duration > interval:
            print('[end] timer_start_stop_stress: ONE_SHOT start&stop;')
            break
        if duration % 600 == 0:
            print('keep running... current duration: %s current runtimes:%s;' % (duration,m))
            utime.sleep(1)
        try:
            rtc.datetime()
        except Exception as e:
            print('.datetime[%s]:: %s||result_api:: False;' % (m, e))
        m += 1


if __name__ == '__main__':
    api_stress()
