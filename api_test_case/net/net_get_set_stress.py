'''
@Author: Randy
@Date: 2020-10-13
@LastEditTime: 2020-10-13
@Description: API test for net
@FilePath: net_get_set_stress.py
'''
'''
-------------------------------------------------------------------------------
脚本逻辑:
    1.单个或成对接口循环执行2H
    2.接口包含csqQueryPoll&getSignal,getCellInfo&getCi&getMnc&getMcc&getLac,getConfig&nitzTime,getNetMode&operatorName&getState,
    getModemFun&setModemFun
    3.输出异常返回结果
脚本统计:
    1.接口函数调用崩溃log
测试前准备:
    无
-------------------------------------------------------------------------------
'''
import net
import utime

interval = 7200    #运行持续时长

print('net_api_stress for 2H: csqQueryPoll&getSignal;')
start_time = utime.time()
while 1:
    duration = utime.time()-start_time
    if duration > interval:
        break
    try:
        a1 = net.csqQueryPoll()
        a2 = net.getSignal()
        if a1 == -1:
            print('csqQueryPoll:: %s||result_api:: False;' % a1)
        if a2 == -1:
            print('getSignal:: %s||result_api:: False;' % a2)
    except Exception as e:
        print('csqQueryPoll&getSignal::[error]%s||result_api:: False;'%e)
    if duration%600 == 0:
        print('keep running... current duration: %s  csq: %s;'%(duration,a1))
        utime.sleep(1)

print('net_api_stress for 2H: getCellInfo&getCi&getMnc&getMcc&getLac;')
start_time = utime.time()
while 1:
    duration = utime.time()-start_time
    if duration > interval:
        break
    try:
        b1 = net.getCellInfo()
        b2 = net.getCi()
        b3 = net.getMnc()
        b4 = net.getMcc()
        b5 = net.getLac()
        if b2[0] not in b1[2][0]:
            print('getCellInfo,getCi::%s, %s||result_api:: False;' % (b1,b2))
        if b3[0] not in b1[2][0]:
            print('getCellInfo,getMnc::%s, %s||result_api:: False;' % (b1,b3))
        if b4[0] not in b1[2][0]:
            print('getCellInfo,getMcc::%s, %s||result_api:: False;' % (b1,b4))
        if b5[0] not in b1[2][0]:
            print('getCellInfo,getLac::%s, %s||result_api:: False;' % (b1,b5))

    except Exception as e:
        print('getCellInfo&getCi&getMnc&getMcc&getLac::[error]%s||result_api:: False;'%e)
    if duration%600 == 0:
        print('keep running... current duration: %s ;'%duration)
        utime.sleep(1)

print('net_api_stress for 2H: getConfig&nitzTime;')
start_time = utime.time()
while 1:
    duration = utime.time()-start_time
    if duration > interval:
        break
    try:
        c1 = net.getConfig()
        c2 = net.nitzTime()
        if c1 == -1:
            print('getConfig:: %s||result_api:: False;' % c1)
        if c2 == -1:
            print('nitzTime:: %s||result_api:: False;' % c2)
    except Exception as e:
        print('getConfig&nitzTime::[error]%s||result_api:: False;' % e)
    if duration % 600 == 0:
        print('keep running... current duration: %s getCellInfo:%s nitzTime:%s;' % (duration,c1,c2))
        utime.sleep(1)

print('net_api_stress for 2H: getNetMode&operatorName&getState;')
start_time = utime.time()
while 1:
    duration = utime.time()-start_time
    if duration > interval:
        break
    try:
        d1 = net.getNetMode()
        d2 = net.operatorName()
        d3 = net.getState()
        if d1 == -1:
            print('getNetMode:: %s||result_api:: False;' % d1)
        if d2 == -1:
            print('operatorName:: %s||result_api:: False;' % d2)
        if d3 == -1:
            print('getState:: %s||result_api:: False;' % d3)
    except Exception as e:
        print('getNetMode&operatorName&getState::[error]%s||result_api:: False;' % e)
    if duration % 600 == 0:
        print('keep running... current duration: %s getNetMode:%s operatorName:%s getState:%s;' % (duration,d1,d2,d3))
        utime.sleep(1)

print('net_api_stress for 2H: getModemFun&setModemFun;')
start_time = utime.time()
while 1:
    duration = utime.time()-start_time
    if duration > interval:
        break
    try:
        e1 = net.getModemFun()
        e2 = net.setModemFun(4)
        e3 = net.getModemFun()
        e4 = net.setModemFun(0)
        e5 = net.getModemFun()
        e6 = net.setModemFun(1)
        if e1 != 1:
            print('getModemFun:: %s||result_api:: False;' % e1)
        if e2 != 0:
            print('setModemFun(4):: %s||result_api:: False;' % e2)
        if e3 != 4:
            print('getModemFun:: %s||result_api:: False;' % e3)
        if e4 != 0:
            print('setModemFun(0):: %s||result_api:: False;' % e4)
        if e5 != 0:
            print('getModemFun:: %s||result_api:: False;' % e5)
        if e6 != 0:
            print('setModemFun(1):: %s||result_api:: False;' % e6)
    except Exception as e:
        print('getModemFun&setModemFun::[error]%s||result_api:: False;'%e)
    if duration%600 == 0:
        print('keep running... current duration: %s;'%duration)
        utime.sleep(1)