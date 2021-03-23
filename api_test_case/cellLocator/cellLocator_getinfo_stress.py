"""
@Author: trent.zhang
@Date: 2020-10-12
@LastEditTime: 2020-10-12 17:05:08
@Description: API test for cellLocator
@FilePath: cellLocator_getinfo_stress.py
"""
'''
-------------------------------------------------------------------------------
脚本逻辑:
    1.单个或成对接口循环执行2H
    2.接口包含getLocation
    3.输出异常返回结果
脚本统计:
    1.接口函数调用崩溃log
测试前准备:
    无
-------------------------------------------------------------------------------
'''
import cellLocator
import utime
interval = 7200    #运行持续时长


def api_stress():
    m =1
    start_time = utime.time()
    while 1:
        duration = utime.time() - start_time
        if duration > interval:
            break
        if duration % 600 == 0:
            print('keep running... current duration: %s;' % duration)
        try:
            a = cellLocator.getLocation("www.queclocator.com", 80, "1111111122222222", 8, 1)
            if str(a) == "(0.0, 0.0, 0)":
                print('getLocation[%s]:: %s||result_api:: False;' % (m, a))
            else:
                pass
        except Exception as e:
            print('getLocation[%s]:: %s||result_api:: False;' % (m, e))
        utime.sleep(1)
        m += 1


if __name__ == '__main__':
    api_stress()

