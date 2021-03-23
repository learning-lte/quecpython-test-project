'''
@Author: Randy
@Date: 2020-09-07
@LastEditTime: 2020-09-08
@Description: API test for net
@FilePath: net_get_set_netinfo_cfun_api_test.py
'''

import net
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
    print('%s:: %s||result_api:: %s;'%(api,result1,result2))
    utime.sleep(0.05)

api_list = [
    'net.csqQueryPoll()',
    'net.getCellInfo()',
    'net.getConfig()',
    'net.getNetMode()',
    'net.getSignal()',
    'net.nitzTime()',
    'net.operatorName()',
    'net.getState()',
    'net.getCi()',
    'net.getMnc()',
    'net.getMcc()',
    'net.getLac()',
    'net.getModemFun()',
    'net.setModemFun(0)',
    'net.getModemFun()',
    'net.setModemFun(4)',
    'net.getModemFun()',
    'net.setModemFun(1)',
            ]
for i in api_list:
    api_test(i)
