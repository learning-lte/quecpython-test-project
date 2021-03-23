"""
@Author: Randy.zhu
@Date: 2021-02-03
@LastEditTime: 2021-02-03
@Description: Function test for log
@FilePath: Log_Function_Test.py
"""
"""
LOG-01	各种网络制式下同步时间正常
LOG-02	无网状态下同步时间
LOG-03	API稳定性压力

"""
import log  # 导入的功能模块
import ure
import utime
import uos

cu_mnc_list = ['01','06','09','10']
cmcc_mnc_list = ['00','02','04','07','08','13']
ct_mnc_list = ['03','05','11','12']

class LogFunctionTest():

    def __init__(self):
        pass

    def log_01_001(self): # 待执行函数
        '''
        默认log输出级别
        :return: info 执行log,result 执行结果
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = log.basicConfig()
                if info == None:
                    info = 'log.basicConfig()'
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

    def log_01_002(self): # 待执行函数
        '''
        创建log对象
        :return: info 执行log,result 执行结果
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                self.testlog = log.getLogger('test')
                if self.testlog:
                    info = "self.testlog = log.getLogger('test')"
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

    def log_01_003(self): # 待执行函数
        '''
        创建log1对象
        :return: info 执行log,result 执行结果
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                self.testlog1 = log.getLogger('test1')
                if self.testlog1:
                    info = "self.testlog1 = log.getLogger('test1')"
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

    def log_01_004(self): # 待执行函数
        '''
        输出 debug 级别的日志
        :return: info 执行log,result 执行结果
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = self.testlog.debug('this is debug message;')
                info1 = self.testlog1.debug('this is debug message;')
                if info == info1 == None:
                    info = "self.testlog.debug('this is debug message')"
                    info1 = "self.testlog1.debug('this is debug message')"
                    info = info +'\r\n'+info1
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

    def log_01_005(self): # 待执行函数
        '''
        输出 info 级别的日志
        :return: info 执行log,result 执行结果
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = self.testlog.info('this is info message;')
                info1 = self.testlog1.info('this is info message;')
                if info == info1 == None:
                    info = "self.testlog.debug('this is info message')"
                    info1 = "self.testlog1.debug('this is info message')"
                    info = info +'\r\n'+info1
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

    def log_01_006(self): # 待执行函数
        '''
        输出 warning 级别的日志
        :return: info 执行log,result 执行结果
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = self.testlog.warning('this is warning message;')
                info1 = self.testlog1.warning('this is warning message;')
                if info == info1 == None:
                    info = "self.testlog.warning('this is warning message')"
                    info1 = "self.testlog1.warning('this is warning message')"
                    info = info +'\r\n'+info1
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

    def log_01_007(self): # 待执行函数
        '''
        输出 error 级别的日志
        :return: info 执行log,result 执行结果
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = self.testlog.error('this is error message;')
                info1 = self.testlog1.error('this is error message;')
                if info == info1 == None:
                    info = "self.testlog.error('this is error message')"
                    info1 = "self.testlog1.error('this is error message')"
                    info = info +'\r\n'+info1
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

    def log_01_008(self): # 待执行函数
        '''
        输出 critical 级别的日志
        :return: info 执行log,result 执行结果
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = self.testlog.critical('this is critical message;')
                info1 = self.testlog1.critical('this is critical message;')
                if info == info1 == None:
                    info = "self.testlog.critical('this is critical message')"
                    info1 = "self.testlog1.critical('this is critical message')"
                    info = info +'\r\n'+info1
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

    def log_01_009(self): # 待执行函数
        '''
        返回不存在name的log对象
        :return: info 执行log,result 执行结果
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                self.testlog2 = log.getLogger()
                if self.testlog2:
                    info = "self.testlog2 = log.getLogger()"
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

    def log_01_010(self): # 待执行函数
        '''
        输出不同级别的日志
        :return: info 执行log,result 执行结果
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = self.testlog2.debug('this is debug message;')
                info1 = self.testlog2.info('this is info message;')
                info2 = self.testlog2.warning('this is warning message;')
                info3 = self.testlog2.error('this is error message;')
                info4 = self.testlog2.critical('this is critical message;')
                if info == info1 == info2 == info3 == info4 == None:
                    info = "self.testlog2.debug('this is debug message')"
                    info1 = "self.testlog2.info('this is info message')"
                    info2 = "self.testlog2.warning('this is warning message')"
                    info3 = "self.testlog2.error('this is error message')"
                    info4 = "self.testlog2.critical('this is critical message')"
                    info = info +'\r\n'+info1+'\r\n'+info2+'\r\n'+info3+'\r\n'+info4
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

    def log_02_001(self):  # 待执行函数
        '''
        更改log输出级别为NOTSET
        :return: info 执行log,result 执行结果
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = log.basicConfig(log.NOTSET)
                if info == None:
                    info = 'log.basicConfig(log.NOTSET)'
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

    def log_02_002(self): # 待执行函数
        '''
        输出不同级别的日志
        :return: info 执行log,result 执行结果
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = self.testlog2.debug('this is debug message;')
                info1 = self.testlog2.info('this is info message;')
                info2 = self.testlog2.warning('this is warning message;')
                info3 = self.testlog2.error('this is error message;')
                info4 = self.testlog2.critical('this is critical message;')
                if info == info1 == info2 == info3 == info4 == None:
                    info = "self.testlog2.debug('this is debug message')"
                    info1 = "self.testlog2.info('this is info message')"
                    info2 = "self.testlog2.warning('this is warning message')"
                    info3 = "self.testlog2.error('this is error message')"
                    info4 = "self.testlog2.critical('this is critical message')"
                    info = info +'\r\n'+info1+'\r\n'+info2+'\r\n'+info3+'\r\n'+info4
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

    def log_02_003(self):  # 待执行函数
        '''
        更改log输出级别为DEBUG
        :return: info 执行log,result 执行结果
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = log.basicConfig(log.DEBUG)
                if info == None:
                    info = 'log.basicConfig(log.DEBUG)'
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

    def log_02_004(self): # 待执行函数
        '''
        输出不同级别的日志
        :return: info 执行log,result 执行结果
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = self.testlog2.debug('this is debug message;')
                info1 = self.testlog2.info('this is info message;')
                info2 = self.testlog2.warning('this is warning message;')
                info3 = self.testlog2.error('this is error message;')
                info4 = self.testlog2.critical('this is critical message;')
                if info == info1 == info2 == info3 == info4 == None:
                    info = "self.testlog2.debug('this is debug message')"
                    info1 = "self.testlog2.info('this is info message')"
                    info2 = "self.testlog2.warning('this is warning message')"
                    info3 = "self.testlog2.error('this is error message')"
                    info4 = "self.testlog2.critical('this is critical message')"
                    info = info +'\r\n'+info1+'\r\n'+info2+'\r\n'+info3+'\r\n'+info4
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

    def log_02_005(self):  # 待执行函数
        '''
        更改log输出级别为INFO
        :return: info 执行log,result 执行结果
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = log.basicConfig(log.INFO)
                if info == None:
                    info = 'log.basicConfig(log.INFO)'
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

    def log_02_006(self): # 待执行函数
        '''
        输出不同级别的日志
        :return: info 执行log,result 执行结果
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = self.testlog2.debug('this is debug message;')
                info1 = self.testlog2.info('this is info message;')
                info2 = self.testlog2.warning('this is warning message;')
                info3 = self.testlog2.error('this is error message;')
                info4 = self.testlog2.critical('this is critical message;')
                if info == info1 == info2 == info3 == info4 == None:
                    info = "self.testlog2.debug('this is debug message')"
                    info1 = "self.testlog2.info('this is info message')"
                    info2 = "self.testlog2.warning('this is warning message')"
                    info3 = "self.testlog2.error('this is error message')"
                    info4 = "self.testlog2.critical('this is critical message')"
                    info = info +'\r\n'+info1+'\r\n'+info2+'\r\n'+info3+'\r\n'+info4
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

    def log_02_007(self):  # 待执行函数
        '''
        更改log输出级别为WARNING
        :return: info 执行log,result 执行结果
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = log.basicConfig(log.WARNING)
                if info == None:
                    info = 'log.basicConfig(log.WARNING)'
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

    def log_02_008(self): # 待执行函数
        '''
        输出不同级别的日志
        :return: info 执行log,result 执行结果
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = self.testlog2.debug('this is debug message;')
                info1 = self.testlog2.info('this is info message;')
                info2 = self.testlog2.warning('this is warning message;')
                info3 = self.testlog2.error('this is error message;')
                info4 = self.testlog2.critical('this is critical message;')
                if info == info1 == info2 == info3 == info4 == None:
                    info = "self.testlog2.debug('this is debug message')"
                    info1 = "self.testlog2.info('this is info message')"
                    info2 = "self.testlog2.warning('this is warning message')"
                    info3 = "self.testlog2.error('this is error message')"
                    info4 = "self.testlog2.critical('this is critical message')"
                    info = info +'\r\n'+info1+'\r\n'+info2+'\r\n'+info3+'\r\n'+info4
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

    def log_02_009(self):  # 待执行函数
        '''
        更改log输出级别为ERROR
        :return: info 执行log,result 执行结果
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = log.basicConfig(log.ERROR)
                if info == None:
                    info = 'log.basicConfig(log.ERROR)'
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

    def log_02_010(self): # 待执行函数
        '''
        输出不同级别的日志
        :return: info 执行log,result 执行结果
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = self.testlog2.debug('this is debug message;')
                info1 = self.testlog2.info('this is info message;')
                info2 = self.testlog2.warning('this is warning message;')
                info3 = self.testlog2.error('this is error message;')
                info4 = self.testlog2.critical('this is critical message;')
                if info == info1 == info2 == info3 == info4 == None:
                    info = "self.testlog2.debug('this is debug message')"
                    info1 = "self.testlog2.info('this is info message')"
                    info2 = "self.testlog2.warning('this is warning message')"
                    info3 = "self.testlog2.error('this is error message')"
                    info4 = "self.testlog2.critical('this is critical message')"
                    info = info +'\r\n'+info1+'\r\n'+info2+'\r\n'+info3+'\r\n'+info4
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

    def log_02_011(self):  # 待执行函数
        '''
        更改log输出级别为CRITICAL
        :return: info 执行log,result 执行结果
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = log.basicConfig(log.CRITICAL)
                if info == None:
                    info = 'log.basicConfig(log.CRITICAL)'
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

    def log_02_012(self): # 待执行函数
        '''
        输出不同级别的日志
        :return: info 执行log,result 执行结果
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = self.testlog2.debug('this is debug message;')
                info1 = self.testlog2.info('this is info message;')
                info2 = self.testlog2.warning('this is warning message;')
                info3 = self.testlog2.error('this is error message;')
                info4 = self.testlog2.critical('this is critical message;')
                if info == info1 == info2 == info3 == info4 == None:
                    info = "self.testlog2.debug('this is debug message')"
                    info1 = "self.testlog2.info('this is info message')"
                    info2 = "self.testlog2.warning('this is warning message')"
                    info3 = "self.testlog2.error('this is error message')"
                    info4 = "self.testlog2.critical('this is critical message')"
                    info = info +'\r\n'+info1+'\r\n'+info2+'\r\n'+info3+'\r\n'+info4
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

    def log_03_001(self): # 待执行函数
        '''
        特殊字符数据输出测试
        :return: info 执行log,result 执行结果
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = log.basicConfig(log.INFO)
                info1 = self.testlog2.info('~!@#$%^&*()_+<>?/*- ;')
                if info == info1 == None:
                    info = "self.testlog2.info('~!@#$%^&*()_+<>?/*- ')"
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

    def log_03_002(self): # 待执行函数
        '''
        超长数据输出测试
        :return: info 执行log,result 执行结果
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                b = uos.urandom(262145)
                info = self.testlog2.info(str(b)+';')
                if info == None:
                    info = "self.testlog2.info('this is long data(256k)')"
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

    def log_03_003(self): # 待执行函数
        '''
        非str数据输出测试
        :return: info 执行log,result 执行结果
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = self.testlog2.info(1234)
                self.testlog2.info(';')
                if info == None:
                    info = "self.testlog2.info(1234)"
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
            if 'log' in i: # 注意修改此为testcase名称
                case_list.append(i) # 筛选出testcase
        case_list.sort() # testcase排序
        for i in case_list:
            a,b = getattr(self,i)()  # 遍历执行case
            print('%s:: %s||result_case:: %s;'%(i, a, b)) # 输出执行log供外部框架解析
            utime.sleep(3)

if __name__ == '__main__':
    LogFunctionTest().run()


