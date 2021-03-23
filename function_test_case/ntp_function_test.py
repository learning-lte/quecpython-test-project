"""
@Author: Randy.zhu
@Date: 2021-01-19
@LastEditTime: 2021-01-19
@Description: Function test for ntp
@FilePath: Ntp_Function_Test.py
"""
"""
NTP-01	各种网络制式下同步时间正常
NTP-02	无网状态下同步时间
NTP-03	API稳定性压力

"""
import ntptime  # 导入的功能模块
import ure
import utime
import net

cu_mnc_list = ['01','06','09','10']
cmcc_mnc_list = ['00','02','04','07','08','13']
ct_mnc_list = ['03','05','11','12']

class NtpFunctionTest():

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

    def ntp_01_001(self): # 待执行函数
        '''
        查询默认NTP服务器
        :return: info 执行log,result 执行结果
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = ntptime.host
                if info == 'ntp.aliyun.com':
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

    def ntp_01_002(self): # 待执行函数
        '''
        移动AUTO下同步时间正常
        :return: info 执行log,result 执行结果
        '''
        if self.sim == 'CMCC':
            runflag = 1
        else:
            runflag = 0
        result = True
        if runflag:
            try:
                # --------------valid code--------------
                info = net.setConfig(8,0)
                utime.sleep(20)
                info1 = utime.localtime()
                data = ure.search("(\d+), (\d+), (\d+), (\d+), (\d+), (\d+), (\d+), (\d+)",str(info1))
                info2 = ntptime.settime()
                if str(info2) != '0':
                   result = False
                print(result)
                utime.sleep(3)
                info3 = utime.localtime()
                data1 = ure.search("(\d+), (\d+), (\d+), (\d+), (\d+), (\d+), (\d+), (\d+)", str(info3))
                print(data.group(0),data1.group(0))
                print(int(data.group(4)),int(data1.group(4)))
                if not(data.group(0) != data1.group(0) and (int(data.group(4)) - int(data1.group(4)) == 8)):
                    result = False
                info = str(info) +'\r\n'+ str(info1) +'\r\n'+ str(info2) +'\r\n'+ str(info3)
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info,result

    def ntp_01_003(self):  # 待执行函数
        '''
        移动fix4G网络下同步时间正常
        :return: info 执行log,result 执行结果
        '''
        if self.sim == 'CMCC':
            runflag = 1
        else:
            runflag = 0
        result = True
        if runflag:
            try:
                # --------------valid code--------------
                info = net.setConfig(5, 0)
                utime.sleep(15)
                info1 = utime.localtime()
                data = ure.search("(\d+), (\d+), (\d+), (\d+), (\d+), (\d+), (\d+), (\d+)", str(info1))
                info2 = ntptime.settime()
                if str(info2) != '0':
                    result = False
                utime.sleep(3)
                info3 = utime.localtime()
                data1 = ure.search("(\d+), (\d+), (\d+), (\d+), (\d+), (\d+), (\d+), (\d+)", str(info3))
                if not (data.group(0) != data1.group(0) and (int(data.group(4)) == int(data1.group(4)))):
                    result = False
                info = str(info) + '\r\n' + str(info1) + '\r\n' + str(info2) + '\r\n' + str(info3)
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def ntp_01_004(self):  # 待执行函数
        '''
        移动GSM网络下同步时间正常
        :return: info 执行log,result 执行结果
        '''
        if self.sim == 'CMCC':
            runflag = 1
        else:
            runflag = 0
        result = True
        if runflag:
            try:
                # --------------valid code--------------
                info = net.setConfig(0, 0)
                utime.sleep(15)
                info1 = utime.localtime()
                data = ure.search("(\d+), (\d+), (\d+), (\d+), (\d+), (\d+), (\d+), (\d+)", str(info1))
                info2 = ntptime.settime()
                if str(info2) != '0':
                    result = False
                utime.sleep(3)
                info3 = utime.localtime()
                data1 = ure.search("(\d+), (\d+), (\d+), (\d+), (\d+), (\d+), (\d+), (\d+)", str(info3))
                if not (data.group(0) != data1.group(0) and (int(data.group(4)) == int(data1.group(4)))):
                    result = False
                info = str(info) + '\r\n' + str(info1) + '\r\n' + str(info2) + '\r\n' + str(info3)
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def ntp_01_005(self): # 待执行函数
        '''
        联通AUTO下同步时间正常
        :return: info 执行log,result 执行结果
        '''
        if self.sim == 'CU':
            runflag = 1
        else:
            runflag = 0
        result = True
        if runflag:
            try:
                # --------------valid code--------------
                info = net.setConfig(8,0)
                utime.sleep(20)
                info1 = utime.localtime()
                data = ure.search("(\d+), (\d+), (\d+), (\d+), (\d+), (\d+), (\d+), (\d+)",str(info1))
                info2 = ntptime.settime()
                if str(info2) != '0':
                   result = False
                utime.sleep(3)
                info3 = utime.localtime()
                data1 = ure.search("(\d+), (\d+), (\d+), (\d+), (\d+), (\d+), (\d+), (\d+)", str(info3))
                if not(data.group(0) != data1.group(0) and (int(data.group(4)) - int(data1.group(4)) == 8)):
                    result = False
                info = str(info) +'\r\n'+ str(info1) +'\r\n'+ str(info2) +'\r\n'+ str(info3)
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info,result

    def ntp_01_006(self):  # 待执行函数
        '''
        联通fix4G网络下同步时间正常
        :return: info 执行log,result 执行结果
        '''
        if self.sim == 'CU':
            runflag = 1
        else:
            runflag = 0
        result = True
        if runflag:
            try:
                # --------------valid code--------------
                info = net.setConfig(5, 0)
                utime.sleep(15)
                info1 = utime.localtime()
                data = ure.search("(\d+), (\d+), (\d+), (\d+), (\d+), (\d+), (\d+), (\d+)", str(info1))
                info2 = ntptime.settime()
                if str(info2) != '0':
                    result = False
                utime.sleep(3)
                info3 = utime.localtime()
                data1 = ure.search("(\d+), (\d+), (\d+), (\d+), (\d+), (\d+), (\d+), (\d+)", str(info3))
                if not (data.group(0) != data1.group(0) and (int(data.group(4)) == int(data1.group(4)))):
                    result = False
                info = str(info) + '\r\n' + str(info1) + '\r\n' + str(info2) + '\r\n' + str(info3)
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def ntp_01_007(self): # 待执行函数
        '''
        电信AUTO下同步时间正常
        :return: info 执行log,result 执行结果
        '''
        if self.sim == 'CT':
            runflag = 1
        else:
            runflag = 0
        result = True
        if runflag:
            try:
                # --------------valid code--------------
                info = net.setConfig(8,0)
                utime.sleep(20)
                info1 = utime.localtime()
                data = ure.search("(\d+), (\d+), (\d+), (\d+), (\d+), (\d+), (\d+), (\d+)",str(info1))
                info2 = ntptime.settime()
                if str(info2) != '0':
                   result = False
                utime.sleep(3)
                info3 = utime.localtime()
                data1 = ure.search("(\d+), (\d+), (\d+), (\d+), (\d+), (\d+), (\d+), (\d+)", str(info3))
                if not(data.group(0) != data1.group(0) and (int(data.group(4)) - int(data1.group(4)) == 8)):
                    result = False
                info = str(info) +'\r\n'+ str(info1) +'\r\n'+ str(info2) +'\r\n'+ str(info3)
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info,result

    def ntp_01_008(self):  # 待执行函数
        '''
        电信fix4G网络下同步时间正常
        :return: info 执行log,result 执行结果
        '''
        if self.sim == 'CT':
            runflag = 1
        else:
            runflag = 0
        result = True
        if runflag:
            try:
                # --------------valid code--------------
                info = net.setConfig(5, 0)
                utime.sleep(15)
                info1 = utime.localtime()
                data = ure.search("(\d+), (\d+), (\d+), (\d+), (\d+), (\d+), (\d+), (\d+)", str(info1))
                info2 = ntptime.settime()
                if str(info2) != '0':
                    result = False
                utime.sleep(3)
                info3 = utime.localtime()
                data1 = ure.search("(\d+), (\d+), (\d+), (\d+), (\d+), (\d+), (\d+), (\d+)", str(info3))
                if not (data.group(0) != data1.group(0) and (int(data.group(4)) == int(data1.group(4)))):
                    result = False
                info = str(info) + '\r\n' + str(info1) + '\r\n' + str(info2) + '\r\n' + str(info3)
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def ntp_02_001(self):  # 待执行函数
        '''
        无网时同步时间失败
        :return: info 执行log,result 执行结果
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = net.setModemFun(4)
                utime.sleep(3)
                try:
                    info1 = ntptime.settime()
                except BaseException as e:
                    info1 = e

                if str(info1) != 0:
                    result = True
                else:
                    result = False
                info = str(info) + '\r\n' + str(info1)
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def ntp_02_002(self):  # 待执行函数
        '''
        修改NTP服务器再同步
        :return: info 执行log,result 执行结果
        '''
        runflag = 1
        result = True
        if runflag:
            try:
                # --------------valid code--------------
                net.setModemFun(1)
                net.setConfig(8, 0)
                utime.sleep(10)
                info = ntptime.host
                info1 = ntptime.sethost("cn.pool.ntp.org")
                info2 = ntptime.host
                info3 = ntptime.settime()
                if not(info != info2 and info2 == "cn.pool.ntp.org"):
                    result = False
                if str(info3) != '0':
                    result = False
                info = str(info) + '\r\n' + str(info1) + '\r\n' + str(info2) + '\r\n' + str(info3)
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
            ntptime.sethost('ntp.aliyun.com')
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
        self.sim_check()
        case_list = []
        for i in self.method(): # 遍历类中方法
            if 'ntp' in i: # 注意修改此为testcase名称
                case_list.append(i) # 筛选出testcase
        case_list.sort() # testcase排序
        for i in case_list:
            a,b = getattr(self,i)()  # 遍历执行case
            print('%s:: %s||result_case:: %s;'%(i, a, b)) # 输出执行log供外部框架解析
            utime.sleep(3)

if __name__ == '__main__':
    NtpFunctionTest().run()


