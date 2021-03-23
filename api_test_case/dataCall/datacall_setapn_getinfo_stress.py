"""
@Author: trent.zhang
@Date: 2020-10-12
@LastEditTime: 2020-10-12 16:48:08
@Description: API test for dataCall
@FilePath: datacall_setapn_getinfo_stress.py
"""
'''
-------------------------------------------------------------------------------
脚本逻辑:
    1.单个或成对接口循环执行2H
    2.接口包含setApn&getInfo
    3.输出异常返回结果
脚本统计:
    1.接口函数调用崩溃log
测试前准备:
    无
-------------------------------------------------------------------------------
'''
import utime
import net
import dataCall
interval = 172800    # 运行持续时长
outtime = 60  # 设置找网时间限制


def api_stress():
    m = 1
    start_time = utime.time()
    while 1:
        duration = utime.time() - start_time
        if duration > interval:
            break
        if duration % 100 == 0:
            print('keep running... current duration: %s;' % duration)
        try:
            # 添加cfun切换的操作，检测注网成功后再循环设置apn拨号
            t1 = utime.time()
            net.setModemFun(0)
            net.setModemFun(1)
            while True:
                # 获取网络状态
                n = list(net.getState())
                t = utime.time() - t1
                utime.sleep(1)
                if t > 30:
                    if net.getModemFun() == 1:
                        print('The timeout period is %s;' % t)
                    else:
                        net.setModemFun(1)
                        # print('setModemFun is ')
                        pass
                if t > outtime:
                    print('Looking for a network failure: %s;' % outtime)
                    break
                else:
                    pass
                if n[1][0] == 1:
                    break
                else:
                    pass
            ta = utime.time()
            while 1:
                b = dataCall.getInfo(1, 0)
                tb = utime.time()-ta
                if list(b)[2][0] == 0:
                    if tb > 30:
                        if list(b)[2][0] == 0:
                            print('setApn&getInfo[%s]:: getInfo_timeout:%s||result_api:: False %s;' % (m, b, tb))
                        else:
                            pass
                    if tb > outtime:
                        print('setApn&getInfo[%s]:: getInfo_timeout60:%s||result_api:: False;' % (m, b))
                else:
                    break
        except Exception as e:
            print('setApn&getInfo[%s]:: %s||result_api:: False;' % (m, e))
        utime.sleep(1)
        m += 1


if __name__ == '__main__':
    api_stress()
