# -*- coding: UTF-8 -*-
'''
@Author: Randy
@Date: 2020-09-08
@LastEditTime: 2020-09-08
@Description: API test for sim
@FilePath: sim_get_set_api_test.py
'''

import sim
import net
import ure
import utime

def api_test(api):
    result1 = -1
    try:
        result1 = eval(api)
        if 'Modem' in api:
            utime.sleep(3)
        if 'verifyPin' in api:
            utime.sleep(10)

    except Exception as err:
        print('[error]'+str(err)+';')
    if result1 != -1:
        result2 = True
        if 'readPhonebook' in api and '15556904516' not in str(result1):
            result2 = False
    else:
        result2 = False
    print('%s:: %s||result_api:: %s'%(api,result1,result2))
    utime.sleep(1)

api_list = [
    'sim.getImsi()',
    'sim.getIccid()',
    'sim.getPhoneNumber()',
    'sim.getStatus()',
    'sim.enablePin("1234")',
    'net.setModemFun(0)',
    'net.setModemFun(1)',
    'sim.verifyPin("1234")',
    'sim.getImsi()',
    'sim.getIccid()',
    'sim.disablePin("1234")',
    #'sim.unblockPin(puk, newPin)',
    #'sim.changePin(oldPin, newPin)',
    'sim.writePhonebook(9,1,"111","15556904516")',
    #'sim.writePhonebook(9,2,"张三","15556904517")',  # 不支持中文
    'sim.readPhonebook(9,0,0,"1")',
    #'sim.readPhonebook(9,0,0,"张")', # 不支持中文
            ]
for i in api_list:
    api_test(i)