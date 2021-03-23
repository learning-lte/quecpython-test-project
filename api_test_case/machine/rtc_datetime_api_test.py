# coding: utf-8
"""
@Author: trent.zhang
@Date: 2020-09-23
@LastEditTime: 2020-09-23 16:36:08
@Description: example for module RTC
@FilePath: rtc_datetime_api_test.py
"""
from machine import RTC
import utime


def api_test(api):
    result1 = 'error'
    try:
        result1 = eval(api)
    except Exception as err:
        print('[error]'+str(err)+';')
    if result1 != 'error':
        result2 = True
    else:
        result2 = False
    print('%s:: %s||result_api:: %s'%(api, result1, result2))
    utime.sleep(0.05)


if __name__ == '__main__':
    list = [
        'RTC().datetime()',
        'RTC().datetime([2020, 3, 12, 1, 12, 12, 12, 0]) ',  # 年，月，日，星期，时，分，秒，微秒
        'RTC().datetime()',
    ]
    for i in list:
        api_test(i)
