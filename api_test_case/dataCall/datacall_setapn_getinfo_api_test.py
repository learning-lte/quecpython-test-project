# coding: utf-8
"""
@Author: trent.zhang
@Date: 2020-10-12
@LastEditTime: 2020-10-12 10:25:08
@Description: example for module dataCall
@FilePath: dataCall_setapn_getinfo_test.py
"""
import dataCall
import utime
import net


def nw_cb(args):
    global tmp
    global pdp
    pdp = args[0]
    nw_sta = args[1]
    if nw_sta == 1:
        print("*** network %d connected! ***;" % pdp)
        tmp = 1
    else:
        print("*** network %d not connected! ***;" % pdp)
        tmp = 0

def datacall_cb_test():
    a = dataCall.setCallback(nw_cb)
    net.setModemFun(4)
    utime.sleep(1)
    if a == 0 and tmp == 0:
        print("dataCall.setCallback::%s,%s||result_api:: Ture;" % (a, tmp))
    else:
        print("dataCall.setCallback::%s,%s||result_api:: False;" % (a, tmp))
    net.setModemFun(1)
    utime.sleep(1)
    if a == 0 and tmp == 1:
        print("dataCall.setCallback::%s,%s||result_api:: Ture;" % (a, tmp))
    else:
        print("dataCall.setCallback::%s,%s||result_api:: False;" % (a, tmp))

def api_test(i, j, k):
    try:
        utime.sleep(0.05)
        a = dataCall.start(i, j, "3gnet.mnc001.mcc460.gprs", "", "", k)
        b = dataCall.getInfo(i, j)
        if a == 0:
            print("dataCall.setApn::profileIdx[%s],info %s||result_api:: Ture;" % (i, b))
        else:
            print('dataCall.setApn::profileIdx[%s],ip[%s],auth[%s]||result_api:: False;' % (i, j, k))
    except Exception as e:
        print('dataCall.setApn::[error]%s||result_api:: False;'%e)
    try:
        utime.sleep(0.05)
        a = dataCall.start(i, j, "3gnet.mnc001.mcc460.gprs", "", "", k)
        b = dataCall.getInfo(i, j)
        if a == 0:
            print("dataCall.start::profileIdx[%s],info %s||result_api:: Ture;" % (i, b))
        else:
            print('dataCall.start::profileIdx[%s],ip[%s],auth[%s]||result_api:: False;' % (i, j, k))
    except Exception as e:
        print('dataCall.start::[error]%s||result_api:: False;'%e)




if __name__ == '__main__':
    for z in range(3):  # auth_type值0/1/2
        for y in range(3):  # ipv4/ipv6/ipv4&ipv6
            for x in range(1,9):  # profileIdx（1-8）
                api_test(x, y, z)
    datacall_cb_test()
