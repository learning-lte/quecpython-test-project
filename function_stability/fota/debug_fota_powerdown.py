#!/usr/bin/env python
# -*- coding=utf-8 -*-
# @Time    : 2020/9/1 13:31
# @Author  : Loren.jia
# @FileName: debug_fota_powerdown.py
# @Software: PyCharm
import re
import urllib.request
import http.cookiejar
from urllib import request
import time
import threading
import serial
import mybuffer
from dataclasses import dataclass
import datetime
import serial.tools.list_ports

time_str = str(datetime.datetime.now())[:19]
time1 = datetime.datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')


# now = time.strftime('%Y%m%d%H%M%s',now)
def time_format():
    '''
    格式化时间
    :return: 返回一个格式化的时间 如2019_06_27_09_24_30
    '''
    time_str = str(datetime.datetime.now())[0:19]
    time1 = datetime.datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')
    # 根据字符串本身的格式进行转换
    time2 = time1.strftime('%Y_%m_%d_%H_%M_%S')
    # 装换成需要的格式2019_06_27_09_24_30
    return time2


name = "DEBUG" + time_format() + ".log"
name2 = "RESULT" + time_format() + ".log"
name3 = "AT" + time_format() + ".log"
f = open(name, "w+")
RESULT = open(name2, "w+")
AT = open(name3, "w+")


def debuglog(data):
    # pass
    # print(data)
    f.write(f"[{str(datetime.datetime.now())}] {data.strip().lstrip()}\n")
    f.flush()

def ATlog(data):
    # pass
    # print(data)
    AT.write(f"[{str(datetime.datetime.now())}] {data.strip().lstrip()}\n")
    AT.flush()


def RESULTlog(data):
    # pass
    # print(data)
    RESULT.write(f"[{str(datetime.datetime.now())}] {data.strip().lstrip()}\n")
    RESULT.flush()


class paserKeyClass(object):
    
    def __init__(self):
        self.cookie = http.cookiejar.CookieJar()
        self.headers = {'User-agent': 'Mozilla/5.0 '
                                      '(Windows NT 10.0; WOW64; rv:67.0) '
                                      'Gecko/20100101 Firefox/67.0'}
        self.opener = request.build_opener(
            urllib.request.HTTPCookieProcessor(self.cookie))
    
    def loginJenkins(self):
        # sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
        # #改变标准输出的默认编码
        data = {'j_username': 'st_merge1',
                'j_password': '123456',
                'from': '',
                'Submit': 'Sign+in',
                'remember_me': 'on'}
        post_data = urllib.parse.urlencode(data).encode('utf-8')
        # 设置请求头
        # 登录时表单提交到的地址（用开发者工具可以看到）
        login_url = 'http://192.168.10.11:8080/j_acegi_security_check'
        # 构造登录请求
        req = request.Request(login_url, headers=self.headers, data=post_data)
        # 构造cookie
        # 由cookie构造opener
        # 登录后才能访问的网页
        self.opener.open(req)
    
    def getPaserKey(self, queryId, qtype):
        self.loginJenkins()
        url = 'http://192.168.10.11:8080/job/query_key/'
        # 构造访问请求
        req = request.Request(url, headers=self.headers)
        resp = self.opener.open(req)
        respBuffer = resp.read().decode('utf-8')
        succerssStr = re.search(r'最近成功的构建\s\(#\d+\)', respBuffer).group()
        newIndex = int(re.search(r'\d+', succerssStr).group())
        reayKeyStr = ""
        endIndex = 10
        if newIndex > 610:
            endIndex = newIndex - 600
        try:
            for i in range(newIndex, endIndex, -1):
                ur2 = 'http://192.168.10.11:8080/job/query_key/' + str(
                    i) + '/consoleText'
                req2 = request.Request(ur2, headers=self.headers)
                resp2 = self.opener.open(req2)
                respBuffer2 = resp2.read().decode('utf-8')
                if queryId.strip() != '' and queryId in respBuffer2 and \
                        qtype.strip() != '' and qtype in respBuffer2:
                    ikeyIndex = int(respBuffer2.find('ikey='))
                    echoIndex = int(respBuffer2.find('+ echo'))
                    reayKeyStr = respBuffer2[ikeyIndex + 5:echoIndex]
                    
                    break
                self.opener.close()
        except Exception:
            reayKeyStr = ""
        return reayKeyStr
    
    def createPwd(self, queryId, qtype):
        self.loginJenkins()
        url = 'http://192.168.10.11:8080/job/query_key/build '
        data = {
            'json': '{"parameter": [{"name": "qversion", "value": "v1.0"}, '
                    '{"name": "ID", "value": "' + queryId + '"},{"name": '
                                                            '"qtype", '
                                                            '"value": "' +
                    qtype + '"}], "statusCode": "303", "redirectTo": "."}'
        }
        post_data = urllib.parse.urlencode(data).encode('utf-8')
        req = request.Request(url, headers=self.headers, data=post_data)
        self.opener.open(req)
        self.opener.close()


def getpasswd(queryId, qtype="console"):
    """
    获取debug口动态密码
    :param queryId: 密码请求ID
    :param qtype: 请求密码类型（console，adb）
    :return: 密码
    """
    key = paserKeyClass().getPaserKey(queryId, qtype)
    if key != "":
        return key
    paserKeyClass().createPwd(queryId, qtype)
    time.sleep(1)
    key = paserKeyClass().getPaserKey(queryId, qtype)
    time.sleep(1)
    return key


@dataclass
class debug(object):
    portnamme: str
    baudrate: int
    
    def __post_init__(self):
        self.__port = serial.Serial(self.portnamme, self.baudrate, timeout=0.2)
        self.__cmd = "None"
        self.__buf = {}
        self.__buf[self.__cmd] = []
        self.__working = True
        self.__idle = 0
        self.__flag = 1
        t = threading.Thread(target=self.__read, args=())
        t.setDaemon(True)
        t.start()
        self.__buff = mybuffer.Buffer(1024)
    
    def __read(self):
        t = time.time()
        i = 0
        TMP = 0
        flag = 0
        while self.__working:
            # 部分PC运行时会出现ClearCommError Failed(OSError(22,'函数不正确。', None, 1))
            try:
                data = self.__port.readline()
            except Exception as e:
                data = '[error]%s' % e
            try:
                data = data.decode()
            except:
                data = str(data)
            
            if len(data) > 2:
                self.__buf[self.__cmd].append(data)
                self.__buff.put(data)
                debuglog(data)
                self.__idle = 0
                self.__flag = 1
                if re.search('BOOTLOADER DONE JUMP TO UPDATER',str(data)):
                    t = time.time()
                    flag = 1
                    i += 1
                if re.search('Clear upgrade flag OK',str(data)):
                    flag = 0
                if time.time() - t > TIME1*i and flag == 1:
                    ATlog("uart口拉高DTR")
                    uart.setDTR(False)
                    self.__port.flush()
                    flag = 0
                    time.sleep(0.5)
                    ATlog("uart口拉低DTR")
                    uart.setDTR(True)
                    ATlog(f"第{i}次断电重启")
                    debuglog(f"第{i}次断电重启")
                    RESULTlog(f"第{i}次断电重启")
                    print(f"第{i}次断电重启")
            else:
                if self.__flag == 1:
                    self.__flag = 0
                if self.__flag == 0 and time.time() - t > 30:
                    self.__idle = 1
            
            time.sleep(0.01)
    
    def sendCMD(self, cmd):
        if cmd == "":
            self.__cmd = "None"
        else:
            self.__cmd = cmd
        
        self.__buf[self.__cmd] = []
        self.__port.write(str(cmd + "\n").encode())
        time.sleep(0.1)
    
    def getbuf(self):
        return self.__buf[self.__cmd]
    
    def open(self):
        self.__working = True
        t = threading.Thread(target=self.__read, args=())
        t.setDaemon(True)
        t.start()
    
    def close(self):
        self.__working = False
    
    def login(self, user, passwd=""):
        self.__buf[self.__cmd] = []
        self.__port.write("\n".encode())
        i = 0
        time.sleep(1)
        flag = 0
        while True:
            ltmp = self.__buf[self.__cmd]
            for log in ltmp[i:]:
                # print("----- %s ----" % log.strip())
                if "login:" in ltmp[-1]:
                    self.__port.write(str(user + "\n").encode())
                elif "quectel-ID" in log and not passwd:
                    k = log.split(":")[0].strip()
                    v = log.split(":")[1].strip()
                    passwd = getpasswd(v).strip()
                    # debuglog(passwd)
                elif "PASSWORD" in log.upper():
                    debuglog("user: %s passwd:%s" % (user, passwd))
                    self.__port.write(str(passwd + "\n").encode())
                    flag += 1
                elif "root@" in log:
                    return True
                if flag > 10:
                    return False
                i += 1
                time.sleep(0.1)
    def getendbuf(self):
        return self.__buff.get()

def checkUSB():
    try:
        port_list = list(serial.tools.list_ports.comports())
        if len(port_list) == 0:
            return []
        else:
            listt = []
            for i in range(0, len(port_list)):
                # print(port_list[i])
                matchObj = re.match(r'(.*) - (.*)', str(port_list[i]),
                                    re.M | re.I)
                try:
                    a = matchObj.group(1)
                    b = matchObj.group(2)
                  
                    # print(port_list[i])
                    listt.append(a.upper())
                except  Exception as e:
                    pass
            
            return listt
    except:
       return []

debugport = str(input("DEBUG端口例如COM3：")).strip()
UARTport = str(input("UART端口例如COM4：")).strip()
USBATport = str(input("USBAT端口例如COM8：")).strip()
TIME1 = int(input("断电间隔(s)例如1："))
C = debug(debugport, 115200)
uart = serial.Serial(UARTport, 115200, timeout=0.1)
uart.setDTR(True)
i = 0
TMP = 0
usbatflag = 0
runtimes = 0
while True:
    pass
            






