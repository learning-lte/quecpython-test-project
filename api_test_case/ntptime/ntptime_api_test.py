'''
@Author: Randy
@Date: 2020-09-08
@LastEditTime: 2020-09-08
@Description: API test for ntptime
@FilePath: ntptime_api_test.py
'''

import ntptime
import utime
import ure

def api_test(api):
    result1 = 'error'
    try:
        if ure.search('settime',api):
            a = utime.localtime()
        result1 = eval(api)
        if ure.search('settime',api):
            b = utime.localtime()
            if a[3] == b[3]:
                print('settime not done;')
                result1 = False
        if ure.search('sethost',api): # 重新设置成默认ntp服务器
            ntptime.sethost('ntp.aliyun.com')
    except Exception as err:
        print('[error]'+str(err)+';')
    if result1 != 'error':
        result2 = True
    else:
        result2 = False
    print('%s:: %s||result_api:: %s;'%(api,result1,result2))
    utime.sleep(0.05)

api_list = [
    'ntptime.host',
    'ntptime.sethost("pool.ntp.org")',
    'ntptime.settime()',
            ]
ntptime.host = "ntp.aliyun.com"
for i in api_list:
    api_test(i)