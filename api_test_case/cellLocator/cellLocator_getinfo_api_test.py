# coding: utf-8
"""
@Author: trent.zhang
@Date: 2020-10-12
@LastEditTime: 2020-10-12 10:25:08
@Description: example for module cellLocator
@FilePath: cellLocator_getinfo_api_test.py
"""
import dataCall
import cellLocator
import utime


def api_test(i):
    """
    执行该脚本前需要设置正确的IMEI号
    :param i:
    :return:
    """
    try:
        utime.sleep(0.05)
        if i == 0:
            pass
        else:
            a = dataCall.setApn(i, 0, '3gnet.mnc001.mcc460.gprs', '', '', 0)
            b = cellLocator.getLocation('www.queclocator.com', 80, '1111111122222222', 8, i)

            if a == 0:
                if b == "(0.0, 0.0, 0)":
                    print('profileIdx[%s]::||result_api:: False;' % i)
                else:
                    print("profileIdx[%s]:: %s||result_api:: Ture;" % (i, b))
            else:
                print('profileIdx[%s]::||result_api:: False;' % i)

    except Exception as e:
        print('cellLocator.getLocation::[error]%s||result_api: False;'%e)


if __name__ == '__main__':
        for x in range(9):  # profileIdx（1-8）
            api_test(x)
