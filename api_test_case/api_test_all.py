# -*- coding: utf-8 -*-
"""
@Author: Trent
@Date: 2020-11_30
@LastEditTime: 2020-11_30
@Description: API test for all
@FilePath: api_test_all.py
"""
import signal
import serial
import configparser
import sys
import os
import time
import re
import threading
import wrapper_library_ec100y.common_log as common_log
import wrapper_library_ec100y.exec_dos_command as exec_dos_command
import wrapper_library_ec100y.exec_at_command as exec_at_command
import wrapper_library_ec100y.check_usb as check_usb
import wrapper_library_ec100y.common_log_queue_dict as common_log_queue_dict
import subprocess
import serialport_checkusb
uart_port = 'COM3'
debug_port = "COM37"
cdc_port = 'COM27'
at_port = 'COM29'
baudrate = 115200
test_list = r'E:\04_python\python项目脚本\lte_open_py\api_test_case'


class ApiTest(object):
    def __init__(self,uart_port='', debug_port='',cdc_port='', at_port='', baudrate=115200, test_list=''):
            self.uart_port = uart_port
            self.debug_port = debug_port
            self.cdc_port = cdc_port
            self.at_port = at_port
            self.baudrate = baudrate
            self.test_list = test_list

    def special_file_path(self, path):
        """
        单独跑的API路径
        :param path:
        :return:
        """
        with open('special_file_path.txt', "a+", encoding='utf8') as f:
            f.write(str(path + '\n'))
        f.close()

    def file_path(self):
        """
        读取API文件
        :return:
        """
        list1 = []
        list2 = []
        with open('api_test_path.txt', "w+", encoding='utf8') as f:
            path_list = os.listdir(self.test_list)
            path_list.sort()  # 对读取的路径进行排序
            for dirName, subdirList, fileList in os.walk(self.test_list):
                if fileList:
                    list1.append(fileList)
                if subdirList:
                    list2.append(subdirList)
            list1.pop(11)
            list1.pop(15)
            print(list2[0])
            print(list1)
            for idx in range(len(list1)):
                for i in list1[idx]:
                    if i[-11:] == 'api_test.py':
                        if i == "thread_bulid_lock__api_test.py" or i == 'fota_download_update_verify_api_test.py' or \
                           i == 'uart_api_test.py' or i == 'mqtt_uart_api_test.py' or i == 'power_getvbatt_api_test.py'\
                           or i == 'power_onoff_api_test.py' or i == 'power_restart_api_test.py' or i == 'socket_write_read_recv_api_test.py':
                            self.special_file_path(str(self.test_list+"\\"+list2[0][idx]+"\\"+i))
                        else:
                            f.write(str(self.test_list+"\\"+list2[0][idx]+"\\"+i+'\n'))
                    else:
                        pass
        f.close()

    def cmd_dos(self):
        """
        CMD 命令交互,监听dos环境数据
        :param cmd: str类型，dos 命令
        :param result:  str类型，期望的结果
        :return: Result,re_info #Result :0/1 ，存在result返回1 否则0   re_info
        :dos执行log
        """
        self.file_path()
        with open('api_test_path.txt', "r", encoding='utf8') as f:
            a = f.readlines()
            print(len(a))
            for i in a:
                print(str(i)[:-1])
                cmd = f'QuecPyComTools.exe -d {self.cdc_port} -b {self.baudrate} {str(i)[:-1]}'
                # cmd = 'ping baidu.com'
                a = exec_dos_command.DosCmd()
                a.commands(cmd=cmd, result='0')
                time.sleep(5)
            f.close()


if __name__ == '__main__':
    common_log.LogTools.set_project('EC100Y_OPEN_PY')
    s = ApiTest(uart_port, debug_port, cdc_port, at_port, baudrate, test_list)
    s.cmd_dos()
    # s.file_path()
