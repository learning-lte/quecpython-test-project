"""
@Author: Randy.zhu
@Date: 2021-01-14
@LastEditTime: 2021-01-14
@Description: Function test for network
@FilePath: network_function_test.py
"""
"""
network for Function
Network-01	检查模块的默认BAND正确
Network-02	设置CFUN状态0,1,4，查询注网状态
Network-03	弱信号下（不插天线），移动联通电信卡LTE网络下，屏蔽箱屏蔽10min正常（确认是否会Dump，恢复信号后注网正常）
Network-04	使用电信/移动/联通物联网卡固定不同的网络制式，查询注网状态，网络时间，信号强度，小区访问状态，运营商信息，与实际一致
Network-05	不同网络制式下，小区信息查询
Network-06	无卡、无信号、有卡锁PIN下、欠费卡，查询注网状态，网络时间，信号强度，小区访问状态，运营商信息，与实际一致
Network-07	未激活的物联网卡，首次插入模块自动激活流程测试
Network-08	根据spec支持的band固定检查可以正常找网


"""
import net
import utime
import ure
import sim

cu_mnc_list = ['01','06','09','10']
cmcc_mnc_list = ['00','02','04','07','08','13']
ct_mnc_list = ['03','05','11','12']

class NetworkFunctionTest():

    def __init__(self):
        pass

    def network_01_001(self):
        '''
        检查模块的默认BAND是否正确
        :return: info 执行log,result 执行结果
        '''
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = ''
                result = ''
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info,result

    def network_01_002(self):
        '''
        检查模块的默认网络配置模式
        :return: info 执行log,result 执行结果
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = net.getConfig()
                if (8, False) == info:
                    info1 = str(net.getNetMode())
                    if ure.search("0, '460', '(\d+)', 7",str(info1)): # 判断SIM卡类型
                        mnc = str(ure.search("0, '460', '(\d+)', 7", str(info1)).group(1))
                        result = True
                        if mnc in cu_mnc_list:
                            self.sim = 'CU'
                        elif mnc in cmcc_mnc_list:
                            self.sim = 'CMCC'
                        elif mnc in ct_mnc_list:
                            self.sim = 'CT'
                        else:
                            self.sim = None
                            result = False

                    else:
                        result = False
                    info = str(info)+'\r\n'+str(info1)
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

    def network_01_003(self):
        '''
        检查模块的默认CFUN状态
        :return: info 执行log,result 执行结果
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = net.getModemFun()
                if str(info) == '1':
                    result = True
                else:
                    result = False
                ##########################
                # at接口暂未开放 AT+CFUN后续补充查询
                ##########################
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info,result

    def network_02_001(self):
        '''
        设置飞行模式
        :return: info 执行log,result 执行结果
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                result = True
                info = net.setModemFun(4)
                if str(info) != '0':
                    result = False
                utime.sleep(3)
                info1 = net.getModemFun()
                if str(info1) != '4':
                    result = False
                utime.sleep(3)
                ##########################
                # at接口暂未开放 AT+CFUN后续补充查询
                ##########################
                info2 = sim.getStatus()
                if str(info2) != '1':
                    result = False
                info3 = net.getConfig()
                if str(info3) == '-1':
                    result = False
                info4 = net.operatorName()
                if str(info4) == '-1':
                    result = False
                info5 = net.getState()
                if str(info5) == '-1':
                    result = False
                info6 = net.getSignal()
                if str(info6) == '-1':
                    result = False
                info7 = net.csqQueryPoll()
                if str(info7) != '99':
                    result = False
                info = str(info)+'\r\n'+str(info1)+'\r\n'+str(info2)+'\r\n'+str(info3)+'\r\n'+str(info4)+'\r\n'+str(info5)+'\r\n'+str(info6)+'\r\n'+str(info7)
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info,result

    def network_02_002(self):
        '''
        设置最小功能模式
        :return: info 执行log,result 执行结果
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                result = True
                info = net.setModemFun(0)
                if str(info) != '0':
                    result = False
                utime.sleep(3)
                info1 = net.getModemFun()
                if str(info1) != '0':
                    result = False
                utime.sleep(3)
                ##########################
                # at接口暂未开放 AT+CFUN后续补充查询
                ##########################
                info2 = sim.getStatus()
                if str(info2) == '1':
                    result = False
                info3 = net.getConfig()
                if str(info3) == '-1':
                    result = False
                info4 = net.operatorName()
                if str(info4) == '-1':
                    result = False
                info5 = net.getState()
                if str(info5) == '-1':
                    result = False
                info6 = net.getSignal()
                if str(info6) == '-1':
                    result = False
                info7 = net.csqQueryPoll()
                if str(info7) != '99':
                    result = False
                info = str(info)+'\r\n'+str(info1)+'\r\n'+str(info2)+'\r\n'+str(info3)+'\r\n'+str(info4)+'\r\n'+str(info5)+'\r\n'+str(info6)+'\r\n'+str(info7)
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info,result

    def network_02_003(self):
        '''
        设置全功能模式
        :return: info 执行log,result 执行结果
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                result = True
                info = net.setModemFun(1)
                if str(info) != '0':
                    result = False
                utime.sleep(10)
                info1 = net.getModemFun()
                if str(info1) != '1':
                    result = False
                utime.sleep(3)
                ##########################
                # at接口暂未开放 AT+CFUN后续补充查询
                ##########################
                info2 = sim.getStatus()
                if str(info2) != '1':
                    result = False
                info3 = net.getConfig()
                if str(info3) == '-1':
                    result = False
                info4 = net.operatorName()
                if str(info4) == '-1':
                    result = False
                info5 = net.getState()
                if str(info5) == '-1':
                    result = False
                info6 = net.getSignal()
                if str(info6) == '-1':
                    result = False
                info7 = net.csqQueryPoll()
                if str(info7) == '99':
                    result = False
                info = str(info)+'\r\n'+str(info1)+'\r\n'+str(info2)+'\r\n'+str(info3)+'\r\n'+str(info4)+'\r\n'+str(info5)+'\r\n'+str(info6)+'\r\n'+str(info7)
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info,result

    def network_03_001(self):
        '''
        移动联通电信卡LTE网络下，屏蔽箱屏蔽10min正常（确认是否会Dump）
        :return: info 执行log,result 执行结果
        '''
        runflag = 0
        if runflag:
            # --------------valid code--------------
            try:
                info = '因暂缺少接口发送at问题，无法实现'
                if info == '864430010001091':
                    result = True
                else:
                    result = False
            except BaseException as e:
                info = e
                result = False
            # --------------valid code--------------
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def network_04_001(self):
        '''
        电信设置LTE only网络，调用接口查询状态，与AT对比
        :return: info 执行log,result 执行结果
        '''
        if self.sim == 'CT':
            runflag = 1
        else:
            runflag = 0
        result = True
        if runflag:
            # --------------valid code--------------
            try:
                info = net.setConfig(5,1)
                if str(info) != '0':
                    result = False
                utime.sleep(10)
                info3 = net.getConfig()
                if str(info3) != '(5, True)':
                    result = False
                info4 = net.operatorName()
                if str(info4) != "('CHN-CT', 'CT', '460', '11')":
                    result = False
                info5 = net.getState()
                if str(info5) != '-1':
                    data = ure.search("[(\d+), (\d+), (\d+), (\d), (\d+), (\d+)], [(\d+), (\d+), (\d+), (\d), (\d+), (\d+)]", str(info5))
                    if str(data.group(1)) != '11':
                        result = False
                    if str(data.group(4)) != '7':
                        result = False
                    if str(data.group(7)) != '1':
                        result = False
                    if str(data.group(10)) != '7':
                        result = False
                else:
                    result = False
                info6 = net.getSignal()
                if str(info6) == '-1':
                    result = False
                info7 = net.nitzTime()
                if not(ure.search("('21/(\d+)/(\d+),(\d+):(\d+):(\d+)+32', (\d+)), 0)", str(info7))):
                    result = False
                info8 = net.csqQueryPoll()
                if str(info8) == '-1' and str(info8) != '99':
                    result = False
                ##########################
                # at接口暂未开放 AT+COPS? AT+QENG="SERVINGCELL"后续补充查询
                ##########################
                info = str(info) + '\r\n' + str(info3) + '\r\n' + str(
                    info4) + '\r\n' + str(info5) + '\r\n' + str(info6) + '\r\n' + str(info7) + '\r\n' + str(info8)
            except BaseException as e:
                info = e
                result = False
            # --------------valid code--------------
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def network_04_002(self):
        '''
        移动设置LTE only网络，调用接口查询状态，与AT对比
        :return: info 执行log,result 执行结果
        '''
        if self.sim == 'CMCC':
            runflag = 1
        else:
            runflag = 0
        result = True
        if runflag:
            # --------------valid code--------------
            try:
                info = net.setConfig(5,1)
                if str(info) != '0':
                    result = False
                utime.sleep(10)
                info3 = net.getConfig()
                if str(info3) != '(5, True)':
                    result = False
                info4 = net.operatorName()
                if str(info4) != "('CHINA MOBILE', 'CMCC', '460', '00')":
                    result = False
                info5 = net.getState()
                if str(info5) != '-1':
                    data = ure.search(
                        "\[(\d+), (\d+), (\d+), (\d), (\d+), (\d+)], \[(\d+), (\d+), (\d+), (\d), (\d+), (\d+)]",
                        str(info5))
                    if data:
                        if str(data.group(1)) != '6':
                            result = False
                        if str(data.group(4)) != '7':
                            result = False
                        if str(data.group(7)) != '1':
                            result = False
                        if str(data.group(10)) != '7':
                            result = False
                    else:
                        result = False
                else:
                    result = False
                info6 = net.getSignal()
                if str(info6) == '-1':
                    result = False
                info7 = net.nitzTime()
                if not (ure.search("('21/(\d+)/(\d+),(\d+):(\d+):(\d+)\+32', (\d+), 0)", str(info7))):
                    result = False
                info8 = net.csqQueryPoll()
                if str(info8) == '-1' and str(info8) != '99':
                    result = False
                ##########################
                # at接口暂未开放 AT+COPS? AT+QENG="SERVINGCELL"后续补充查询
                ##########################
                info = str(info) + '\r\n' + str(info3) + '\r\n' + str(
                    info4) + '\r\n' + str(info5) + '\r\n' + str(info6) + '\r\n' + str(info7) + '\r\n' + str(info8)
            except BaseException as e:
                info = e
                result = False
            # --------------valid code--------------
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def network_04_003(self):
        '''
        移动设置GSM only网络，调用接口查询状态，与AT对比
        :return: info 执行log,result 执行结果
        '''
        if self.sim == 'CMCC':
            runflag = 1
        else:
            runflag = 0
        result = True
        if runflag:
            # --------------valid code--------------
            try:
                info = net.setConfig(0,1)
                if str(info) != '0':
                    result = False
                utime.sleep(20)
                info3 = net.getConfig()
                if str(info3) != '(0, True)':
                    result = False
                info4 = net.operatorName()
                if str(info4) != "('CHINA MOBILE', 'CMCC', '460', '00')":
                    result = False
                info5 = net.getState()
                if str(info5) != '-1':
                    data = ure.search(
                        "\[(\d+), (\d+), (\d+), (\d), (\d+), (\d+)], \[(\d+), (\d+), (\d+), (\d), (\d+), (\d+)]",
                        str(info5))
                    if str(data.group(1)) != '1':
                        result = False
                    if str(data.group(4)) != '3':
                        result = False
                    if str(data.group(7)) != '1':
                        result = False
                    if str(data.group(10)) != '3':
                        result = False
                else:
                    result = False
                info6 = net.getSignal()
                if str(info6) == '-1':
                    result = False
                info7 = net.nitzTime()
                if not (ure.search("('21/(\d+)/(\d+),(\d+):(\d+):(\d+)\+32', (\d+), 0)", str(info7))):
                    result = False
                info8 = net.csqQueryPoll()
                if str(info8) == '-1' and str(info8) != '99':
                    result = False
                ##########################
                # at接口暂未开放 AT+COPS? AT+QENG="SERVINGCELL"后续补充查询
                ##########################
                info = str(info) + '\r\n' + str(info3) + '\r\n' + str(
                    info4) + '\r\n' + str(info5) + '\r\n' + str(info6) + '\r\n' + str(info7) + '\r\n' + str(info8)
            except BaseException as e:
                info = e
                result = False
            # --------------valid code--------------
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def network_04_004(self):
        '''
        联通设置LTE only网络，调用接口查询状态，与AT对比
        :return: info 执行log,result 执行结果
        '''
        if self.sim == 'CU':
            runflag = 1
        else:
            runflag = 0
        result = True
        if runflag:
            # --------------valid code--------------
            try:
                info = net.setConfig(5,1)
                if str(info) != '0':
                    result = False
                utime.sleep(20)
                info3 = net.getConfig()
                if str(info3) != '(5, True)':
                    result = False
                info4 = net.operatorName()
                if str(info4) != "('CHINA UNICOM', 'CU', '460', '01')":
                    result = False
                info5 = net.getState()
                if str(info5) != '-1':
                    data = ure.search(
                        "\[(\d+), (\d+), (\d+), (\d), (\d+), (\d+)], \[(\d+), (\d+), (\d+), (\d), (\d+), (\d+)]",
                        str(info5))
                    if str(data.group(1)) != '6':
                        result = False
                    if str(data.group(4)) != '7':
                        result = False
                    if str(data.group(7)) != '1':
                        result = False
                    if str(data.group(10)) != '7':
                        result = False
                else:
                    result = False
                info6 = net.getSignal()
                if str(info6) == '-1':
                    result = False
                info7 = net.nitzTime()
                if not (ure.search("('21/(\d+)/(\d+),(\d+):(\d+):(\d+)\+32', (\d+), 0)", str(info7))):
                    result = False
                info8 = net.csqQueryPoll()
                if str(info8) == '-1' and str(info8) != '99':
                    result = False
                ##########################
                # at接口暂未开放 AT+COPS? AT+QENG="SERVINGCELL"后续补充查询
                ##########################
                info = str(info) + '\r\n' + str(info3) + '\r\n' + str(
                    info4) + '\r\n' + str(info5) + '\r\n' + str(info6) + '\r\n' + str(info7) + '\r\n' + str(info8)
            except BaseException as e:
                info = e
                result = False
            # --------------valid code--------------
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def network_04_005(self):
        '''
        联通设置GSM only网络，调用接口查询状态，与AT对比
        :return: info 执行log,result 执行结果
        '''
        # 国内联网GSM已退网，无法注册，不再测试
        if self.sim == 'CU':
            runflag = 1
        else:
            runflag = 0
        result = True
        if runflag:
            # --------------valid code--------------
            try:
                info = net.setConfig(0,1)
                if str(info) != '0':
                    result = False
                utime.sleep(10)
                info3 = net.getConfig()
                if str(info3) != '(0, True)':
                    result = False
                info4 = net.operatorName()
                if str(info4) != "('CHINA MOBILE', 'CMCC', '460', '00')":
                    result = False
                info5 = net.getState()
                if str(info5) != '-1':
                    data = ure.search(
                        "\[(\d+), (\d+), (\d+), (\d), (\d+), (\d+)], \[(\d+), (\d+), (\d+), (\d), (\d+), (\d+)]",
                        str(info5))
                    if str(data.group(1)) != '1':
                        result = False
                    if str(data.group(4)) != '3':
                        result = False
                    if str(data.group(7)) != '1':
                        result = False
                    if str(data.group(10)) != '3':
                        result = False
                else:
                    result = False
                info6 = net.getSignal()
                if str(info6) == '-1':
                    result = False
                info7 = net.nitzTime()
                if not (ure.search("('21/(\d+)/(\d+),(\d+):(\d+):(\d+)\+32', (\d+), 0)", str(info7))):
                    result = False
                info8 = net.csqQueryPoll()
                if str(info8) == '-1' and str(info8) != '99':
                    result = False
                ##########################
                # at接口暂未开放 AT+COPS? AT+QENG="SERVINGCELL"后续补充查询
                ##########################
                info = str(info) + '\r\n' + str(info3) + '\r\n' + str(
                    info4) + '\r\n' + str(info5) + '\r\n' + str(info6) + '\r\n' + str(info7) + '\r\n' + str(info8)
            except BaseException as e:
                info = e
                result = False
            # --------------valid code--------------
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def network_05_001(self):
        '''
        2G网络下查询小区信息
        :return: info 执行log,result 执行结果
        '''
        if self.sim == 'CMCC':
            runflag = 1
        else:
            runflag = 0
        result = True
        if runflag:
            # --------------valid code--------------
            try:
                info = net.setConfig(0,1)
                if str(info) != '0':
                    result = False
                utime.sleep(20)
                info3 = net.getCellInfo()
                data = ure.search("\((\d), (\d+), (\d+), (\d), (\d+), (\d+), (\d+), (\-\d+)\)",str(info3))
                if data:
                    flag = data.group(1)
                    cid = data.group(2)
                    mcc = data.group(3)
                    mnc = data.group(4)
                    lac = data.group(5)
                    arfcn = data.group(6)
                    bsic = data.group(7)
                    rssi = data.group(8)
                else:
                    result = False
                info4 = net.getCi()
                if type(info4) is list:
                    if str(info4[0]) != cid:
                        result = False
                else:
                    result = False
                info5 = net.getMnc()
                if type(info5) is list:
                    if str(info5[0]) != mnc:
                        result = False
                else:
                    result = False
                info6 = net.getMcc()
                if type(info6) is list:
                    if str(info6[0]) != mcc:
                        result = False
                else:
                    result = False
                info7 = net.getLac()
                if type(info7) is list:
                    if str(info7[0]) != lac:
                        result = False
                else:
                    result = False
                info8 = net.getSignal()
                if type(info8) is tuple:
                    if str(info8[0][0]) != rssi:
                        info8 = str(info8) + 'signal_rssi: %s,cell_rssi: %s' % (info8[1][0], rssi)
                        result = False
                else:
                    result = False
                ##########################
                # at接口暂未开放 AT+QENG="SERVINGCELL"后续补充查询
                ##########################
                info = str(info) + '\r\n' + str(info3) + '\r\n' + str(
                    info4) + '\r\n' + str(info5) + '\r\n' + str(info6) + '\r\n' + str(info7) + '\r\n' + str(info8)
            except BaseException as e:
                info = e
                result = False
            # --------------valid code--------------
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def network_05_002(self):
        '''
        4G网络下查询小区信息
        :return: info 执行log,result 执行结果
        '''
        runflag = 1
        result = True
        if runflag:
            # --------------valid code--------------
            try:
                info = net.setConfig(5,1)
                if str(info) != '0':
                    result = False
                utime.sleep(15)
                info3 = net.getCellInfo()
                data = ure.search("\((\d+), (\d+), (\d+), (\d), (\d+), (\d+), (\d+), (\-\d+)\)",str(info3))
                if data:
                    flag = data.group(1)
                    cid = data.group(2)
                    mcc = data.group(3)
                    mnc = data.group(4)
                    pci = data.group(5)
                    tac = data.group(6)
                    earfcn = data.group(7)
                    rssi = data.group(8)
                else:
                    result = False
                info4 = net.getCi()
                if type(info4) is list:
                    if str(info4[0]) != cid:
                        result = False
                else:
                    result = False
                info5 = net.getMnc()
                if type(info5) is list:
                    if str(info5[0]) != mnc:
                        result = False
                else:
                    result = False
                info6 = net.getMcc()
                if type(info6) is list:
                    if str(info6[0]) != mcc:
                        result = False
                else:
                    result = False
                info7 = net.getLac()
                if type(info7) is list:
                    if str(info7[0]) != tac:
                        result = False
                else:
                    result = False
                info8 = net.getSignal()
                if type(info8) is tuple:
                    if str(info8[1][0]) != rssi:
                        info8 = str(info8) + 'signal_rssi: %s,cell_rssi: %s'%(info8[1][0],rssi)
                        result = False
                else:
                    result = False
                ##########################
                # at接口暂未开放 AT+QENG="SERVINGCELL"后续补充查询
                ##########################
                info = str(info) + '\r\n' + str(info3) + '\r\n' + str(
                    info4) + '\r\n' + str(info5) + '\r\n' + str(info6) + '\r\n' + str(info7) + '\r\n' + str(info8)
            except BaseException as e:
                info = e
                result = False
            # --------------valid code--------------
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def network_06_001(self): # 待执行函数
        '''
        无卡状态下，调用接口查询状态，与AT对比
        :return:
        '''
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = net.getConfig()
                if info == '864430010001091':
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

    def network_06_002(self): # 待执行函数
        '''
        无信号下，调用接口查询状态，与AT对比
        :return:
        '''
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = net.getConfig()
                if info == '864430010001091':
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

    def network_06_003(self): # 待执行函数
        '''
        锁PIN下，调用接口查询状态，与AT对比
        :return:
        '''
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = net.getConfig()
                if info == '864430010001091':
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

    def network_06_004(self): # 待执行函数
        '''
        欠费卡，调用接口查询状态，与AT对比
        :return:
        '''
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = net.getConfig()
                if info == '864430010001091':
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

    def network_07_001(self): # 待执行函数
        '''
        未激活的电信物联网卡
        :return:
        '''
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = net.getConfig()
                if info == '864430010001091':
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

    def network_07_002(self): # 待执行函数
        '''
        未激活的移动物联网卡
        :return:
        '''
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = net.getConfig()
                if info == '864430010001091':
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

    def network_07_003(self): # 待执行函数
        '''
        未激活的联通物联网卡
        :return:
        '''
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = net.getConfig()
                if info == '864430010001091':
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

    def run(self):  # 必备函数
        '''
        主执行函数
        :return:
        '''
        case_list = []
        for i in self.method():  # 遍历类中方法
            if 'network' in i:  # 注意修改此为testcase名称
                case_list.append(i)  # 筛选出testcase
        case_list.sort()  # testcase排序
        for i in case_list:
            a, b= getattr(self, i)()  # 遍历执行case
            print('%s:: %s||result_case:: %s;' % (i, a, b))  # 输出执行log供外部框架解析
            utime.sleep(3)
        net.setConfig(8, 0)

if __name__ == '__main__':
    Net = NetworkFunctionTest()
    Net.run()

