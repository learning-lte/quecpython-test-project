"""
@Author: Ivy.zhang
@Date: 2021-02-19
@LastEditTime: 2021-02-19
@Description: Function test for CellLocator
@FilePath: CellLocator_Function_Test.py
"""
"""
CellLocator for Function

CellLocator-01	各种网络制式下定位正常
CellLocator-02	多路拨号定位正常
CellLocator-03	异常场景下定位失败
CellLocator-04  Quecpython的模块对比高通模块定位信息差异  暂无高通模块
"""
import cellLocator  # 导入的功能模块
import dataCall
import net
import ure
import sys
import utime
import modem
import sim

cu_mnc_list = ['01','06','09','10']
cmcc_mnc_list = ['00','02','04','07','08','13']
ct_mnc_list = ['03','05','11','12']

res_list=[-1,-2,-3,-4,-5,-6,(0.0,0.0,0)]

class CellLocatorFunctionTest():

    def __init__(self):
        pass

    def sim_check(self):
        info1 = str(net.getNetMode())
        if ure.search("0, '460', '(\d+)', 7", str(info1)):  # 判断SIM卡类型
            mnc = str(ure.search("0, '460', '(\d+)', 7", str(info1)).group(1))
            if mnc in cu_mnc_list:
                self.sim = 'CU'
            elif mnc in cmcc_mnc_list:
                self.sim = 'CMCC'
            elif mnc in ct_mnc_list:
                self.sim = 'CT'
            else:
                self.sim = None
        print("sim:",self.sim)


    def cellLocator_01_001(self): # 待执行函数
        '''
        定位前配置IMEI号，服务器以及token正常（服务器以及token默认eaxmple中均配置正确）
        注：需真实的IMEI号
        :return: info 执行log,result 执行结果
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = modem.getDevImei()
                if info == '865501048651732':
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
        return info,result

    def cellLocator_01_002(self): # 待执行函数
        '''
        模块未插卡，定位失败
        :return:
        '''
        self.sim_check()
        if self.sim == None:
            runflag = 1
        else:
            runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = cellLocator.getLocation("www.queclocator.com", 80, "1111111122222222", 8, 1)
                if info == -5:
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

    def cellLocator_01_003(self): # 待执行函数
        '''
        移动AUTO下基站定位正常
        :return:
        '''
        self.sim_check()
        if self.sim == 'CMCC':
            runflag = 1
        else:
            runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info1 = net.setConfig(8, 0)
                info2 = dataCall.start(1, 0, "3gnet.mnc001.mcc460.gprs", "", "", 0)
                utime.sleep(20)
                info3 = cellLocator.getLocation("www.queclocator.com", 80, "1111111122222222", 8, 1)
                info = str(info1) + '\r\n' + str(info2) + '\r\n' + str(info3)
                if info3 not in res_list:
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

    def cellLocator_01_004(self): # 待执行函数
        '''
        移动fix4G网络下基站定位正常
        :return:
        '''
        self.sim_check()
        if self.sim == 'CMCC':
            runflag = 1
        else:
            runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info1 = net.setConfig(5, 0)
                info2 = dataCall.start(1, 0, "3gnet.mnc001.mcc460.gprs", "", "", 0)
                utime.sleep(20)
                info3 = cellLocator.getLocation("www.queclocator.com", 80, "1111111122222222", 8, 1)
                info = str(info1) + '\r\n' + str(info2) + '\r\n' + str(info3)
                if info3 not in res_list:
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

    def cellLocator_01_005(self): # 待执行函数
        '''
        移动GSM网络下基站定位正常
        :return:
        '''
        self.sim_check()
        if self.sim == 'CMCC':
            runflag = 1
        else:
            runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info1 = net.setConfig(0, 0)
                info2 = dataCall.start(1, 0, "3gnet.mnc001.mcc460.gprs", "", "", 0)
                utime.sleep(20)
                info3 = cellLocator.getLocation("www.queclocator.com", 80, "1111111122222222", 8, 1)
                info = str(info1) + '\r\n' + str(info2) + '\r\n' + str(info3)
                if info3 not in res_list:
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


    def cellLocator_01_006(self): # 待执行函数
        '''
        联通AUTO下基站定位正常
        :return:
        '''
        self.sim_check()
        if self.sim == 'CU':
            runflag = 1
        else:
            runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info1 = net.setConfig(8, 0)
                utime.sleep(10)
                info2 = dataCall.start(1, 0, "3gnet.mnc001.mcc460.gprs", "", "", 0)
                utime.sleep(5)
                info3 = cellLocator.getLocation("www.queclocator.com", 80, "1111111122222222", 8, 1)
                info = str(info1) + '\r\n' + str(info2) + '\r\n' + str(info3)
                if info3 not in res_list:
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

    def cellLocator_01_007(self): # 待执行函数
        '''
        联通fix4G网络下基站定位正常
        :return:
        '''
        self.sim_check()
        if self.sim == 'CU':
            runflag = 1
        else:
            runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info1 = net.setConfig(5, 0)
                utime.sleep(5)
                info2 = dataCall.start(1, 0, "3gnet.mnc001.mcc460.gprs", "", "", 0)
                print("info1,info2", info1,info2)
                utime.sleep(5)
                info3 = cellLocator.getLocation("www.queclocator.com", 80, "1111111122222222", 8, 1)
                info = str(info1) + '\r\n' + str(info2) + '\r\n' + str(info3)
                if info3 not in res_list:
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

    def cellLocator_01_008(self): # 待执行函数
        '''
        电信AUTO下基站定位正常
        :return:
        '''
        self.sim_check()
        if self.sim == 'CT':
            runflag = 1
        else:
            runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info1 = net.setConfig(8, 0)
                info2 = dataCall.start(1, 0, "3gnet.mnc001.mcc460.gprs", "", "", 0)
                utime.sleep(20)
                info3 = cellLocator.getLocation("www.queclocator.com", 80, "1111111122222222", 8, 1)
                info = str(info1) + '\r\n' + str(info2) + '\r\n' + str(info3)
                if info3 not in res_list:
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

    def cellLocator_01_009(self): # 待执行函数
        '''
        电信fix4G网络下基站定位正常
        :return:
        '''
        self.sim_check()
        if self.sim == 'CT':
            runflag = 1
        else:
            runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info1 = net.setConfig(5, 0)
                info2 = dataCall.start(1, 0, "3gnet.mnc001.mcc460.gprs", "", "", 0)
                utime.sleep(20)
                info3 = cellLocator.getLocation("www.queclocator.com", 80, "1111111122222222", 8, 1)
                info = str(info1) + '\r\n' + str(info2) + '\r\n' + str(info3)
                if info3 not in res_list:
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

    def cellLocator_01_010(self): # 待执行函数
        '''
        模块放在屏蔽箱里5min,10min,20min
        :return:
        '''
        self.sim_check()
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info1 = net.setConfig(5, 0)
                info2 = dataCall.start(1, 0, "3gnet.mnc001.mcc460.gprs", "", "", 0)
                print("info1,info2", info1,info2)
                utime.sleep(20)
                info3 = cellLocator.getLocation("www.queclocator.com", 80, "1111111122222222", 8, 1)
                info = str(info1) + '\r\n' + str(info2) + '\r\n' + str(info3)
                if info3 not in res_list:
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

        # 拨号成功情况下，获取基站定位

    def cellLocator_02_001(self):  # 待执行函数
        '''
        插入移动卡多路拨号基站定位正常
        :return:
        '''
        self.sim_check()
        if self.sim == 'CMCC':
            runflag = 1
        else:
            runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info1 = []
                info2 = []
                for i in range(1, 9):
                    print("*************第",i,"路*****************")
                    net.setConfig(0, 0)
                    utime.sleep(10)
                    net.setConfig(8, 0)
                    utime.sleep(10)
                    print(dataCall.getInfo(i, 0))
                    a = dataCall.start(i, 0, "3gnet.mnc001.mcc460.gprs", "", "", 0)
                    print(dataCall.getInfo(i, 0))
                    if a == -1:             # 拨号成功情况下，获取基站定位，不成功无法获取基站定位不执行定位
                        continue
                    info1.append(a)
                    utime.sleep(5)
                    b = cellLocator.getLocation("www.queclocator.com", 80, "1111111122222222", 8, 1)
                    info2.append(b)
                    info = str(info1) + '\r' + str(info2)
                    if b not in res_list:
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

    def cellLocator_02_002(self):  # 待执行函数
        '''
        插入联通卡多路拨号基站定位正常
        :return:
        '''
        self.sim_check()
        if self.sim == 'CU':
            runflag = 1
        else:
            runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info1 = []
                info2 = []
                for i in range(1, 9):
                    print("*************第", i, "路*****************")
                    net.setConfig(0, 0)
                    utime.sleep(10)
                    net.setConfig(8, 0)
                    utime.sleep(10)
                    print(dataCall.getInfo(i, 0))
                    a = dataCall.start(i, 0, "3gnet.mnc001.mcc460.gprs", "", "", 0)
                    print(dataCall.getInfo(i, 0))
                    if a == -1:  # 拨号成功情况下，获取基站定位，不成功无法获取基站定位不执行定位
                        continue
                    info1.append(a)
                    utime.sleep(5)
                    b = cellLocator.getLocation("www.queclocator.com", 80, "1111111122222222", 8, 1)
                    info2.append(b)
                    info = str(info1) + '\r' + str(info2)
                    if b not in res_list:
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

    def cellLocator_02_003(self):  # 待执行函数
        '''
        插入电信卡多路拨号基站定位正常
        :return:
        '''
        self.sim_check()
        if self.sim == 'CT':
            runflag = 1
        else:
            runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info1 = []
                info2 = []
                for i in range(1, 9):
                    print("*************第", i, "路*****************")
                    net.setConfig(0, 0)
                    utime.sleep(10)
                    net.setConfig(8, 0)
                    utime.sleep(10)
                    print(dataCall.getInfo(i, 0))
                    a = dataCall.start(i, 0, "3gnet.mnc001.mcc460.gprs", "", "", 0)
                    print(dataCall.getInfo(i, 0))
                    if a == -1:  # 拨号成功情况下，获取基站定位，不成功无法获取基站定位不执行定位
                        continue
                    info1.append(a)
                    utime.sleep(5)
                    b = cellLocator.getLocation("www.queclocator.com", 80, "1111111122222222", 8, 1)
                    info2.append(b)
                    info = str(info1) + '\r' + str(info2)
                    if b not in res_list:
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

    def cellLocator_03_001(self): # 待执行函数
        '''
        设置超时时间，定位超时定位失败
        :return: info 执行log,result 执行结果
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = cellLocator.getLocation("www.queclocator.com", 300, "1111111122222222", 8, 1)
                if info == (0.0,0.0,0):
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

    def cellLocator_03_002(self): # 待执行函数
        '''
        配置错误的IMEI号定位失败
        :return: info 执行log,result 执行结果
        '''
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = cellLocator.getLocation("www.queclocator.com", 300, "1111111122222222", 8, 1)
                if info == (0.0,0.0,0):
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

    def cellLocator_03_003(self): # 待执行函数
        '''
        配置错误的token定位失败
        :return: info 执行log,result 执行结果
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = cellLocator.getLocation("www.queclocator.com", 300, "1111111122222222", 8, 1)
                if info == (0.0,0.0,0):
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

    def cellLocator_03_004(self): # 待执行函数
        '''
        配置错误的服务器信息定位失败
        :return: info 执行log,result 执行结果
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = cellLocator.getLocation("xxx", 80, "1111111122222222", 8, 1)
                if info == (0.0,0.0,0):
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


    def method(self): # 必备函数
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
        for i in self.method(): # 遍历类中方法
            if 'cellLocator' in i: # 注意修改此为testcase名称
                case_list.append(i) # 筛选出testcase
        case_list.sort() # testcase排序
        for i in case_list:
            a,b = getattr(self,i)()  # 遍历执行case
            print('%s:: %s||result_case:: %s;'%(i, a, b)) # 输出执行log供外部框架解析
            utime.sleep(3)

if __name__ == '__main__':
    net.setConfig(8, 0)             #防止其他脚本执行后网络制式被固定，此脚本运行不了
    CellLocatorFunctionTest().run()


