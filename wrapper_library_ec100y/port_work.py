#!/usr/bin/env python 
# -*- coding: utf-8 -*-
'''
#-------------------------------------------------------------------------------
脚本名称: port_work.py
需求来源: 常规版本压力测试
测试目的：
修改记录: 初始版本V1.0 2020/3/9 16:33 loren.jia
脚本逻辑:
脚本统计:
测试前准备:
#-------------------------------------------------------------------------------
'''
import time
import wrapper_library_ec100y.common_log as common_log
import wrapper_library_ec100y.common_log_queue_dict as common_log_queue_dict
import wrapper_library_ec100y.exception_handling as exception_handling
import wrapper_library_ec100y.check_usb as usb

@exception_handling.my_error()
def at_write( port, at):  # 处理使用usb驱动 模块异常重启的脚本异常问题
    LOG = common_log.LogTools()
    start_time = time.time()
    portname = port.name
    baudrate = port.baudrate
    porttimeout = port.timeout
    close_flag = 0
    while True:
        try:
            port.write(at)
            return
        except Exception as e:
            LOG.abnormal_log_put('[port ERROR ]%s' % str(e))
            port.close()
            close_flag = 1
            time.sleep(5)
            usb_dict = usb.usb_dict()
            if portname not in usb_dict.keys():
                LOG.abnormal_log_put(f'[port ERROR ] {portname} 异常消失')
            else:
                LOG.abnormal_log_put(
                    f'[port ERROR ] {portname} 仍存在，但是端口写入报错')

        while close_flag:
            time.sleep(2)
            usb_dict = usb.usb_dict()
            if portname in usb_dict.keys():
                data = str(f'[port ERROR ] {portname} 异常消失'
                           f'{str(time.time() - start_time)}秒后再次出现,'
                           f'暂判断为模块异常重启一次')
                LOG.abnormal_log_put(data)

                LOG.at_log_put(data)
                port.open()
                close_flag = 0
            if time.time() - start_time > 60:
                data = str(f'[port ERROR ] {portname} 异常消失60秒后'
                           f'未再次出现，AT不通，保留现场')
                LOG.abnormal_log_put(data)
                time.sleep(3)
                while True:
                    time.sleep(2)
                    DICT = common_log_queue_dict.DictObject()
                    if DICT.setting()['module']['STOP'] == 0:
                        return re_data_dict
                start_time = time.time()


@exception_handling.my_error()
def at_read(port,size=1024):  # 处理使用usb驱动 模块异常重启的脚本异常问题
    LOG = common_log.LogTools()
    start_time = time.time()
    close_flag = 0
    portname = port.name
    while True:
        try:
            data = port.read(size=size)
            return data
        except Exception as e:
            LOG.abnormal_log_put('[port ERROR ]%s' % str(e))
            usb_dict = usb.usb_dict()
            port.close()
            close_flag = 1
            time.sleep(3)
            if portname not in usb_dict.keys():
                LOG.abnormal_log_put(f'[port ERROR ] {portname} 异常消失')
            else:
                LOG.abnormal_log_put(
                    f'[port ERROR ] {portname} 仍存在，但是端口读取报错')

        while close_flag:
            time.sleep(2)
            usb_dict = usb.usb_dict()
            if portname in usb_dict.keys():
                data = str(f'[port ERROR ] {portname} 异常消失'
                           f'{str(time.time() - start_time)}秒后再次出现,'
                           f'暂判断为模块异常重启一次')
                LOG.abnormal_log_put(data)

                LOG.at_log_put(data)
                port.open()
                close_flag = 0
            if time.time() - start_time > 60:
                data = str(f'[port ERROR ] {portname} 异常消失60秒后'
                           f'未再次出现，AT不通，保留现场')
                LOG.abnormal_log_put(data)
                time.sleep(10)
                while True:
                    time.sleep(2)
                    DICT = common_log_queue_dict.DictObject()
                    if DICT.setting()['module']['STOP'] == 0:
                        return re_data_dict
                start_time = time.time()