'''
@Author: Randy
@Date: 2020-10-13
@LastEditTime: 2020-10-13
@Description: API test for modem
@FilePath: modem_getcomminfo_stress.py
'''
'''
-------------------------------------------------------------------------------
脚本逻辑:
    1.单个或成对接口循环执行2H
    2.接口包含getDevImei，getDevModel，getDevSN，getDevFwVersion，getDevProductId
    3.输出异常返回结果
脚本统计:
    1.接口函数调用崩溃log
测试前准备:
    无
-------------------------------------------------------------------------------
'''

import modem
import utime

interval = 7200    #运行持续时长

runtimes = 0
print('[start] modem_api_stress: getDevImei;')
start_time = utime.time()
while 1:
    duration = utime.time()-start_time
    if duration > interval:
        print('[end] modem_api_stress: getDevImei,runtimes: %s;' % runtimes)
        runtimes = 0
        break
    try:
        a = modem.getDevImei()
        runtimes += 1
    except Exception as e:
        print('runtimes:%s,getDevImei::[error]%s||result_api: False;'%(runtimes,e))
    if duration%600 == 0:
        print('keep running... current duration: %sH  imei: %s;'%(duration/3600,a))
        utime.sleep(1)

print('[start] modem_api_stress: getDevModel;')
start_time = utime.time()
while 1:
    duration = utime.time()-start_time
    if duration > interval:
        print('[end] modem_api_stress: getDevModel,runtimes: %s;' % runtimes)
        runtimes = 0
        break
    try:
        b = modem.getDevModel()
        runtimes += 1
    except Exception as e:
        print('runtimes:%s,getDevModel::[error]%s||result_api:: False;'%(runtimes,e))
    if duration%600 == 0:
        print('keep running... current duration: %sH  imei: %s;'%(duration/3600,b))
        utime.sleep(1)

print('[start] modem_api_stress: getDevSN;')
start_time = utime.time()
while 1:
    duration = utime.time()-start_time
    if duration > interval:
        print('[end] modem_api_stress: getDevSN,runtimes: %s;' % runtimes)
        runtimes = 0
        break
    try:
        c = modem.getDevSN()
        runtimes += 1
    except Exception as e:
        print('runtimes:%s,getDevSN::[error]%s||result_api:: False;'%(runtimes,e))
    if duration%600 == 0:
        print('keep running... current duration: %sH  imei: %s;'%(duration/3600,c))
        utime.sleep(1)

print('[start] modem_api_stress: getDevFwVersion;')
start_time = utime.time()
while 1:
    duration = utime.time()-start_time
    if duration > interval:
        print('[end] modem_api_stress: getDevFwVersion,runtimes: %s;' % runtimes)
        runtimes = 0
        break
    try:
        d = modem.getDevFwVersion()
        runtimes += 1
    except Exception as e:
        print('runtimes:%s,getDevSN::[error]%s||result_api:: False;'%(runtimes,e))
    if duration%600 == 0:
        print('keep running... current duration: %sH  imei: %s;'%(duration/3600,d))
        utime.sleep(1)

print('[start] modem_api_stress: getDevProductId;')
start_time = utime.time()
while 1:
    duration = utime.time()-start_time
    if duration > interval:
        print('[end] modem_api_stress: getDevProductId,runtimes: %s;' % runtimes)
        runtimes = 0
        break
    try:
        e = modem.getDevProductId()
        runtimes += 1
    except Exception as e:
        print('runtimes:%s,getDevProductId::[error]%s||result_api:: False;'%(runtimes,e))
    if duration%600 == 0:
        print('keep running... current duration: %sH  imei: %s;'%(duration/3600,e))
        utime.sleep(1)