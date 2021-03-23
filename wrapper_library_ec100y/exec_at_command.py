#!/usr/bin/env python 
# -*- coding: utf-8 -*-
'''
-------------------------------------------------------------------------------
脚本名称:  exec_at_command
需求来源:
    发送AT与读取串口操作
测试目的：
    主要实现AT命令串口通信以及检测串口输出数据
修改记录:
    初始版本V1.0 2019/8/23 loren.jia
脚本逻辑:
    无
脚本统计:
    无
测试前准备:
    无
-------------------------------------------------------------------------------
'''

import datetime
import re
import time
import wrapper_library_ec100y.common_function as common_function
import wrapper_library_ec100y.common_log as common_log
import wrapper_library_ec100y.common_log_queue_dict as common_log_queue_dict
import wrapper_library_ec100y.exception_handling as exception_handling
import wrapper_library_ec100y.off_the_card_processing as processing
import wrapper_library_ec100y.port_work as p_w

print = common_function.my_print
info = common_log_queue_dict.DictObject().info()

class ExecAtCommand(object):
    """
    该类主要用来实现串口的AT通信，以及检测串口输出的数据。
    
    Attributes:
    _runtimes: int类型，表示第几次执行AT命令，用于区分模块异常重启的问题
    command: str类型，写入的AT命令。
    timeout: int类型，设置超时时间，超时退出。
    at_port_open: object类型，是一个已经打开的串口对象，对该串口进行读写
    at_result: str类型，期望AT命令的结果，匹配退出。
    
    """
    
    def __init__(self, _runtimes): #实例化该类需要的参数
        """
        实例化该类需要的参数_runtimes，用于区分模块异常重启的问题
        :param _runtimes:  int类型，用于区分模块异常重启的问题
        """
        self._runtimes = _runtimes
        self.result_dict = common_log_queue_dict.DictObject().parameter()
        # 初始化一个数据字典，用于记录串口读取的数据内容一些必要参数
        
        self.LOG = common_log.LogTools()

    @exception_handling.my_error()
    def send_at(self, command, timeout, at_port_opened, at_result,RDY=0,CPIN=0):
        """
        串口的写与读
        :param command: str类型，写入的AT命令。
        :param timeout: int类型，设置超时时间，超时退出。
        :param at_port_open: object类型，是一个已经打开的串口对象，对该串口进行读写
        :param at_result: str类型，期望AT命令的结果，匹配退出。
        :return: dict类型，re_data_dict，记录串口读取的数据内容一些必要参数
        """
        self.portname = at_port_opened.name
        self.baudrate = at_port_opened.baudrate
        self.porttimeout = at_port_opened.timeout

        self.re_data_dict = {'Creg': (False, 0),
                             'Cereg': (False, 0),
                             'Cgreg': (False, 0),
                             }
        self.LOG.at_log_put('[send]%s'%command)
        at_command = (command + "\r\n").encode("utf-8")
        p_w.at_write(at_port_opened,at_command) #
        at_start_time = datetime.datetime.now()
        _data_buffer = ''
        _log = ''
        i = 0
        time_flag = 0
        CWRITESIM = 0
        while 1:
            at_port_data = p_w.at_read(at_port_opened)
            at_end_time = datetime.datetime.now()
            at_time = common_function.duration(at_start_time, at_end_time)

            if at_time > int(timeout):
                if len(_log) == 0 and self._runtimes >0:
                    i += 1
                    p_w.at_write(at_port_opened, b'+++')
                    time.sleep(1)
                    #at_port_opened.write(at_command)
                    p_w.at_write(at_port_opened, at_command)
                    self.LOG.at_log_put('[send]%s' % command)
                    if i > 5:
                        while True:
                            i += 1
                            #at_port_opened.write()
                            p_w.at_write(at_port_opened, b"AT\r\n")
                            self.LOG.at_log_put('[send]AT')
                            at_port_data = p_w.at_read(at_port_opened)
                            if len(at_port_data) == 0:
                                time.sleep(2)
                                if i > 20 :
                                    data = str('Runtimes：%s 模块异常，'
                                               'AT不通，保留现场'
                                               %str(self._runtimes))
                                    self.LOG.abnormal_log_put(data)
                                    self.re_data_dict['result'] = False
                                    self.re_data_dict['re_data'] = _log
                                    time.sleep(10)
                                    while True:
                                        time.sleep(2)
                                        DICT = common_log_queue_dict.DictObject()
                                        if DICT.setting()['module']['STOP'] == 0:
                                            return self.re_data_dict
                                
                            else:
                                break
                elif self._runtimes == 0 and len(_log) == 0:
                    info['modem_fail'] = 1
                    self.LOG.abnormal_log_put('modem 启动失败 AT 不通')
                    self.LOG.at_log_put('modem 启动失败 AT 不通')
                    self.re_data_dict['result'] = False
                    self.re_data_dict['re_data'] = _log
                    return self.re_data_dict
                else:
                    # self.log.write_at_log(at_log1)
                    self.re_data_dict['result'] = False
                    self.re_data_dict['re_data'] = _log
                    return self.re_data_dict
            
            at_data_replace = _data_buffer + \
                              str(at_port_data).replace('b\'', '')\
                                  .replace('\'', '')

            _log += at_data_replace
            at_result_temp = at_data_replace.split(r'\r\n')
            _data = at_result_temp[:-1]
            _data_buffer = at_result_temp[-1]

            if _data:
                result = 0
                for a in _data:
                    a = a.replace('\\r', '')
                    self.LOG.at_log_put('[recv]%s'%a)
                    c_list = a
                    if re.search('RDY', c_list):
                        if self._runtimes > 0 and RDY==0:
                            notes = str('模块异常重启一次')
                            self.LOG.abnormal_log_put(notes)
                            self.LOG.at_log_put(notes)
                        else:
                            pass
                    if re.search('\+EGMR: "(\d+)"', c_list):
                        if command == "AT+EGMR=0,7":
                            UE_IMEI = ','.join(re.compile('\+EGMR: "(\d+)"')
                                               .findall(c_list))
                            # 获取模块的IMEI
                            try:
                                if info['IMEI'] != UE_IMEI and info['IMEI'] != '':
                                    self.LOG.abnormal_log_put('模块IMEI号发生改变')
                                    self.LOG.at_log_put('模块IMEI号发生改变')
                                else:
                                    info['IMEI'] = UE_IMEI
                            except Exception as e:
                                info['IMEI'] = UE_IMEI
                        else:
                            UE_SN = ','.join(re.compile('\+EGMR: "(\d+)"')
                                               .findall(c_list))
                            # 获取模块的IMEI
                            try:
                                if info['SN'] != UE_SN and info[
                                    'SN'] != '':
                                    self.LOG.abnormal_log_put('模块SN号发生改变')
                                    self.LOG.at_log_put('模块SN号发生改变')
                                else:
                                    info['SN'] = UE_SN
                            except Exception as e:
                                info['SN'] = UE_SN
                    elif re.search("(\d+)", c_list) and command == "AT+CIMI":
                        SIM_IMSI = ','.join(re.compile('(\d+)')
                                            .findall(c_list))
                        # 获取当前卡槽中SIM卡的IMSI号
                        info['IMSI'] = SIM_IMSI
                    elif re.search('QNWINFO: "(.*)","(.*)","(.*)",(.*)', c_list) :
                        band =re.search('QNWINFO: "(.*)","(.*)","(.*)",(.*)', c_list).group(3)
                        BCCH =re.search('QNWINFO: "(.*)","(.*)","(.*)",(.*)', c_list).group(4)
                        # 获取当前卡槽中SIM卡的IMSI号
                        info['band'] = band
                        info['BCCH'] = BCCH
                    elif re.search("Revision: (.*)", c_list):
                        Revision = ','.join(re.compile("Revision: (.*)")
                                            .findall(c_list))
                        # 获取当前卡槽中SIM卡的IMSI号
                        info['Revision'] = Revision
                    elif re.search('QWSETMAC: "(.*)"', c_list):
                        QWSETMAC = ','.join(re.compile('QWSETMAC: "(.*)"')
                                            .findall(c_list))
                        try:
                            if info['QWSETMAC'] != QWSETMAC and info['QWSETMAC'] != '':
                                self.LOG.abnormal_log_put('模块MAC地址发生改变')
                                self.LOG.at_log_put('模块MAC地址发生改变')
                            else:
                                info['QWSETMAC'] = QWSETMAC
                        except Exception as e:
                            info['QWSETMAC'] = QWSETMAC
                    elif re.search("SubEdition: (\w+)", c_list):
                        SubEdition = ','.join(re.compile("SubEdition: (\w+)")
                                              .findall(c_list))
                        # 获取当前卡槽中SIM卡的IMSI号
                        info['SubEdition'] = SubEdition
                    elif re.search("QCCID: (\d+)", c_list):
                        QCCID = ','.join(re.compile("QCCID: (.*)")
                                         .findall(c_list))
                        # 获取当前卡槽中SIM卡的IMSI号
                        info['QCCID'] = QCCID
                    elif re.search("\+QPRTPARA: (\d+),(\d+),(\d+),"
                                   "(\d+),(\d+),(\d+),(\d+),(\d+),(\d+),(\d+)",
                                   c_list):  #获取cefs还原信息
                        cefs_restore = re.search("\+QPRTPARA: (\d+),(\d+),(\d+),"
                                                 "(\d+),(\d+),(\d+),(\d+),"
                                                 "(\d+),(\d+),(\d+)",
                                                 c_list)
                        self.re_data_dict["cefs_restore"] = cefs_restore.group(2)
                        info['cefs_restore'] = int(self.re_data_dict["cefs_restore"])
                    elif re.search('\+QNAND: "RecoveryCnt",(\d+),(\d+),(\d+),'
                                   '(\d+),(\d+),(\d+),(\d+),(\d+),'
                                   '(\d+),(\d+),(\d+),(.*)',
                                   #获取modem/linux还原信息
                                    c_list):
                        restore = re.search(
                            '\+QNAND: "RecoveryCnt",(\d+),(\d+),(\d+),'
                            '(\d+),(\d+),(\d+),(\d+),'
                            '(\d+),(\d+),(\d+),(\d+),(.*)',
                            c_list)
                        self.re_data_dict["linux_restore"] = restore.group(1)
                        info['linux_restore'] = int(restore.group(1))
                        self.re_data_dict["modem_restore"] = restore.group(12)
                        info['modem_restore'] = int(restore.group(12))
                    elif re.search('\+CREG: 2,1', c_list):
                        #获取creg注网信息
                        Creg = True
                        Creg_endtime = datetime.datetime.now()
                        self.re_data_dict['Creg'] = (Creg, Creg_endtime)

                    elif re.search(
                        '\+QENG: "servingcell","\S+","\S+","\S+",\d+,\d+,\S+,\d+,\d+,\d+,\d+,\d+,\S+,\S+,\S+,\S+,\S+,\S+',
                        c_list):
                        earfcn = ''.join(
                            re.compile(
                                '\+QENG: "servingcell","\S+","\S+","\S+",\d+,\d+,\S+,\d+,(\d+),\d+,\d+,\d+,\S+,\S+,\S+,\S+,\S+,\S+').findall(
                                str(c_list)))
                        pci = ''.join(
                            re.compile(
                                '\+QENG: "servingcell","\S+","\S+","\S+",\d+,\d+,\S+,(\d+),\d+,\d+,\d+,\d+,\S+,\S+,\S+,\S+,\S+,\S+').findall(
                                str(c_list)))
                        snr = ''.join(
                            re.compile(
                                '\+QENG: "servingcell","\S+","\S+","\S+",\d+,\d+,\S+,\d+,\d+,\d+,\d+,\d+,\S+,\S+,\S+,\S+,(\S+),\S+').findall(
                                str(c_list)))
                        rsrp = ''.join(
                            re.compile(
                                '\+QENG: "servingcell","\S+","\S+","\S+",\d+,\d+,\S+,\d+,\d+,\d+,\d+,\d+,\S+,(\S+),\S+,\S+,\S+,\S+').findall(
                                str(c_list)))
                        info['rsrp'] = rsrp
                    elif re.search('\+QENG:"servingcell", "NOCONN"',c_list):
                        info['rsrp'] = "null"
                    elif re.search('closed', c_list):

                        try:
                            info['closed'] += 1
                        except:
                            info['closed'] = 1
                        self.LOG.at_log_put('连接异常断开')
                        self.LOG.abnormal_log_put('连接异常断开')
                    elif re.search('\+CGREG: 2,1', c_list):
                        #获取cgreg注网信息
                        Cgreg = True
                        Cgreg_endtime = datetime.datetime.now()
                        self.re_data_dict['Cgreg'] = (Cgreg, Cgreg_endtime)
                    elif re.search('\+CEREG: 2,1', c_list):
                        #获取cereg注网信息
                        Cereg = True
                        Cereg_endtime = datetime.datetime.now()
                        self.re_data_dict['Cereg'] = (Cereg, Cereg_endtime)
                    elif re.search('\+COPS: (\d+),(\d+),"(.*)",(\d+)', c_list):
                        COPS = ','.join(re.compile('\+COPS: \d+,\d+,"(.*)",\d+')
                                        .findall(c_list))
                        info['COPS'] = COPS
                    elif re.search('\+CPIN: NOT READY', c_list):
                        if CPIN == 0:
                            self.LOG.abnormal_log_put('模块检测到掉卡')
                            self.LOG.at_log_put('模块检测到掉卡')
                            processing.cfun(at_port_opened)
                    elif re.search('\+QTEMP: (.*),(.*),(.*),(.*)', c_list):
                        #temp = re.search('\+QTEMP: (\d+),(\d+),(\d+),(\d+),', c_list)
                        temp = re.search('\+QTEMP: (\S+),(\S+),(\S+),(\S+),', c_list)
                        QTEMP = temp.group(3)
                        info['QTEMP'] = int(QTEMP)
                    elif re.search('\+qdmem: "modem_heap",(\d+),(\d+),(\d+)', c_list):
                        dmem = re.search('\+qdmem: "modem_heap",(\d+),(\d+),(\d+)', c_list)
                        QDMEM = dmem.group(2)
                        info['QDMEM_Use'] = int(QDMEM)
                    elif re.search('\+QCFG: (\d+)', c_list) and command.upper() == 'AT+QCFG="USAGE/APFS"':
                        dmem = re.search('\+QCFG: (\d+)', c_list)
                        APFS = dmem.group(1)
                        self.LOG.at_log_put(f'linux文件系统的大小:{APFS}')
                        info['APFS'] = int(APFS)
                    elif re.search('MemTotal: (\d+)',c_list) :
                        Mem = re.search('MemTotal: (\d+)', c_list)
                        MemTotal = Mem.group(1)
                        info['MemTotal'] = int(MemTotal)
                    elif re.search('MemFree: (\d+)',c_list) :
                        Mem = re.search('MemFree: (\d+)', c_list)
                        MemFree = Mem.group(1)
                        info['MemFree'] = int(MemFree)
                    elif re.search('\+QDBGCFG: "memory",(\d+),(\d+),(\d+)',c_list) :
                        Mem = re.search('\+QDBGCFG: "memory",(\d+),(\d+),(\d+)', c_list)
                        Total = Mem.group(1)
                        info['MemTotal'] = int(Total)
                        Free = Mem.group(2)
                        info['MemFree'] = int(Free)
                    elif re.search('BlkEraseTotalCnt: (\d+)',c_list) :
                        Mem = re.search('BlkEraseTotalCnt: (\d+)', c_list)
                        BlkEraseTotalCnt = Mem.group(1)
                        info['BlkEraseTotalCnt'] = int(BlkEraseTotalCnt)
                    elif re.search('(\d+),Quectel,EC200T,(.*),', c_list):
                        Revision = re.search('(\d+),Quectel,EC200T,(.*),(.*),(.*),(.*)', c_list).group(4)
                        info['Revision'] = Revision
                    elif re.search('\+IMEI: 1100,(.*)', c_list):
                        UE_IMEI = re.search('\+IMEI: 1100,(.*)', c_list).group(1)
                        # 获取模块的IMEI
                        try:
                            if info['IMEI'] != UE_IMEI and info['IMEI'] != '':
                                self.LOG.abnormal_log_put('模块IMEI号发生改变')
                                self.LOG.at_log_put('模块IMEI号发生改变')
                            else:
                                info['IMEI'] = UE_IMEI
                        except Exception as e:
                            info['IMEI'] = UE_IMEI
                    elif re.search('(\d+),Quectel,EC200T,(.*),', c_list):
                        Revision = re.search('(\d+),Quectel,EC200T,(.*),(.*),(.*),(.*)', c_list).group(4)
                        info['Revision'] = Revision
                    elif re.search('CWRITESIM:0xFFFF,(\d+)', c_list):
                        CWRITESIM = re.search('CWRITESIM:0xFFFF,(\d+)', c_list).group(1)
                        info['CWRITESIM'] = int(CWRITESIM)
                    elif re.search('\+QSIMWRFREQ: (.*),(.*),(.*),(\d+)', c_list):
                        CWRITESIM += int(re.search('\+QSIMWRFREQ: (.*),(.*),(.*),(\d+)', c_list).group(4))
                        info['CWRITESIM'] = CWRITESIM
                    elif re.search('\+QIURC: "pdpdeact",', c_list)and \
                        command.upper() !='AT+CFUN=0':
                        try:
                            info['pdpdeact'] += 1
                        except:
                            info['pdpdeact'] = 1

                        # self.LOG.at_log_put('AT命令报错返回PDPDEACT')
                        # self.LOG.abnormal_log_put('AT命令报错返回PDPDEACT:')
                    if re.search(at_result, c_list):
                        # 匹配到指定的response后结束循环
                        result = 1
                        self.re_data_dict['result'] = True
                    elif re.search('ERROR', c_list):
                        result = 2
                        self.re_data_dict['result'] = False
                        self.LOG.abnormal_log_put("%s 执行返回 %s" % (command, c_list))
                if result != 0:
                    self.re_data_dict['re_data'] = _log
                    return self.re_data_dict
            else:
                if at_time - time_flag > 1:
                    common_log.LogTools().log().error(f'等待{at_time}秒，无回应')
                    time_flag = at_time



