"""
@Author: Randy.zhu
@Date: 2021-01-08
@LastEditTime: 2021-01-13
@Description: Function test for modem
@FilePath: Modem_Function_Test.py
"""
"""
Modem for Function
MODEM-01	设置读取模块IMEI正确
MODEM-02	读取模块版本号正确(注意不要有V号)
MODEM-03	读取Model正确(与项目名称保持一致即可)
MODEM-04	读取SN正确
MODEM-05	查询product_id

"""
import modem
import utime

class ModemFunctionTest():

    def __init__(self):
        pass

    def modem_01_001(self):
        '''
        接口读取模块IMEI号正确
        :return: info 执行log,result 执行结果
        '''
        runflag = 1
        if runflag:
            # --------------valid code--------------
            try:
                info = modem.getDevImei()
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
        return info,result

    def modem_01_002(self):
        '''
        AT设置模块IMEI号成功
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

    def modem_01_003(self):
        '''
        接口读取模块IMEI号为设置后的值
        :return: info 执行log,result 执行结果
        '''
        runflag = 1
        if runflag:
            # --------------valid code--------------
            try:
                info = modem.getDevImei()
                if info == '864430010001080':
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
        return info,result

    def modem_01_004(self):
        '''
        AT查询模块IMEI号正确
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

    def modem_02_001(self):
        '''
        接口读取模块版本号正确
        :return: info 执行log,result 执行结果
        '''
        runflag = 1
        if runflag:
            # --------------valid code--------------
            try:
                info = modem.getDevFwVersion()
                if 'PY' in info:
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
        return info,result

    def modem_02_002(self):
        '''
        AT查询设备型号
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

    def modem_03_001(self):
        '''
        接口读取Model正确
        :return: info 执行log,result 执行结果
        '''
        runflag = 1
        if runflag:
            # --------------valid code--------------
            try:
                info = modem.getDevModel()
                if len(info) > 4:
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
        return info,result

    def modem_03_002(self):
        '''
        AT读取Model正确
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

    def modem_04_001(self):
        '''
        接口读取SN正确
        :return: info 执行log,result 执行结果
        '''
        runflag = 1
        if runflag:
            # --------------valid code--------------
            try:
                info = modem.getDevSN()
                if info == '':
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
        return info,result

    def modem_04_002(self):
        '''
        AT设置SN成功
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

    def modem_04_003(self):
        '''
        接口读取SN为设置后的值
        :return: info 执行log,result 执行结果
        '''
        runflag = 1
        if runflag:
            # --------------valid code--------------
            try:
                info = modem.getDevSN()
                if info == 'P1D19GS1E000113':
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
        return info,result

    def modem_04_004(self):
        '''
        AT查询SN正确
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

    def modem_05_001(self):
        '''
        接口读取product_id正确
        :return: info 执行log,result 执行结果
        '''
        runflag = 1
        if runflag:
            # --------------valid code--------------
            try:
                info = modem.getDevProductId()
                if info == 'Quectel':
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
        return info,result

    def modem_05_002(self):
        '''
        AT读取product_id正确
        :return: info 执行log,result 执行结果
        '''
        runflag = 0
        if runflag:
            # --------------valid code--------------
            try:
                info = '因暂缺少接口发送at问题，无法实现'
                if info == 'Quectel':
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
            if 'modem' in i:  # 注意修改此为testcase名称
                case_list.append(i)  # 筛选出testcase
        case_list.sort()  # testcase排序
        for i in case_list:
            a, b= getattr(self, i)()  # 遍历执行case
            print('%s:: %s||result_case:: %s;' % (i, a, b))  # 输出执行log供外部框架解析
            utime.sleep(3)

if __name__ == '__main__':
    ModemFunctionTest().run()

