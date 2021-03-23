"""
@Author: Randy.zhu
@Date: 2021-01-12
@LastEditTime: 2021-01-12
@Description: Function test for demo
@FilePath: Demo_Function_Test.py
"""
"""
Demo for Function
改造测试用例时可参考此Demo
"""
import xxx  # 导入的功能模块
import sys
import utime

class XXXXXXX():

    def __init__(self):
        pass

    def xxx_01_001(self): # 待执行函数
        '''
        :return: info 执行log,result 执行结果
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = xxx.fun()
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
        return info,result

    def xxx_01_002(self): # 待执行函数
        '''
        暂无法py层实现发送at指令
        :return:
        '''
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = xxx.fun()
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
            if 'xxx' in i: # 注意修改此为testcase名称
                case_list.append(i) # 筛选出testcase
        case_list.sort() # testcase排序
        for i in case_list:
            a,b = getattr(self,i)()  # 遍历执行case
            print('%s:: %s||result_case:: %s;'%(i, a, b)) # 输出执行log供外部框架解析
            utime.sleep(3)

if __name__ == '__main__':
    XXXXXXX().run()


