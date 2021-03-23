import re
import subprocess
import time
import os
import sys
import signal
import serial
import configparser
import wrapper_library_ec100y.common_log as common_log

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
        self.log = common_log.LogTools()

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
        self.log.at_log_put('[DOS_Cmd]%s' % (str(cmd)))
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
                    self.log.at_log_put(e)
                    self.log.at_log_put(str(s.stdout.readline()))
                if nextline == "":
                    break
            else:
                try:
                    nextline = str(s.stdout.readline().strip(), encoding='utf-8')
                except Exception as e:
                    self.log.at_log_put(e)
                    self.log.at_log_put(str(s.stdout.readline()))
            re_info += nextline
            if nextline != "":
                # print("<<<<<<",nextline)
                self.log.at_log_put('[DOS_Recv]%s' % str(nextline))

            if re.search(result, nextline):
                Result = 1
            if time.time() - time1 > timeout:
                os.kill(s.pid ,signal.CTRL_C_EVENT)
                return Result, re_info
        return Result, re_info  # 添加dos命令返回结果

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
                sys.exit(0)
            else:
                for i in setting.keys():
                    setting[i] = conf.get(cfg_name, i)
        if "" in setting.values():
            print('please setting "Func_setting.cfg"')
            sys.exit(0)
        else:
            return setting

settingtools = SettingTools()

class fs_read_write(object):

    def __init__(self,uart1_port,usb_port,baudrate,source_file):
        """ None """
        if type(uart1_port) is not serial.serialwin32.Serial:
            self.uart1_port = serial.Serial(uart1_port,int(baudrate),timeout=0.1)
        self.usb_port = usb_port
        self.dos = DosCmd()
        self.baudrate = baudrate
        self.source_file = source_file
        self.log = common_log.LogTools()

    def sc_file(self):
        # 生成工具
        name = self.source_file.split('\\')[-1]
        with open(self.source_file, "rb+") as f_sc:
            file_data = f_sc.read()
            f_sc.close()
        with open(name, "wb+") as f:
            f.write(file_data)
            f.close()

    def fs_r_w(self):
        source_size = os.path.getsize(self.source_file)
        start_cp_time = time.time()
        file_name = self.source_file.split('\\')[-1]
        cmd = f'QuecPyComTools.exe -d {self.usb_port} -b {self.baudrate} -f cp ./{file_name} :/usr/'
        self.dos.commands(cmd, '', 1800)
        end_cp_time = time.time()
        data = self.dos.commands(f'QuecPyComTools.exe -d {self.usb_port} -b {self.baudrate} -f ls /usr', f'{source_size}', 1800)
        if data[0]:
            cp_duration = end_cp_time - start_cp_time
            fs_read_write_speed = source_size/cp_duration
            self.log.at_log_put('fs_read_write_speed: %s bps,duration: %s'%(int(fs_read_write_speed),int(cp_duration)))
            self.dos.commands(f'QuecPyComTools.exe -d {self.usb_port} -b {self.baudrate} -f rm /usr/{file_name}', f'{source_size}',
                              1800)
        else:
            self.log.at_log_put('file cp fail')
            self.log.abnormal_log_put('file cp fail')
            if re.search('failed to access',data[1]):
                self.log.abnormal_log_put('[ERROR]failed to access %s'%self.usb_port)
                self.log.abnormal_log_put('保留环境...')
                while 1:
                    time.sleep(1)

    def run(self,runtimes):
        self.sc_file()
        i = 1
        self.log.at_log_put('------------Test Start--------------')
        while 1:
            self.log.at_log_put('----------Runtimes: %s--------------'%i)
            try:
                self.fs_r_w()
                time.sleep(3)
            except Exception as e:
                self.log.at_log_put(e)
            if i >= int(runtimes) and runtimes != '0':
                self.log.at_log_put('------------Test Done--------------')
                break
            i += 1

if __name__ == "__main__":
    common_log.LogTools().set_project('fs_read_write_stress')
    cfg_name = 'EC100Y_OPEN_PY_FS_READ_WRITE'
    cfg_setting = {
                    'runtimes': '0',
                   'uart1_port': 'COM3',
                    'usb_port': 'COM6',
                    'baudrate': '115200',
                    'source_file': r'F:\projecttest\LTE-open\LTE_OPEN_PY\testfile'
                   }
    conf = configparser.ConfigParser()
    set_v = settingtools.build_setting(cfg_setting, cfg_name)
    runtimes = set_v['runtimes']
    uart1_port = set_v['uart1_port']
    usb_port = set_v['usb_port']
    baudrate = set_v['baudrate']
    source_file = set_v['source_file']

    F = fs_read_write(uart1_port,usb_port,baudrate,source_file)
    F.run(runtimes)




