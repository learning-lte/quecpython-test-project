"""
@Author: Trent.zhang
@Date: 2021-01-18
@LastEditTime: 2021-01-18
@Description: Function test for dataCall
@FilePath: datacall_Function_Test.py
"""
"""
每次测试跑该test脚本均需要插上三大运营商
需要手动执行查看的有：
    Datacall-01：Datacall-01-02：DataCall-01-01已经可以只需要对比上个版本文件与该文件内容是否一致即可
                 Datacall-01-03之后的全需要手动测试
    Datacall-05： 所有均需手动测试
    Datacall-06: 
    Datacall-08:需要插上物联网卡单独测试
    Datacall-09: 此用例需要插上物联网卡、实网卡需单独插卡测试
    Datacall-10：此大项需要单独手动测试
"""
import dataCall  # 导入的功能模块
import uos
import utime
import net


class DatacallFunctionTest(object):

    def __init__(self):
        pass

    def dataCall_01_001(self): # 待执行函数
        """
        查看是否有apn_cfg.json文件
        :return:
        """
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = uos.listdir('usr')
                if 'apn_cfg.json' in info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def dataCall_01_002(self): # 待执行函数
        """
        查看模块apn_cfg.json文件并查看支持的PLMN号
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                with open('/usr/apn_cfg.json', 'r') as f:
                    info = f.read()
                f.close()
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def dataCall_01_003(self):  # 待执行函数
        """
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def dataCall_01_004(self):  # 待执行函数
        """
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def dataCall_01_005(self):  # 待执行函数
        """
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def dataCall_01_006(self):  # 待执行函数
        """
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def dataCall_01_007(self):  # 待执行函数
        """
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def dataCall_01_008(self):  # 待执行函数
        """
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def dataCall_01_009(self):  # 待执行函数
        """
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def dataCall_01_010(self):  # 待执行函数
        """
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def dataCall_01_011(self):  # 待执行函数
        """
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def dataCall_01_012(self):  # 待执行函数
        """
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def dataCall_01_013(self):  # 待执行函数
        """
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def dataCall_01_014(self):  # 待执行函数
        """
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def dataCall_01_015(self):  # 待执行函数
        """
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def dataCall_01_016(self):  # 待执行函数
        """
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def dataCall_01_017(self):  # 待执行函数
        """
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def dataCall_01_018(self):  # 待执行函数
        """
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def dataCall_01_019(self):  # 待执行函数
        """
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def dataCall_01_020(self):  # 待执行函数
        """
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def dataCall_01_021(self):  # 待执行函数
        """
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def dataCall_01_022(self):  # 待执行函数
        """
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def dataCall_02_001(self):  # 待执行函数
        """
        插入移动卡进行1-8路拨号
        :return:
        """
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                for i in range(1, 9):
                    t1 = utime.time()
                    while 1:
                        t2 = utime.time()
                        if t2 - t1 > 15:
                            break
                        else:
                            a = dataCall.start(i, 0, "3gnet.mnc001.mcc460.gprs", "", "", 0)
                            b = dataCall.getInfo(i, 0)
                            print('#########', a, b, "#######")
                            info.append(a)
                            if a == 0:
                                break
                            else:
                                pass

                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def dataCall_02_002(self):  # 待执行函数
        """
        插入电信卡进行1-8路拨号
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def dataCall_02_003(self):  # 待执行函数
        """
        插入联通卡进行1-8路拨号
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def dataCall_03_001(self):  # 待执行函数
        """
        插入移动卡进行1-8路拨号
        :return:
        """
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                for i in range(1, 9):
                    t1 = utime.time()
                    while 1:
                        t2 = utime.time()
                        if t2 - t1 > 15:
                            break
                        else:
                            a = dataCall.start(i, 1, "3gnet.mnc001.mcc460.gprs", "", "", 0)
                            b = dataCall.getInfo(i, 0)
                            print('#########', a, b, "#######")
                            info.append(a)
                            if a == 0:
                                break
                            else:
                                pass

                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def dataCall_03_002(self):  # 待执行函数
        """
        插入电信卡进行1-8路拨号
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def dataCall_03_003(self):  # 待执行函数
        """
        插入联通卡进行1-8路拨号
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def dataCall_04_001(self):  # 待执行函数
        """
        插入移动卡进行1-8路拨号
        :return:
        """
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                for i in range(1, 9):
                    t1 = utime.time()
                    while 1:
                        t2 = utime.time()
                        if t2 - t1 > 15:
                            break
                        else:
                            a = dataCall.start(i, 2, "3gnet.mnc001.mcc460.gprs", "", "", 0)
                            b = dataCall.getInfo(i, 0)
                            print('#########', a, b, "#######")
                            info.append(a)
                            if a == 0:
                                break
                            else:
                                pass

                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def dataCall_04_002(self):  # 待执行函数
        """
        插入电信卡进行1-8路拨号
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def dataCall_04_003(self):  # 待执行函数
        """
        插入联通卡进行1-8路拨号
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def dataCall_05_001(self):  # 待执行函数
        """
        弱信号下拨号，模块未发生dump
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def dataCall_05_002(self):  # 待执行函数
        """
        使用欠费卡拨号，模块未发生dump
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def dataCall_06_001(self):  # 待执行函数
        """
        三大运营商（IPV4）
        1.配置正确的APN
        2.配置空的APN
        3.配置错误的APN
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                a = dataCall.start(1, 0, "3gnet.mnc001.mcc460.gprs", "", "", 0)
                a_addr = dataCall.getInfo(1, 0)
                a_a = str(a, a_addr)
                b = dataCall.start(1, 0, "", "", "", 0)
                b_addr = dataCall.getInfo(1, 0)
                b_b = str(b, b_addr)
                c = dataCall.start(1, 0, "xxx", "", "", 0)
                c_addr = dataCall.getInfo(1, 0)
                c_c = str(c, c_addr)
                info.append(a_a)
                info.append(b_b)
                info.append(c_c)
                if a == 0 and b == 0 and c == 0:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def dataCall_06_002(self):  # 待执行函数
        """
        三大运营商（IPV6）
        1.配置正确的APN
        2.配置空的APN
        3.配置错误的APN
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                a = dataCall.start(1, 1, "3gnet.mnc001.mcc460.gprs", "", "", 0)
                a_addr = dataCall.getInfo(1, 1)
                a_a = str(a, a_addr)
                b = dataCall.start(1, 1, "", "", "", 0)
                b_addr = dataCall.getInfo(1, 1)
                b_b = str(b, b_addr)
                c = dataCall.start(1, 1, "xxx", "", "", 0)
                c_addr = dataCall.getInfo(1, 1)
                c_c = str(c, c_addr)
                info.append(a_a)
                info.append(b_b)
                info.append(c_c)
                if a == 0 and b == 0 and c == 0:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def dataCall_06_003(self):  # 待执行函数
        """
        三大运营商（IPV4IPV6）
        1.配置正确的APN
        2.配置空的APN
        3.配置错误的APN
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                a = dataCall.start(1, 2, "3gnet.mnc001.mcc460.gprs", "", "", 0)
                a_addr = dataCall.getInfo(1, 2)
                a_a = str(a, a_addr)
                b = dataCall.start(1, 2, "", "", "", 0)
                b_addr = dataCall.getInfo(1, 2)
                b_b = str(b, b_addr)
                c = dataCall.start(1, 2, "xxx", "", "", 0)
                c_addr = dataCall.getInfo(1, 2)
                c_c = str(c, c_addr)
                info.append(a_a)
                info.append(b_b)
                info.append(c_c)
                if a == 0 and b == 0 and c == 0:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def dataCall_07_001(self):  # 待执行函数
        """
        三大运营商（IPV4IPV6）
        1.配置正确的APN
        2.配置空的APN
        3.配置错误的APN
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                for i in range(3):
                    a = dataCall.start(1, 0, "3gnet.mnc001.mcc460.gprs", "", "", i)
                    info.append(a)
                if info[0] == 0 and info[1] == 0 and info[2] == 0:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def dataCall_07_002(self):  # 待执行函数
        """
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def dataCall_07_003(self):  # 待执行函数
        """
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def dataCall_08_001(self):  # 待执行函数
        """
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def dataCall_08_002(self):  # 待执行函数
        """
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def dataCall_08_003(self):  # 待执行函数
        """
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def dataCall_09_001(self):  # 待执行函数
        """
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def dataCall_09_002(self):  # 待执行函数
        """
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def dataCall_09_003(self):  # 待执行函数
        """
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def dataCall_10_001(self):  # 待执行函数
        """
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def dataCall_10_002(self):  # 待执行函数
        """
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def dataCall_10_003(self):  # 待执行函数
        """
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def dataCall_10_004(self):  # 待执行函数
        """
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def dataCall_10_005(self):  # 待执行函数
        """
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def dataCall_10_006(self):  # 待执行函数
        """
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def dataCall_10_007(self):  # 待执行函数
        """
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def dataCall_11_001(self):  # 待执行函数
        """
        设置回调函数
        :return:
        """
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                def nw_cb(args):
                    pdp = args[0]
                    nw_sta = args[1]
                    if nw_sta == 1:
                        print("*** network %d connected! ***" % pdp)
                    else:
                        print("*** network %d not connected! ***" % pdp)
                info = dataCall.setCallback(nw_cb)
                if info == 0:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def dataCall_11_002(self):  # 待执行函数
        """
        cfun0,1切换
        :return:
        """
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                a = net.setModemFun(0)
                a_1 = net.getState()
                a_a = str(a, a_1)
                b = net.setModemFun(1)
                t1 = utime.time()
                while 1:
                    t2 = utime.time()
                    b_1 = net.getState()
                    if t2 - t1 > 15:
                        b_b = str(b, b_1)
                        info.append(b_b)
                        break
                    else:
                        if b_1[1][0] == 1:
                            b_b = str(b, b_1)
                            info.append(b_b)
                            break
                        else:
                            pass

                info.append(a_a)
                if a == 0 and b == 0 and a_1[1][0] == 0 and b_1[1][0] == 1:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def dataCall_11_003(self):  # 待执行函数
        """
        cfun4,1切换
        :return:
        """
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                a = net.setModemFun(4)
                a_1 = net.getState()
                a_a = str(a, a_1)
                b = net.setModemFun(1)
                t1 = utime.time()
                while 1:
                    t2 = utime.time()
                    b_1 = net.getState()
                    if t2 - t1 > 15:
                        b_b = str(b, b_1)
                        info.append(b_b)
                        break
                    else:
                        if b_1[1][0] == 1:
                            b_b = str(b, b_1)
                            info.append(b_b)
                            break
                        else:
                            pass

                info.append(a_a)
                if a == 0 and b == 0 and a_1[1][0] == 0 and b_1[1][0] == 1:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def dataCall_11_004(self):  # 待执行函数
        """
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def method(self):  # 必备函数
        '''
        返回类中除内置方法外的所有方法名
        :return:
        '''
        return (list(filter(lambda m: not m.startswith("__") and not m.endswith("__") and callable(getattr(self, m)),
                            dir(self))))

    def run(self): # 必备函数
        '''
        主执行函数
        :return:
        '''
        case_list = []
        for i in self.method():  # 遍历类中方法
            if 'dataCall' in i:  # 注意修改此为testcase名称
                case_list.append(i)  # 筛选出testcase
        case_list.sort() # testcase排序
        for i in case_list:
            a, b = getattr(self,i)()  # 遍历执行case
            print('%s:: %s||result_case:: %s;' % (i, a, b))  # 输出执行log供外部框架解析
            utime.sleep(3)


if __name__ == '__main__':
    DatacallFunctionTest().run()
