"""
@Author: Trent.zhang
@Date: 2021-01-12
@LastEditTime: 2021-01-12
@Description: Function test for demo
@FilePath: Demo_Function_Test.py
"""
"""
Socket_01_001:根据测试用例是不插卡，本测试为了方便自动化，需要插卡设置无网状态即可
Socket_01_002：同上无需插卡因为开始已经插卡，切换有网即可
Socket_01_003: 模块需重启只要保证手机卡找网正常即可
Socket_03；Socket_04；Socket_05；Socket_06:socket的IPV6创建对象报错暂时存在问题无法测试
Socket_07：暂时需要手动测试
Socket_08:十六进制特殊字符不支持
"""
import usocket  # 导入的功能模块
import net
import utime
import dataCall


class SocketFunctionTest(object):
    def __init__(self):
        self.HOST = '220.180.239.212'
        self.PORT = 8305
        self.BUFSIZ = 1024
        self.value = 10
        self.msg = 'hello'

    def Socket_01_001(self): # 待执行函数
        """
        :return: 模块做客户端，建立TCP方式的连接，收发数据
        """
        runflag = 1
        if runflag:
            tcp_client_socket = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM)
            try:
                # --------------valid code--------------
                net.setModemFun(0)
                utime.sleep(0.5)
                tcp_client_socket.settimeout(self.value)
                info = tcp_client_socket.connect((self.HOST, self.PORT))
                tcp_client_socket.close()
                if info:
                    result = False
                else:
                    result = True
                # --------------valid code--------------
            except BaseException as e:
                tcp_client_socket.close()
                info = e
                result = True
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def Socket_01_002(self):  # 待执行函数
        """
        插入手机卡
        :return:
        """
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                a = net.setModemFun(1)
                info.append(a)
                t1 = utime.time()
                while True:
                    b = net.getState()
                    t2 = utime.time()
                    if t2-t1 > 15:
                        info.append(b)
                        break
                    elif b[1][0] == 1:
                        info.append(b)
                        break
                    else:
                        pass
                if info[0] == 0 and info[1][1][0] == 1:
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

    def Socket_01_003(self):  # 待执行函数
        """
        插入手机卡
        :return:
        """
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                a = net.setModemFun(1)
                info.append(a)
                t1 = utime.time()
                while True:
                    b = net.getState()
                    t2 = utime.time()
                    if t2-t1 > 15:
                        info.append(b)
                        break
                    elif b[1][0] == 1:
                        info.append(b)
                        break
                    else:
                        pass
                if info[0] == 0 and info[1][1][0] == 1:
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

    def Socket_01_004(self):  # 待执行函数
        """
        使用IP地址，建立TCP连接（域名，ip:端口）
        :return:
        """
        runflag = 1
        if runflag:
            # 1.创建tcp_client_socket 套接字对象
            tcp_client_socket = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM)
            try:
                # --------------valid code--------------
                # 2.连接服务器
                tcp_client_socket.connect((self.HOST, self.PORT))
                tcp_client_socket.send(self.msg)
                info = tcp_client_socket.recv(self.BUFSIZ)
                utime.sleep(0.5)
                tcp_client_socket.close()
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                tcp_client_socket.close()
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def Socket_01_005(self):  # 待执行函数
        """
        使用IP地址，建立TCP连接（域名，ip:端口）
        :return:
        """
        runflag = 1
        if runflag:
            try:
                info = []
                # --------------valid code--------------
                # 1.创建tcp_client_socket 套接字对象
                tcp_client_socket = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM)
                # 作为客户端，主动连接服务器较多，一般不需要绑定端口
                tcp_client_socket.settimeout(self.value)
                # 2.连接服务器
                tcp_client_socket.connect((self.HOST, self.PORT))
                for i in range(10):
                    tcp_client_socket.send(self.msg.encode())
                    a = tcp_client_socket.recv(self.BUFSIZ)
                    info.append(a)
                    utime.sleep(0.05)
                tcp_client_socket.close()
                if len(info) == 10:
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

    def Socket_01_006(self):  # 待执行函数
        """
        模块多路拨号（1-8路）
        :return:
        """
        runflag = 1
        msg = 'hello'
        if runflag:
            try:
                info = []
                # --------------valid code--------------
                for i in range(1, 9):
                    for i in range(1, 9):
                        t1 = utime.time()
                        while 1:
                            t2 = utime.time()
                            if t2 - t1 > 15:
                                break
                            else:
                                a = dataCall.start(i, 0, "3gnet.mnc001.mcc460.gprs", "", "", 0)
                                b = dataCall.getInfo(i, 0)
                                if a == 0:
                                    tcp_client_socket = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM)
                                    # 作为客户端，主动连接服务器较多，一般不需要绑定端口
                                    tcp_client_socket.settimeout(self.value)
                                    # 2.连接服务器
                                    tcp_client_socket.connect((self.HOST, self.PORT))
                                    tcp_client_socket.send(msg.encode())
                                    info = tcp_client_socket.recv(self.BUFSIZ)
                                    info.append(a)
                                    utime.sleep(0.05)
                                    m = tcp_client_socket.close()
                                    info.append(m)
                                    break
                                else:
                                    pass
                if len(info) == 10:
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

    def Socket_02_001(self):  # 待执行函数
        """
        使用IP地址，建立TCP连接
        :return:
        """
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                client = usocket.socket(usocket.AF_INET, usocket.SOCK_DGRAM)
                ip_port = (self.HOST, self.PORT)
                client.sendto(self.msg, ip_port)
                data, server_addr = client.recvfrom(self.BUFSIZ)
                info = data.decode('utf-8')
                client.close()
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

    def Socket_02_002(self):  # 待执行函数
        """
        模块多路拨号（1-8路）
        :return:
        """
        runflag = 1
        if runflag:
            try:
                info = []
                # --------------valid code--------------
                for i in range(1, 9):
                    for i in range(1, 9):
                        t1 = utime.time()
                        while 1:
                            t2 = utime.time()
                            if t2 - t1 > 15:
                                break
                            else:
                                a = dataCall.start(i, 0, "3gnet.mnc001.mcc460.gprs", "", "", 0)
                                if a == 0:
                                    client = usocket.socket(usocket.AF_INET, usocket.SOCK_DGRAM)
                                    ip_port = (self.HOST, self.PORT)
                                    client.sendto(self.msg, ip_port)
                                    data, server_addr = client.recvfrom(self.BUFSIZ)
                                    m = data.decode('utf-8')
                                    info.append(m)
                                    client.close()
                                    break
                                else:
                                    pass
                if len(info) == 10:
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

    def Socket_03_001(self):  # 待执行函数
        """
        使用IP地址，建立TCP连接（域名，ip:端口）
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                t1 = utime.time()
                info = []
                while 1:
                    t2 = utime.time()
                    if t2 - t1 > 15:
                        break
                    else:
                        a = dataCall.start(1, 1, "3gnet.mnc001.mcc460.gprs", "", "", 0)
                        b = dataCall.getInfo(1, 1)
                        print('1')
                        if a == 0 and b[2][0] == 1:
                            info.append(a)
                            print('2')
                            # 1.创建tcp_client_socket 套接字对象
                            tcp_client_socket = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM)
                            # 作为客户端，主动连接服务器较多，一般不需要绑定端口
                            tcp_client_socket.settimeout(self.value)
                            # 2.连接服务器
                            tcp_client_socket.connect((self.HOST, self.PORT))
                            print('3')
                            tcp_client_socket.send(self.msg.encode())
                            m = tcp_client_socket.recv(self.BUFSIZ)
                            info.append(m)
                            print('5')
                            utime.sleep(0.05)
                            tcp_client_socket.close()
                            break
                        else:
                            pass
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                print('erro')
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def Socket_03_002(self):  # 待执行函数
        """
        使用IP地址，建立TCP连接（域名，ip:端口）
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                # 1.创建tcp_client_socket 套接字对象
                tcp_client_socket = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM)
                # 作为客户端，主动连接服务器较多，一般不需要绑定端口
                tcp_client_socket.settimeout(self.value)
                # 2.连接服务器
                tcp_client_socket.connect((self.HOST, self.PORT))
                tcp_client_socket.send(self.msg.encode())
                info = tcp_client_socket.recv(self.BUFSIZ)
                utime.sleep(0.05)
                tcp_client_socket.close()
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

    def Socket_03_003(self):  # 待执行函数
        """
        使用IP地址，建立TCP连接（域名，ip:端口）
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                # 1.创建tcp_client_socket 套接字对象
                tcp_client_socket = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM)
                # 作为客户端，主动连接服务器较多，一般不需要绑定端口
                tcp_client_socket.settimeout(self.value)
                # 2.连接服务器
                tcp_client_socket.connect((self.HOST, self.PORT))
                tcp_client_socket.send(self.msg.encode())
                info = tcp_client_socket.recv(self.BUFSIZ)
                utime.sleep(0.05)
                tcp_client_socket.close()
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

    def Socket_04_001(self):  # 待执行函数
        """
        使用IP地址，建立TCP连接（域名，ip:端口）
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = 'IPV6有问题暂时无法测试'
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

    def Socket_05_001(self): # 待执行函数
        '''
        :return: info 执行log,result 执行结果
        '''
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
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

    def Socket_06_001(self):  # 待执行函数
        '''
        :return: info 执行log,result 执行结果
        '''
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
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

    def Socket_07_001(self):  # 待执行函数
        '''
        :return: info 执行log,result 执行结果
        '''
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
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

    def Socket_07_002(self):  # 待执行函数
        '''
        :return: info 执行log,result 执行结果
        '''
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
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

    def Socket_07_003(self):  # 待执行函数
        '''
        :return: info 执行log,result 执行结果
        '''
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
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

    def Socket_07_004(self):  # 待执行函数
        '''
        :return: info 执行log,result 执行结果
        '''
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
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

    def Socket_07_005(self):  # 待执行函数
        '''
        :return: info 执行log,result 执行结果
        '''
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
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

    def Socket_07_006(self):  # 待执行函数
        '''
        :return: info 执行log,result 执行结果
        '''
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
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

    def Socket_07_007(self):  # 待执行函数
        '''
        :return: info 执行log,result 执行结果
        '''
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
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

    def Socket_08_001(self):  # 待执行函数
        """
        模块发送不固定长度数据，发送十六进制特殊字符
        //08：往前删除一个字符
        1A：ctrl+z，结束输入，发送数据
        1B：Esc，取消发送
        00：NUL空格符
        0A：LF换行
        0D：CR回车
        7F：DEL删除
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
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

    def Socket_08_002(self):  # 待执行函数
        """
        1.输入十六进制：0100081A
        2.输入十六进制：000A081A
        3.输入十六进制：000D081A
        4.输入十六进制：001A081A
        5.输入十六进制：007F081A
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
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

    def Socket_08_003(self):  # 待执行函数
        """
        模块发送不固定长度00-FF的十六进制数据，参照数据sheet页00-FF
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
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

    def Socket_08_004(self):  # 待执行函数
        """
        模块发送固定长度数据1024字节
        :return:
        """
        runflag = 1
        if runflag:
            try:
                msg = 'STARTBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBEND'
                # --------------valid code--------------
                tcp_client_socket = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM)
                tcp_client_socket.connect((self.HOST, self.PORT))
                tcp_client_socket.send(msg)
                info = tcp_client_socket.recv(1024).decode('utf-8')
                tcp_client_socket.close()
                if info == msg:
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

    def Socket_08_005(self):  # 待执行函数
        """
        模块发送固定长度数据1056字节
        :return:
        """
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                msg = 'startaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaend'
                tcp_client_socket = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM)
                tcp_client_socket.connect((self.HOST, self.PORT))
                tcp_client_socket.send(msg)
                info = tcp_client_socket.recv(1056).decode('utf-8')
                tcp_client_socket.close()
                if info == msg:
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

    def Socket_08_006(self):  # 待执行函数
        """
        模块发送固定长度数据1460字节
        :return:
        """
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                msg = 'STARTBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBEND'  # --------------valid code--------------
                tcp_client_socket = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM)
                tcp_client_socket.connect((self.HOST, self.PORT))
                tcp_client_socket.send(msg)
                info = tcp_client_socket.recv(1460).decode('utf-8')
                tcp_client_socket.close()
                if info == msg:
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

    def Socket_09_001(self):  # 待执行函数
        """
        模块放入屏蔽箱静置一段时间取出，模块手动建立TCP连接正常
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
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

    def Socket_09_002(self):  # 待执行函数
        """
        模块放入屏蔽箱静置一段时间取出，模块手动建立TCP连接正常
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
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

    def Socket_09_003(self):  # 待执行函数
        """
        模块放入屏蔽箱静置一段时间取出，模块手动建立TCP连接正常
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
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
            if 'Socket' in i:  # 注意修改此为testcase名称
                case_list.append(i)  # 筛选出testcase
        case_list.sort()  # testcase排序
        for i in case_list:
            a, b = getattr(self, i)()  # 遍历执行case
            print('%s:: %s||result_case:: %s;' % (i, a, b))  # 输出执行log供外部框架解析
            utime.sleep(3)


if __name__ == '__main__':
    SocketFunctionTest().run()


