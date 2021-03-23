#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
-------------------------------------------------------------------------------
脚本名称:  main_startup
需求来源:
    LTE_OPEN_PY项目测试主启动文件
测试目的：
    主启动文件
修改记录:
    初始版本V1.0 2020/9/11 Randy.zhu
脚本逻辑:
    通过此文件运行dos窗口执行API测试脚本
    1.初始化，通过at口配置进度dump的指令(at+qdumpcfg,at+log)
    2.按照配置文件依次执行API测试脚本（同时读取cdc口数据并保存至atlog）
    3.子线程同时读取debug数据并保存至debuglog，检测到输出内容有flash时，将flash信息保存至abnormallog
脚本统计:
    无
测试前准备:
    需要用到QuecPyComTools.exe文件
-------------------------------------------------------------------------------
'''

import serial
import configparser
import sys
import os
import time
import re
import threading
import xlwt
import xlrd
from xlutils.copy import copy as xl_copy
import glob
import git
import shutil
import datetime
import wrapper_library_ec100y.common_log as common_log
import wrapper_library_ec100y.exec_dos_command as exec_dos_command
import wrapper_library_ec100y.exec_at_command as exec_at_command
import wrapper_library_ec100y.check_usb as check_usb
import wrapper_library_ec100y.common_log_queue_dict as common_log_queue_dict

def get_function_test_case(url='https://stgit.quectel.com/Randy.Zhu/lte_open_py.git',delete_original=True):
    '''
    从git上获取最新的function_case
    :param url: 指定url clone至本地
    :param delete_original: 是否删除原始git文件
    :return:
    '''
    count = 5
    while count:
        count -= 1
        if glob.glob('function_test_case'):
            break
        try:
            new_repo = git.Repo.clone_from(url=url, to_path='git_tmp')
            shutil.copytree('git_tmp/function_test_case', 'function_test_case')
            if delete_original:
                shutil.rmtree(new_repo.working_dir, True)
        except BaseException as e:
            print(e)
            time.sleep(5)
    else:
        print('已尝试5次从git拉取function_test_case失败，请检查网络连接')
        time.sleep(10)
        input('输入任意字符退出：')
    return

print = common_log.print
class SettingTools(object):

    def __init__(self):
        pass

    @classmethod
    def setting_write(self):
        """
        向Func_setting.cfg写测试参数
        :return: conf，conf_path #conf RawConfigParser方法变量，conf_path 配置文件路径
        """
        conf_path = "Func_setting.cfg"
        conf = configparser.RawConfigParser()
        return conf, conf_path

    @classmethod
    def setting_read(self):
        """
        读Func_setting.cfg中的测试参数
        :return: conf #conf RawConfigParser方法变量
        """
        conf_PATH = "Func_setting.cfg"
        conf = configparser.RawConfigParser()
        conf.read(conf_PATH)
        return conf, conf_PATH

    @classmethod
    def build_setting(self, setting, cfg_name):
        file_flag = os.path.exists('Func_setting.cfg')
        if not file_flag:
            conf, conf_path = self.setting_write()
            conf.add_section(cfg_name)
            for i in setting.keys():
                conf.set(cfg_name, i, setting[i])
            with open(conf_path, 'w+') as f:
                conf.write(f)
            print('please setting "Func_setting.cfg"')
            sys.exit(0)
        else:
            conf, conf_path =  self.setting_read()
            if cfg_name not in conf.sections():
                conf, conf_path =  self.setting_write()
                conf.add_section(cfg_name)
                for i in setting.keys():
                    conf.set(cfg_name, i, setting[i])
                with open(conf_path, 'w+') as f:
                    conf.write(f)
                print('please setting "Func_setting.cfg"')
                input('输入任意字符结束:')
                sys.exit(0)
            else:
                for i in setting.keys():
                    setting[i] = conf.get(cfg_name, i)
        # if "" in setting.values():
        #     print('please setting "Func_setting.cfg"')
        #     sys.exit(0)
        # else:
        return setting

settingtools = SettingTools()



class StartUp(object):

    def __init__(self,runtimes,uart_port='',debug_port='',usb_port='',at_port='',baudrate=int(115200),test_list='',platform='ASR'):
        if uart_port != '' and uart_port != usb_port:
            self.uart_port = serial.Serial(uart_port,baudrate,timeout=0.1)
        if debug_port != '':
            self.debug_port = serial.Serial(debug_port, baudrate, timeout=0.1)
            self.debuglog = threading.Thread(target=self.debug_read)
            self.debuglog.setDaemon(True)
            self.debuglog.start()
        self.dos = exec_dos_command.DosCmd()
        self.log = common_log.LogTools()
        self.AT = exec_at_command.ExecAtCommand(0)
        self.runtimes = runtimes
        self.usb_port = usb_port
        self.at_port = at_port
        self.baudrate = baudrate
        self.test_list = test_list
        self.platform = platform

    def debug_read(self):
        while 1:
            data = self.debug_port.readline()
            try:
                data = data.decode()
            except:
                data = str(data)
            if len(data) > 2:
                self.log.LTE_A_debug_log_put(data)

    def initialization(self):
        '''
        初始化
        :return:
        '''
        self.log.at_log_put('Module Initialization')
        result = check_usb.CheckUsbDriver(self.usb_port,
                                 check_communication=False).check_usb(30)
        if result[0]:
            time.sleep(3)
            self.usb = serial.Serial(self.usb_port,self.baudrate,timeout=0.1)
            self.usb.close()
            if self.at_port != '':
                self.at = serial.Serial(self.at_port, self.baudrate, timeout=0.1)
                if 'ASR' in self.platform.upper():
                    self.AT.send_at('AT+QDUMPCFG=0,0',3,self.at,'OK')
                    self.AT.send_at('AT+QDUMPCFG=1,0', 3, self.at, 'OK')
                    self.AT.send_at('AT+LOG=19,1', 3, self.at, 'OK')
                    self.AT.send_at('at+qflash="recoverycnt"', 3, self.at, 'OK')
                    self.AT.send_at('at+QSIMWRITECNT', 3, self.at, 'OK')
                else:
                    self.AT.send_at('AT+QDBGCFG="dumpcfg",0,1', 3, self.at, 'OK')
                    self.AT.send_at('AT^TRACECTRL=0,1,1', 3, self.at, 'OK') # 设置AP log输出至debug口
                    self.AT.send_at('at+qdbgcfg="flash"', 3, self.at, 'OK')
                    self.AT.send_at('at+qdbgcfg="memory"', 3, self.at, 'OK')
                    self.AT.send_at('at+QSIMWRITECNT', 3, self.at, 'OK')
                self.at.close()
        else:
            self.log.abnormal_log_put('USB加载失败，请确认模块是否能开机正常')
            exit()

    def func_xlwr(self, sheet_name, data):
        '''
        将固定格式的data数据处理写入result.xlsx
        :param sheet_name: sheet名称
        :param data: str (xxx::xxx||xxx::xxx;xxx:xxx||xxx::xxx;...)
        :return:
        '''
        api = []
        info = []
        result = []
        for i in data.split(';'):
            try:
                if '::' in i and '||' in i:
                    list_tmp = i.split('||')
                    list_api_info = list_tmp[0].split('::')
                    api.append(list_api_info[0]) # 执行的api个数
                    info.append(list_api_info[1])
                    list_result = list_tmp[1].split('::')
                    result.append(list_result[1])
                elif '::' in i:
                    self.log.abnormal_log_put(i)
                elif '||' in i:
                    self.log.abnormal_log_put(i)
            except Exception as e:
                self.log.abnormal_log_put('[info]%s[error]%s'%(i,e))
        # red
        pattern_red = xlwt.Pattern()  # Create the Pattern
        pattern_red.pattern = xlwt.Pattern.SOLID_PATTERN  # May be: NO_PATTERN, SOLID_PATTERN, or 0x00 through 0x12
        pattern_red.pattern_fore_colour = 2  # 0 = Black, 1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow ...
        style_red = xlwt.XFStyle()  # Create the pattern
        style_red.pattern = pattern_red  # Add pattern to style
        # green
        pattern_green = xlwt.Pattern()  # Create the Pattern
        pattern_green.pattern = xlwt.Pattern.SOLID_PATTERN  # May be: NO_PATTERN, SOLID_PATTERN, or 0x00 through 0x12
        pattern_green.pattern_fore_colour = 3  # 0 = Black, 1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow ...
        style_green = xlwt.XFStyle()  # Create the pattern
        style_green.pattern = pattern_green  # Add pattern to style
        # yellow
        pattern_yellow = xlwt.Pattern()  # Create the Pattern
        pattern_yellow.pattern = xlwt.Pattern.SOLID_PATTERN  # May be: NO_PATTERN, SOLID_PATTERN, or 0x00 through 0x12
        pattern_yellow.pattern_fore_colour = 5  # 0 = Black, 1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow ...
        style_yellow = xlwt.XFStyle()  # Create the pattern
        style_yellow.pattern = pattern_yellow  # Add pattern to style
        print(api, info, result)
        if glob.glob('RESULT.xls'):
            rb = xlrd.open_workbook('RESULT.xls', formatting_info=True)
            book = xl_copy(rb)
            sheet = book.add_sheet(sheet_name)  # 添加sheet

            sheet.write(0, 0, 'TIMESTAMP', style_yellow)  # 表头
            sheet.write(0, 1, 'API', style_yellow)  # 表头
            sheet.write(0, 2, 'TEST_INFO', style_yellow)  # 表头
            sheet.write(0, 3, 'TEST_RESULT', style_yellow)  # 表头
            for n in range(len(api)):
                sheet.write((n + 1), 0, str(datetime.datetime.now())[:19])  # 写入时间戳
                sheet.write((n + 1), 1, api[n])  # 写入测试的api
                sheet.write((n + 1), 2, info[n])  # 写入测试的info
                if 'FALSE' in result[n].upper():
                    sheet.write((n + 1), 3, result[n], style_red)  # 写入测试的result
                elif 'TRUE' in result[n].upper():
                    sheet.write((n + 1), 3, result[n], style_green)  # 写入测试的result
                else:
                    sheet.write((n + 1), 3, result[n])  # 写入测试的result
            book.save('RESULT.xls')
        else:
            with open('RESULT.xls', 'w') as f:
                book = xlwt.Workbook()  # 创建列表对象
                sheet = book.add_sheet(sheet_name)  # 添加sheet

                sheet.write(0, 0, 'TIMESTAMP', style_yellow)  # 表头
                sheet.write(0, 1, 'API', style_yellow)  # 表头
                sheet.write(0, 2, 'TEST_INFO', style_yellow)  # 表头
                sheet.write(0, 3, 'TEST_RESULT', style_yellow)  # 表头
                for n in range(len(api)):
                    sheet.write((n + 1), 0, str(datetime.datetime.now())[:19])  # 写入时间戳
                    sheet.write((n + 1), 1, api[n])  # 写入测试的api
                    sheet.write((n + 1), 2, info[n])  # 写入测试的info
                    if 'FALSE' in result[n].upper():
                        sheet.write((n + 1), 3, result[n], style_red)  # 写入测试的result
                    elif 'TRUE' in result[n].upper():
                        sheet.write((n + 1), 3, result[n], style_green)  # 写入测试的result
                    else:
                        sheet.write((n + 1), 3, result[n])  # 写入测试的result
                book.save('RESULT.xls')

    def run(self):
        '''
        主循环体
        :return:
        '''
        self.log.at_log_put('--------------Test Start---------------')
        runtime = 0
        while 1:
            common_log_queue_dict.DictObject().parameter()['Runtimes'] = runtime + 1
            self.log.at_log_put('--------------Runtimes：%s--------------'%(runtime+1))
            for i in self.test_list:
                if 'stress' or 'function' in i:
                    timeout = 9999999
                    self.runtimes = 1  #当跑测的是stress压力测试时，只运行一次
                else:
                    timeout = 360
                command = f'QuecPyComTools.exe -d {self.usb_port} -b {self.baudrate} ' + i
                print(command)
                if re.search('PowerOnOff',command) and not(re.search('getvbatt',command)):
                    command = f'QuecPyComTools.exe -d {self.usb_port} -b {self.baudrate} -t 5' + i
                    Result, re_info = self.dos.commands(command, '',timeout=timeout)
                    check_usb.CheckUsbDriver(self.usb_port,
                                             check_communication=False).check_usb(
                        60)
                else:
                    Result, re_info = self.dos.commands(command,'flush power_reset...',timeout=timeout)
                    if re.search('fota', command):
                        check_usb.CheckUsbDriver(self.usb_port,
                                                 check_communication=False).check_usb(
                            360)
                for n in re_info.split(';'):
                    if re.search('result_api: False',n):
                        self.log.abnormal_log_put(n)
                file_name = i.split('\\')[-1].replace('.py','')
                try:
                    self.func_xlwr(file_name,re_info[:-1]) # 格式化执行结果并写入excel
                except Exception as e:
                    self.log.abnormal_log_put('[error]%s'%e)
                time.sleep(3)
            runtime += 1
            if str(runtime) == str(self.runtimes):
                break
        if 'api' in str(self.test_list).lower():
            os.rename('RESULT.xls','RESULT_API.xls')  # result表格改名
        elif 'stress' in str(self.test_list).lower():
            os.rename('RESULT.xls', 'RESULT_API_STRESS.xls')  # result表格改名
        elif 'function' in str(self.test_list).lower():
            os.rename('RESULT.xls', 'RESULT_FUNCTION.xls')  # result表格改名
        else:
            print('EXCEL改名失败!!')
        self.log.at_log_put('-----------------Test End-------------------')

if __name__ == "__main__":
    get_function_test_case()
    common_log.LogTools.set_project('QuecPython')
    try:
        os.remove('RESULT.xls')
    except:
        pass
    cfg_name = 'QuecPython'
    cfg_setting = {
                    'Runtimes': '1',
                   'uart_port': 'COM3',
                   'debug_port': 'COM4',
                    'cdc_port': 'COM6',
                    'at_port': 'COM5',
                    'baudrate': '115200',
                    'test_list':
                        r'F:\projecttest\LTE-open\LTE_OPEN_PY\api_test_case\modem\modem_getcomminfo_api_test.py,'
                                r'F:\projecttest\LTE-open\LTE_OPEN_PY\api_test_case\Fs\fs_read_write_cp_api_test.py,'
                                r'F:\projecttest\LTE-open\LTE_OPEN_PY\api_test_case\net\net.py,'
                                r'F:\projecttest\LTE-open\LTE_OPEN_PY\api_test_case\modem\modem.py,'
                                r'F:\projecttest\LTE-open\LTE_OPEN_PY\api_test_case\sim\sim.py',
                    'stress_list':
                        r'F:\projecttest\LTE-open\LTE_OPEN_PY\api_test_case\audio\tts_api_stress.py',
                    'function_list':
                        r'F:\projecttest\LTE-open\LTE_OPEN_PY\function_test_case\datacall\datacall_function_test.py',
                    'runtype': 'test_list or stress_list or function_list',
                    'tooltype': '0',
                    'platform': 'asr or rda',
                   }
    conf = configparser.ConfigParser()
    set_v = settingtools.build_setting(cfg_setting, cfg_name)
    try:
        Runtimes = set_v['Runtimes']
        uart_port = set_v['uart_port']
        debug_port = set_v['debug_port']
        cdc_port = set_v['cdc_port']
        at_port = set_v['at_port']
        baudrate = set_v['baudrate']
        # test_list = eval(set_v['test_list'].replace('\\','\\\\'))
        # stress_list = eval(set_v['stress_list'].replace('\\','\\\\'))
        # function_list = eval(set_v['function_list'].replace('\\','\\\\'))
        test_list = set_v['test_list'].split(',')
        stress_list = set_v['stress_list'].split(',')
        function_list = set_v['function_list'].split(',')
        runtype = set_v['runtype']
        platform = set_v['platform']
    except:
        print('请确保配置参数的正确，温馨提示:删除配置文件可自动生成默认配置')
        time.sleep(5)
        exit()
    try:
        if 'api' in runtype.lower():
            os.remove('RESULT_API.xls')  # 删除RESULT_API.xls
        elif 'stress' in runtype.lower():
            os.remove('RESULT_API_STRESS.xls')  # 删除RESULT_API_STRESS.xls
        elif 'function' in runtype.lower():
            os.remove('RESULT_FUNCTION.xls')  # 删除RESULT_FUNCTION.xls
        os.remove('RESULT.xls')
    except Exception as e:
        pass
    if runtype == 'stress_list':#执行接口压力列表
        s = StartUp(Runtimes,uart_port,debug_port,cdc_port,at_port,baudrate,stress_list,platform)
    elif runtype == 'test_list':#执行接口遍历列表
        s = StartUp(Runtimes, uart_port, debug_port, cdc_port, at_port, baudrate, test_list,platform)
    elif runtype == 'function_list':#执行功能用例遍历列表
        s = StartUp(Runtimes, uart_port, debug_port, cdc_port, at_port, baudrate, function_list,platform)
    else:
        print("runtype配置错误，请按照指定格式配置如 runtype = 'function_list'")
    s.initialization()
    s.run()
    time.sleep(5)
