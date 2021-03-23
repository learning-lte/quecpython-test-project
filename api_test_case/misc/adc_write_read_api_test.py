# coding: utf-8
"""
@Author: trent.zhang
@Date: 2020-09-23
@LastEditTime: 2020-09-23 19:07:08
@Description: example for module ADC
@FilePath: adc_write_read_api_test.py
"""
from misc import ADC
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
        'ADC().open()',
        'ADC().read(ADC.ADC0)',
        'ADC().close()',
        'ADC().open()',
        'ADC().read(ADC.ADC1)',
        'ADC().close()',
    ]
    for i in list:
        api_test(i)
