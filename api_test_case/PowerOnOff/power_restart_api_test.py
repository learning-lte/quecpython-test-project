'''
@Author: Randy
@Date: 2020-09-11
@LastEditTime: 2020-09-11
@Description: API test for Powerrestart
@FilePath: power_restart_api_test.py
'''

from misc import Power
import utime


try:
    powerdown_reason = Power.powerDownReason()
    if powerdown_reason == 1:
        print('Power.powerDown():: 1(期望返回值正确)||result_api:: True;')
    else:
        print('Power.powerDown():: %s(期望返回值错误)||result_api:: True;'%powerdown_reason)
except Exception as e:
    print('Power.powerDown():: [error]%s||result_api:: Flase;'%e)
utime.sleep(2)
try:
    poweron_reason = Power.powerOnReason()
    if poweron_reason == 1:
        print('Power.powerOnReason():: 1||result_api:: True;')
    else:
        print('Power.powerOnReason():: %s||result_api:: True;'%poweron_reason)
except Exception as e:
    print('Power.powerOnReason():: [error]%s||result_api:: Flase;'%e)

utime.sleep(2)
Power.powerRestart()
