# coding: utf-8
"""
@Author: trent.zhang
@Date: 2020-10-13
@LastEditTime: 2020-10-13 13:10:08
@Description: example for module ADC
@FilePath: adc_write_read_stress.py
"""
'''
-------------------------------------------------------------------------------
脚本逻辑:
    1.单个或成对接口循环执行2H
    2.接口包含open&read&close
    3.输出异常返回结果
脚本统计:
    1.接口函数调用崩溃log
测试前准备:
    无
-------------------------------------------------------------------------------
'''
from misc import ADC
import utime
interval = 7200


def api_stress():
    adc = ADC()
    start_time = utime.time()
    m = 1
    while 1:
        duration = utime.time() - start_time
        if duration > interval:
            break
        if duration % 600 == 0:
            print('keep running... current duration: %s,runtimes: %s;' % (duration, m))
            utime.sleep(1)
        try:
            a = adc.open()
            b = adc.read(ADC.ADC0)
            c = adc.read(ADC.ADC1)
            d = adc.close()
            if a == 0:
                if d == 0:
                    pass
                else:
                    print('open&read&close[%s]::(%s,%s,%s,%s)||result_api:: False;' % (m, a, b, c, d))
            else:
                print('open&read&close[%s]::(%s,%s,%s,%s)||result_api:: False;' % (m, a, b, c, d))
        except Exception as e:
            print('getLocation[%s]:: %s||result_api:: False;' % (m, e))

        m += 1


if __name__ == '__main__':
    api_stress()
