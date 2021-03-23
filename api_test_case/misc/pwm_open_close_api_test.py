# coding: utf-8
"""
@Author: Randy.zhu
@Date: 2020-10-22
@LastEditTime: 2020-10-22 17:28:08
@Description: API test for pwm
@FilePath: pwm_open_close_api_test.py
"""
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

pwm_list = [PWM.PWM0,PWM.PWM1,PWM.PWM2,PWM.PWM3,PWM.PWM4,PWM.PWM5]


def api_test(api):
    try:
        result1 = eval(api)
    except Exception as err:
        result1 = 'error'
        print('[error]'+str(err)+';')
    if result1 == 0:
        result2 = True
    else:
        result2 = False
    print('%s:: %s||result_api:: %s;'%(api, result1, result2))


if __name__ == '__main__':
    list = [
        'pwm.open()',
        'pwm.close()',
    ]
    for m in pwm_list:
        pwm = PWM(m, 100, 220)
        for i in list:
            api_test(i)
