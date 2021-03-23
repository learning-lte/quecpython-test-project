# -- coding: UTF-8 --
"""
@Author: Randy.zhu
@Date: 2021-01-13
@LastEditTime: 2021-01-13
@Description: Function test for fs
@FilePath: Fs_Function_Test.py
"""
"""
Fs for Function
FileSystem-01	文件访问：打开、写入、读取、关闭文件
FileSystem-02	文件夹创建、切换、重命名、删除、查看
FileSystem-03	文件上传、读写速率
FileSystem-04	上传重复文件、空间满后继续上传文件、上传过程中随机断电
FileSystem-05	验证开启交互保护，重启、上传后仍为开启状态
FileSystem-06	基本接口测试脚本
FileSystem-07	FS读写稳定性压力测试
"""
import uos  # 导入的功能模块
import utime
import ure
import modem

class Fs_Function_Test():

    def __init__(self):
        pass

    def fs_01_001(self): # 待执行函数
        '''
        新建一个文件
        :return: info 执行log,result 执行结果
        '''
        runflag = 1
        if runflag:
            # --------------valid code--------------
            try:
                self.f = open('/usr/1','w+')
                info = "f = open('/usr/1','w+')"
                result = True
            except BaseException as e:
                info = e
                result = False
            # --------------valid code--------------
        else:
            info = 'N/A'
            result = 'N/A'
        return info,result

    def fs_01_002(self): # 待执行函数
        '''
        写入英文与数字内容
        :return: info 执行log,result 执行结果
        '''
        runflag = 1
        if runflag:
            # --------------valid code--------------
            try:
                self.data = 'abcdefghijklmnopqrstuvwxyz123456789'
                info = self.f.write(self.data)
                info = "f = open('/usr/1','w+')\r\n"+str(info)
                result = True
            except BaseException as e:
                info = e
                result = False
            # --------------valid code--------------
        else:
            info = 'N/A'
            result = 'N/A'
        return info,result

    def fs_01_003(self): # 待执行函数
        '''
        关闭文件
        :return: info 执行log,result 执行结果
        '''
        runflag = 1
        if runflag:
            # --------------valid code--------------
            try:
                self.f.close()
                info = "f.close()"
                result = True
            except BaseException as e:
                info = e
                result = False
            # --------------valid code--------------
        else:
            info = 'N/A'
            result = 'N/A'
        return info,result

    def fs_01_004(self): # 待执行函数
        '''
        打开已存在文件
        :return: info 执行log,result 执行结果
        '''
        runflag = 1
        if runflag:
            # --------------valid code--------------
            try:
                self.f = open('/usr/1','r')
                info = "f = open('/usr/1','r')\r\n"
                re_data = self.f.read()
                info = info+str(re_data)+'\r\n'
                self.f.close()
                info = info + "f.close()"
                if re_data == self.data:
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

    def fs_01_005(self): # 待执行函数
        '''
        写入中文与特殊符号内容
        :return: info 执行log,result 执行结果
        '''
        runflag = 1
        if runflag:
            # --------------valid code--------------
            try:
                self.data = '移远通信~！@#￥%……&*（）,.*-+'
                self.f = open('/usr/1','w')
                info = "f = open('/usr/1','w')\r\n"
                self.f.write(self.data)
                info = info+"f.write('移远通信~！@#￥%……&*（）,.*-+')\r\n"
                self.f.close()
                info = info + "f.close()"
                result = True
            except BaseException as e:
                info = e
                result = False
            # --------------valid code--------------
        else:
            info = 'N/A'
            result = 'N/A'
        return info,result

    def fs_01_006(self): # 待执行函数
        '''
        打开已存在文件
        :return: info 执行log,result 执行结果
        '''
        runflag = 1
        if runflag:
            # --------------valid code--------------
            try:
                self.f = open('/usr/1','r')
                info = "f = open('/usr/1','r')\r\n"
                re_data = self.f.read()
                info = info+str(re_data)+'\r\n'
                self.f.close()
                info = info + "f.close()"
                if re_data == self.data:
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

    def fs_02_001(self): # 待执行函数
        '''
        创建文件夹
        :return:
        '''
        runflag = 1
        if runflag:
            # --------------valid code--------------
            try:
                uos.mkdir('/usr/user')
                info = "uos.mkdir('/usr/user')"
                result = True
            except BaseException as e:
                info = e
                result = False
            # --------------valid code--------------
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def fs_02_002(self): # 待执行函数
        '''
        列出当前目录文件
        :return:
        '''
        runflag = 1
        if runflag:
            # --------------valid code--------------
            try:
                info = uos.listdir('/usr')
                if info != []:
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

    def fs_02_003(self): # 待执行函数
        '''
        切换目录
        :return:
        '''
        runflag = 1
        if runflag:
            # --------------valid code--------------
            try:
                uos.chdir('/usr/user')
                info = "uos.chdir('/usr/user')"
                result = True
            except BaseException as e:
                info = e
                result = False
            # --------------valid code--------------
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def fs_02_004(self): # 待执行函数
        '''
        获取当前路径
        :return:
        '''
        runflag = 1
        if runflag:
            # --------------valid code--------------
            try:
                info = uos.getcwd()
                if info == '/usr/user':
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

    def fs_02_005(self):  # 待执行函数
        '''
        切换目录
        :return:
        '''
        runflag = 1
        if runflag:
            # --------------valid code--------------
            try:
                uos.chdir('/usr')
                info = "uos.chdir('/usr')"
                result = True
            except BaseException as e:
                info = e
                result = False
            # --------------valid code--------------
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def fs_02_006(self):  # 待执行函数
        '''
        重命名文件.文件夹
        :return:
        '''
        runflag = 1
        if runflag:
            # --------------valid code--------------
            try:
                uos.rename('1', '2')
                info = "uos.rename('1', '2')\r\n"
                uos.rename('user', 'user1')
                info = info+"uos.rename('user', 'user1')\r\n"
                data = uos.listdir()
                info = info + str(data)
                if 'user1' in data:
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

    def fs_02_007(self):  # 待执行函数
        '''
        删除文件.文件夹
        :return:
        '''
        runflag = 1
        if runflag:
            # --------------valid code--------------
            try:
                uos.remove('2')
                info = "uos.remove('2')\r\n"
                uos.rmdir('user1')
                info = info+"uos.rmdir('user1')\r\n"
                data = uos.listdir()
                info = info + str(data)
                if 'user1' not in data and '2' not in data:
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

    def fs_02_008(self):  # 待执行函数
        '''
        删除文件.文件夹
        :return:
        '''
        runflag = 1
        if runflag:
            # --------------valid code--------------
            try:
                info = uos.stat('/usr')
                if info == (16384, 0, 0, 0, 0, 0, 0, 0, 0, 0):
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

    def fs_02_009(self):  # 待执行函数
        '''
        删除文件.文件夹
        :return:
        '''
        runflag = 1
        if runflag:
            # --------------valid code--------------
            try:
                info = uos.statvfs('/usr')
                res = ure.search("4096, 4096, (\d+), (\d+), (\d+), 0, 0, 0, 0, 255", str(info))
                if res:
                    totalsize = res.group(1)
                    freesize = res.group(2)
                    info = str(info) + '\r\ntotalsize: %s Mb\r\nfreesize: %s Mb'%(4096*int(totalsize)/1024/1024,4096*int(freesize)/1024/1024)
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

    def fs_02_010(self):  # 待执行函数
        '''
        获取关于底层信息或其操作系统的信息
        :return:
        '''
        runflag = 1
        if runflag:
            # --------------valid code--------------
            try:
                info = uos.uname()
                if modem.getDevModel() in str(info):
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

    def fs_02_011(self):  # 待执行函数
        '''
        返回具有n个随机字节的bytes对象
        :return:
        '''
        runflag = 1
        if runflag:
            # --------------valid code--------------
            try:
                info = uos.urandom(8)
                if info:
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

    def fs_03_001(self):  # 待执行函数
        '''
        上传文件
        :return:
        '''
        runflag = 0
        if runflag:
            # --------------valid code--------------
            try:
                info = uos.urandom(8)
                if info:
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

    def fs_03_002(self):  # 待执行函数
        '''
        统计读写速率
        :return:
        '''
        runflag = 0
        if runflag:
            # --------------valid code--------------
            try:
                info = uos.urandom(8)
                if info:
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

    def fs_04_001(self):  # 待执行函数
        '''
        上传重复文件
        :return:
        '''
        runflag = 0
        if runflag:
            # --------------valid code--------------
            try:
                info = uos.urandom(8)
                if info:
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

    def fs_04_002(self):  # 待执行函数
        '''
        上传过程中随机断电
        :return:
        '''
        runflag = 0
        if runflag:
            # --------------valid code--------------
            try:
                info = uos.urandom(8)
                if info:
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

    def fs_04_003(self):  # 待执行函数
        '''
        空间满后继续上传文件
        :return:
        '''
        runflag = 0
        if runflag:
            # --------------valid code--------------
            try:
                info = uos.urandom(8)
                if info:
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

    def fs_05_001(self):  # 待执行函数
        '''
        开启子线程运行
        :return:
        '''
        runflag = 0
        if runflag:
            # --------------valid code--------------
            try:
                info = uos.urandom(8)
                if info:
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

    def fs_05_002(self):  # 待执行函数
        '''
        开启交互保护，不影响内部程序运行
        :return:
        '''
        runflag = 0
        if runflag:
            # --------------valid code--------------
            try:
                info = uos.urandom(8)
                if info:
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

    def fs_05_003(self):  # 待执行函数
        '''
        交互保护立即生效，无法输入任何指令
        :return:
        '''
        runflag = 0
        if runflag:
            # --------------valid code--------------
            try:
                info = uos.urandom(8)
                if info:
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

    def fs_05_004(self):  # 待执行函数
        '''
        重启模块，交互保护不会失效，不影响内部程序运行
        :return:
        '''
        runflag = 0
        if runflag:
            # --------------valid code--------------
            try:
                info = uos.urandom(8)
                if info:
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

    def fs_05_005(self):  # 待执行函数
        '''
        重新烧录固件包，交互保护取消
        :return:
        '''
        runflag = 0
        if runflag:
            # --------------valid code--------------
            try:
                info = uos.urandom(8)
                if info:
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

    def fs_06_001(self):  # 待执行函数
        '''
        基本接口测试脚本执行
        :return:
        '''
        runflag = 0
        if runflag:
            # --------------valid code--------------
            try:
                info = uos.urandom(8)
                if info:
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

    def fs_07_001(self):  # 待执行函数
        '''
        单个接口稳定性压力
        :return:
        '''
        runflag = 0
        if runflag:
            # --------------valid code--------------
            try:
                info = uos.urandom(8)
                if info:
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

    def fs_07_002(self):  # 待执行函数
        '''
        反复上传文件至空间满后清空
        :return:
        '''
        runflag = 0
        if runflag:
            # --------------valid code--------------
            try:
                info = uos.urandom(8)
                if info:
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

    def fs_07_003(self):  # 待执行函数
        '''
        反复上传文件至空间满后清空，上传过程中随机断电
        :return:
        '''
        runflag = 0
        if runflag:
            # --------------valid code--------------
            try:
                info = uos.urandom(8)
                if info:
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
            if 'fs' in i: # 注意修改此为testcase名称
                case_list.append(i) # 筛选出testcase
        case_list.sort() # testcase排序
        for i in case_list:
            a,b = getattr(self,i)()  # 遍历执行case
            print('%s:: %s||result_case:: %s;'%(i, a, b)) # 输出执行log供外部框架解析
            utime.sleep(3)

if __name__ == '__main__':
    Fs_Function_Test().run()
