#!/usr/bin/env python 
# -*- coding: utf-8 -*-
'''
-------------------------------------------------------------------------------
脚本名称:  check_usb
需求来源:
    检查USB驱动的封装类
测试目的：
    检查USB驱动加载与通信
修改记录:
    初始版本V1.0 2019/8/23 loren.jia
脚本逻辑:
    传入一个usb驱动名称，通过循环读取USB驱动列表来匹配传入的USB驱动是否加载，
    USB加载后打开USBport发送AT测试是否通信正常，通信正常或者超时返回结果
脚本统计:
    无
测试前准备:
    无
-------------------------------------------------------------------------------
'''

import datetime
import re
import time
import serial.tools.list_ports
import wrapper_library_ec100y.common_log as common_log
import wrapper_library_ec100y.common_function as common_function
import wrapper_library_ec100y.exception_handling as exception_handling
import winreg
import itertools
log = common_log.LogTools()
print = common_function.my_print

class CheckUsbDriver(object):
    '''
    该类主要用来检查规定时间内USB驱动是否加载得分，是否通信正常。
    
    Attributes:
    usb_driver_name: 字符串类型，表示需要检测的usb驱动名称。
    check_load: 布尔类型，是否需要检测USB是否加载，默认检测。
    check_communication:布尔类型，是否需要检测USB是否通信正常，默认检测。
    '''
    
    def __init__(self,
                 sub_driver_name,
                 check_load=True,
                 check_communication=True):  #实例化该类需要的参数
        """
        实例化需要传入必选参数usb驱动名称，例如："COM8",可选参数check_load,check_communication
        :param sub_driver_name: str
        :param check_load: bool
        :param check_communication: bool
        """
        self.log = common_log.LogTools()
        self.usb_driver_name = str(sub_driver_name).upper()
        self.check_load = check_load
        self.check_communication = check_communication
        self._usbload = None  #初始USB驱动的加载情况为空
    
    @exception_handling.my_error()
    def check_usb(self, timeout=30):   #检测USB加载与通信
        '''
        在规定时间内检测usb驱动，超时则失败
        :param timeout: int类型，定义超时时间.默认30s
        :return: bool类型,int类型,str类型  -->usb是否正常，usb加载时间戳，usb加载通信情况
        '''
        start_check_usb_time = time.time()
        USB_load_time= datetime.datetime.now()
        self._usbload = False
        self._usb_error = None
        flag = 0
        while True:
            self.log.at_log_put('usb  检测')
            if self.check_load:  #判断是否检测USB加载
                port_list = list(usb_dict().keys())
                port_list2 = list(usb_dict().values())
                if len(port_list) == 0:
                    self.log.at_log_put('usb  加载为空')
                    self._usbload = False
                else:
                    port = []
                    for i in range(0, len(port_list)):
                        try:
                            self.log.at_log_put('port: %s %s' % (port_list[i],port_list2[i]))
                        except Exception as e:
                            print(e)
                            continue
                        matchObj = re.match(r'(.*)',
                                            str(port_list[i]), re.M | re.I)
                        port.append(matchObj.group(1))
                    # self.log.at_log_put('%s' % str(port))
                    if self.usb_driver_name in port:
                        if flag == 1 or time.time()-start_check_usb_time >timeout/3:
                            
                            usb_stat = str("%s口正常加载"
                                           % self.usb_driver_name)
                            self.log.at_log_put(usb_stat)
                            USB_load_time = datetime.datetime.now()
                            self._usbload = True
                            if not self.check_communication:
                                self.log.at_log_put('usb加载正常，不check 通信')
                                return True, USB_load_time, usb_stat
                            else:
                                time1 = time.time()
                                while True:
                                    check_usb_times = (time.time() - start_check_usb_time)
                                    try:
                                        usb_port = serial.Serial(self.usb_driver_name,
                                                                 115200,
                                                                 timeout=0.5)
                                        self._usb_error = None
                                    except Exception as e:
                                        print(e)
                                        try:
                                            usb_port.close()
                                        except:
                                            pass
                                        self._usb_error = e
                                        if (time.time() - time1) % 1 == 0:
                                            usb_stat = str("%s口加载正常，"
                                                           "但是打开失败：%s"
                                                           % (self.usb_driver_name,
                                                              self._usb_error))
                                            self.log.at_log_put(usb_stat)
                                            self.log.abnormal_log_put(usb_stat)
                                    if self._usb_error == None:
                                        try:
                                            self.log.at_log_put('[send] AT')
                                            usb_port.write(b'AT\r\n')
                                            data = usb_port.read(size=1024)
                                            if "OK" in str(data):
                                                self.log.at_log_put(str(data))
                                                usb_port.close()
                                                usb_stat = str("%s口正常加载通信"
                                                               % self.usb_driver_name)
                                                self.log.at_log_put(usb_stat)
                                                return True, USB_load_time, usb_stat
                                            usb_port.close()
                                        except Exception as e:
                                            self._usb_error = e
                                            if (time.time() - time1) % 1 == 0:
                                                usb_stat = str("%s口打开正常，"
                                                               "但是通信失败：%s"
                                                               % (self.usb_driver_name,
                                                                  self._usb_error))
                                                self.log.at_log_put(usb_stat)
                                                self.log.abnormal_log_put(usb_stat)
                                            try:
                                                usb_port.close()
                                            except Exception as e2:
                                                pass
                                    if check_usb_times > timeout:
                                        self.log.at_log_put('usb加载正常，检测超时')
                                        return False, USB_load_time, usb_stat
                    else:
                        flag = 1
                        
            else:
                self._usbload = True
            if self._usbload and self.check_communication: #判断usb是否加载，是否进行AT通信
                time1 =time.time()
                while True:
                    check_usb_times = (time.time() - start_check_usb_time)
                    
                    if check_usb_times > timeout:
                        break
                    try:
                        usb_port = serial.Serial(self.usb_driver_name,
                                                 115200,
                                                 timeout=0.5)
                        usb_port.write(b'AT\r\n')
                        data = usb_port.read(size=1024)
                        if "OK" in str(data):
                            self.log.at_log_put(str(data))
                            usb_port.close()
                            usb_stat = str("%s口正常加载通信"
                                           %self.usb_driver_name)
                            self.log.at_log_put(usb_stat)
                            return True,USB_load_time,usb_stat
                    except Exception as e:
                        self._usb_error = e
                        time.sleep(1)
                        usb_stat = str("%s口加载正常，但是通信失败：%s"
                                       % (self.usb_driver_name,
                                          self._usb_error))
                        self.log.at_log_put(usb_stat)
                        self.log.abnormal_log_put(usb_stat)
                        try:
                            usb_port.close()
                        except Exception as e2:
                            pass
                else:
                    usb_stat = str("%s口加载正常，但是通信失败：%s"
                                   %(self.usb_driver_name,
                                     self._usb_error))
                    return False, USB_load_time,usb_stat
            
            check_usb_times = (time.time() - start_check_usb_time)
            if check_usb_times > timeout:
                usb_stat = str("%s口检测超时 %s" % (self.usb_driver_name,
                                               str(port)))
                self.log.abnormal_log_put(usb_stat)
                return False, USB_load_time, usb_stat
            time.sleep(1)


def usb_dict():
    log = common_log.LogTools()
    port_dict = {}
    def list_ports_with_registry():
        """ Uses the Win32 registry to return a iterator of serial
            (COM) ports existing on this computer.
        """
        path = 'HARDWARE\\DEVICEMAP\\SERIALCOMM'
        try:
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path)
        except WindowsError:
            # raise IterationError
            pass

        for i in itertools.count():
            try:
                val = winreg.EnumValue(key, i)
                yield (str(val[1]), str(val[0]))
            except EnvironmentError:
                break
    def port_list():
        try:
            port_list = list(serial.tools.list_ports.comports())
            if len(port_list) == 0:
                return {'暂无设备': 'None'}
            else:
                listt = []
                for i in range(0, len(port_list)):
                    # print(port_list[i])
                    matchObj = re.match(r'(.*) - (.*)', str(port_list[i]),
                                        re.M | re.I)
                    try:
                        a = matchObj.group(1)
                        b = matchObj.group(2)
                        port_dict[a] = b
                        # print(port_list[i])
                        listt.append(a)
                    except  Exception as e:
                        pass
                p_list = list_ports_with_registry()
                for port in p_list:
                    # log(port[0],port[1])
                    pass
                #去除modem口的检测
                    # if port[0] not in port_dict.keys():
                    #     port_dict[port[0]] = f'Quectel USB Modem Port ({port[0]})'
                    #     listt.append(port[0])
                return listt
        except:
            return {'暂无设备': 'None'}
    port_list()
    return port_dict

def usbat(usb):
    """
    check usb 的通信
    :param usb: usbname
    :return: True/False
    """
    try:
        usb_port = serial.Serial(usb, 115200, timeout=0.5)
        usb_port.write(b'AT\r\n')
        time.sleep(0.1)
        data = usb_port.read(size=1024)
        if "OK" in str(data):
            log.at_log_put("-- %s -- %s " % (usb, str(data)))
            usb_port.close()
            return True
        else:
            usb_port.close()
    except Exception as e:
        log.at_log_put(str(e))
        
        return False
    return False
    
def checkusb(usb, timeout=20, at=True):
    """
    check usb 驱动的加载或消失
    :param usb: usb name
    :param timeout: 检测时长
    :param at: check at通信
    :param flag: 0表示检测由消失到出现,1检测由存在到消失在到出现
    :return: True/False
    """
    status = 9
    __tmptime = time.time()
    while time.time() - __tmptime < timeout:
        
        tmpdict = usb_dict()
        for k,v in tmpdict.items():
            log.at_log_put("-- %s --- %s" % (k, v))
        if usb.upper() in tmpdict.keys():
            if status == 0:
                if at and usbat(usb):
                    return True
                elif not at:
                    return True
                else:
                    continue
           
        else:
            status = 0
        time.sleep(1)
    return False
                
            
if __name__ == "__main__":
    log.set_project("TEST")
    checkusb("COM34", 20)
    