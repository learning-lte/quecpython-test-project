'''
@Author: Randy
@Date: 2020-09-08
@LastEditTime: 2020-09-08
@Description: API test for modem
@FilePath: modem_getcomminfo_api_test.py
'''

import modem
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
    utime.sleep(1)

api_list = [
    'modem.getDevImei()',
    'modem.getDevModel()',
    'modem.getDevSN()',
    'modem.getDevFwVersion()',
    'modem.getDevProductId()',
            ]
for i in api_list:
    api_test(i)