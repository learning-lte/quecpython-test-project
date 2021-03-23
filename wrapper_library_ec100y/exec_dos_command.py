#!/usr/bin/env python 
# -*- coding: utf-8 -*-
'''
-------------------------------------------------------------------------------
脚本名称:  exec_dos_command
需求来源:
    dos命令交互
测试目的：
    主要实现dos命令交互
修改记录:
    初始版本V1.0 2019/8/23 loren.jia
脚本逻辑:
    通过subprocess.Popen方法实现cmd 命令交互
脚本统计:
    无
测试前准备:
    无
-------------------------------------------------------------------------------
'''

import re
import subprocess
import time
import os
import signal
import wrapper_library_ec100y.common_function as common_function
import wrapper_library_ec100y.common_log as common_log
import wrapper_library_ec100y.exec_at_command as exec_at_command

print = common_function.my_print

class DosCmd(object):
    """
    DOS 命令交互
    
    Attributes:
        cmd：dos命令
        result：期望结果
    """
    __isinstance = None
    
    def __new__(cls, *args, **kwargs):
        if cls.__isinstance is None:
            cls.__isinstance = object.__new__(cls)
            return cls.__isinstance
        else:
            return cls.__isinstance
    
    def __init__(self):
        """ None """
        self.at_log = common_log.LogTools.at_log_put

    def commands(self, cmd, result, timeout=360):
        '''
        CMD 命令交互
        :param cmd: str类型，dos 命令
        :param result:  str类型，期望的结果
        :return: Result,re_info #Result :0/1 ，存在result返回1 否则0   re_info
        :dos执行log
        '''
        
        Result = 0
        re_info = ''  # 增加dos命令返回结果
        self.at_log('[DOS_Cmd]%s' % (str(cmd)))
        time1 = time.time()
        s = subprocess.Popen(cmd, shell=True,
                             stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        
        nextline = ""
        while True:
            if nextline == "" and s.poll() != None:
                try:
                    nextline = str(s.stdout.readline().strip(), encoding='utf-8')
                except Exception as e:
                    print(e)
                    print(str(s.stdout.readline()))
                if nextline == "":
                    break
            else:
                try:
                    nextline = str(s.stdout.readline().strip(), encoding='utf-8')
                except Exception as e:
                    print(e)
                    print(str(s.stdout.readline()))
            re_info += nextline
            if nextline != "":
                # print("<<<<<<",nextline)
                self.at_log('[DOS_Recv]%s' % str(nextline))
            
            if re.search(result, nextline):
                Result = 1
            if time.time() - time1 > timeout:
                os.kill(s.pid,signal.CTRL_C_EVENT)
                return Result, re_info
        return Result, re_info  # 添加dos命令返回结果
