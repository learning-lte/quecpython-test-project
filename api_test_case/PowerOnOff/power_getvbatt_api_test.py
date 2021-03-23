'''
@Author: Randy
@Date: 2020-09-11
@LastEditTime: 2020-09-11
@Description: API test for getvbatt
@FilePath: power_getvbatt_api_test.py
'''

from misc import Power

try:
    powerdown_reason = Power.powerDownReason()
    if powerdown_reason == 2:
        print('Power.powerDown():: 2(期望返回值正确)||result_api:: True;')
    else:
        print('Power.powerDown():: %s(期望返回值错误)||result_api:: True;'%powerdown_reason)
except Exception as e:
    print('Power.powerDown():: [error]%s||result_api:: Flase;'%e)

try:
    poweron_reason = Power.powerOnReason()
    if poweron_reason == 1:
        print('Power.powerOnReason():: 1||result_api:: True;')
    else:
        print('Power.powerOnReason():: %s||result_api:: True;'%poweron_reason)
except Exception as e:
    print('Power.powerOnReason():: [error]%s||result_api:: Flase;'%e)

try:
    power_getvbatt = Power.getVbatt()
    print('Power.getVbatt():: %s||result_api:: True;'%power_getvbatt)
except Exception as e:
    print('Power.powerRestart():: [error]%s||result_api:: Flase;'%e)
