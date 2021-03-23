'''
@Author: Randy
@Date: 2020-10-13
@LastEditTime: 2020-10-13
@Description: API test for sim
@FilePath: sim_get_set_stress.py
'''
'''
-------------------------------------------------------------------------------
脚本逻辑:
    1.单个或成对接口循环执行2H
    2.接口包含getImsi&getIccid,getStatus,writePhonebook&readPhonebook&getPhoneNumber
    3.输出异常返回结果
脚本统计:
    1.接口函数调用崩溃log
测试前准备:
    无
-------------------------------------------------------------------------------
'''

import sim
import ure
import utime

interval = 7200    #运行持续时长

runtimes = 0
print('[start] sim_api_stress: getImsi&getIccid;')
start_time = utime.time()
while 1:
    duration = utime.time()-start_time
    if duration > interval:
        print('[end] sim_api_stress: getImsi&getIccid,runtimes: %s;' % runtimes)
        runtimes = 0
        break
    try:
        a1 = sim.getImsi()
        a2 = sim.getIccid()
        if a1 == -1:
            print('runtimes:%s,getImsi:: %s||result_api:: False;' % (runtimes,a1))
        if a2 == -1:
            print('runtimes:%s,getIccid:: %s||result_api:: False;' % (runtimes,a2))
    except Exception as e:
        print('runtimes:%s,getImsi&getIccid::[error]%s||result_api:: False;'%(runtimes,e))
    if duration%600 == 0:
        print('keep running... current duration: %sH imsi:%s ccid:%s;'%(duration/3600,a1,a2))
        utime.sleep(1)
    runtimes += 1

print('[start] sim_api_stress: getStatus;')
start_time = utime.time()
while 1:
    duration = utime.time()-start_time
    if duration > interval:
        print('[end] sim_api_stress: getStatus,runtimes: %s;' % runtimes)
        runtimes = 0
        break
    try:
        b1 = sim.getStatus()
        if b1 == -1:
            print('runtimes:%s,getStatus:: %s||result_api:: False;' % (runtimes,b1))
    except Exception as e:
        print('runtimes:%s,getStatus::[error]%s||result_api:: False;'% (runtimes,e))
    if duration%600 == 0:
        print('keep running... current duration: %sH,current runtimes: %s;'%(duration/3600,runtimes))
        utime.sleep(1)
    runtimes += 1

print('[start] sim_api_stress: writePhonebook&readPhonebook&getPhoneNumber;')
start_time = utime.time()
while 1:
    duration = utime.time()-start_time
    if duration > interval:
        print('[end] sim_api_stress: writePhonebook&readPhonebook&getPhoneNumber,runtimes: %s;' % runtimes)
        runtimes = 0
        break
    try:
        c1 = sim.writePhonebook(9,1,"111","15556904516")
        c2 = sim.readPhonebook(9,0,0,"1")
        sim.writePhonebook(7, 1, "111", "10086")
        c3 = sim.getPhoneNumber()
        if c1 == -1:
            print('runtimes:%s,writePhonebook:: %s||result_api:: False;' % (runtimes,c1))
        if c2 == -1 or not(ure.search('155',str(c2))):
            print('runtimes:%s,readPhonebook:: %s||result_api:: False;' % (runtimes,c2))
        if c3 == -1 or not(ure.search('10086',str(c3))):
            print('runtimes:%s,getPhoneNumber:: %s||result_api:: False;' % (runtimes,c3))
    except Exception as e:
        print('runtimes:%s,writePhonebook&readPhonebook&getPhoneNumber::[error]%s||result_api:: False;'% (runtimes,e))
    if duration%600 == 0:
        print('keep running... current duration: %sH phonenumber:%s;'%(duration/3600,c3))
        utime.sleep(1)