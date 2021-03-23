import re
import subprocess
import time
import os
import sys
import signal
import serial
import threading
import configparser

Quecpython_file_data = b'import sys\r\nimport time\r\nimport os\r\n\r\ntry:\r\n    stdout = sys.stdout.buffer\r\nexcept AttributeError:\r\n    # Python2 doesn\'t have buffer attr\r\n    stdout = sys.stdout\r\n\r\n\r\ndef stdout_write_bytes(b):\r\n    b = b.replace(b"\\x04", b"")\r\n    stdout.write(b)\r\n    stdout.flush()\r\n\r\n\r\nclass QuecpythonError(Exception):\r\n    pass\r\n\r\n\r\nclass Quecpython:\r\n    def __init__(self, device, baudrate=115200, wait=0):\r\n        import serial\r\n        delayed = False\r\n        for attempt in range(wait + 1):\r\n            try:\r\n                self.serial = serial.Serial(device, baudrate=baudrate, interCharTimeout=1)\r\n                break\r\n            except (OSError, IOError):  # Py2 and Py3 have different errors\r\n                if wait == 0:\r\n                    continue\r\n                if attempt == 0:\r\n                    sys.stdout.write("Waiting {} seconds for Quecpython ".format(wait))\r\n                    delayed = True\r\n            time.sleep(1)\r\n            sys.stdout.write(".")\r\n            sys.stdout.flush()\r\n        else:\r\n            if delayed:\r\n                print("")\r\n            raise QuecpythonError("failed to access " + device)\r\n        if delayed:\r\n            print("")\r\n\r\n    def close(self):\r\n        self.serial.close()\r\n\r\n    def read_until(self, min_num_bytes, ending, timeout=10, data_consumer=None):\r\n        # if data_consumer is used then data is not accumulated and the ending must be 1 byte long\r\n        assert data_consumer is None or len(ending) == 1\r\n\r\n        data = self.serial.read(min_num_bytes)\r\n        if data_consumer:\r\n            data_consumer(data)\r\n        timeout_count = 0\r\n        while True:\r\n            if data.endswith(ending):\r\n                break\r\n            elif self.serial.inWaiting() > 0:\r\n                new_data = self.serial.read(1)\r\n                if data_consumer:\r\n                    data_consumer(new_data)\r\n                #     data = new_data\r\n                # else:\r\n                #     data = data + new_data\r\n                data = data + new_data\r\n                timeout_count = 0\r\n            else:\r\n                timeout_count += 1\r\n                if timeout is not None and timeout_count >= 100 * timeout:\r\n                    break\r\n                time.sleep(0.01)\r\n\r\n        return data\r\n\r\n    def enter_raw_repl(self):\r\n        self.serial.write(b"\\r\\x03\\x03")  # ctrl-C twice: interrupt any running program\r\n\r\n        # flush input (without relying on serial.flushInput())\r\n        n = self.serial.inWaiting()\r\n        while n > 0:\r\n            self.serial.read(n)\r\n            n = self.serial.inWaiting()\r\n\r\n        self.serial.write(b"\\r\\x01")  # ctrl-A: enter raw REPL\r\n        data = self.read_until(1, b"raw REPL; CTRL-B to exit\\r\\n>")\r\n        if not data.endswith(b"raw REPL; CTRL-B to exit\\r\\n>"):\r\n            print(data)\r\n            raise QuecpythonError("could not enter raw repl")\r\n\r\n        self.serial.write(b"\\x04")  # ctrl-D: soft reset\r\n        data = self.read_until(1, b"soft reboot\\r\\n")\r\n        if not data.endswith(b"soft reboot\\r\\n"):\r\n            print(data)\r\n            raise QuecpythonError("could not enter raw repl")\r\n        # By splitting this into 2 reads, it allows boot.py to print stuff,\r\n        # which will show up after the soft reboot and before the raw REPL.\r\n        data = self.read_until(1, b"raw REPL; CTRL-B to exit\\r\\n")\r\n        if not data.endswith(b"raw REPL; CTRL-B to exit\\r\\n"):\r\n            print(data)\r\n            raise QuecpythonError("could not enter raw repl")\r\n\r\n    def exit_raw_repl(self):\r\n        self.serial.write(b"\\r\\x02")  # ctrl-B: enter friendly REPL\r\n\r\n    def follow(self, timeout, data_consumer=None):\r\n        # wait for normal output\r\n        data = self.read_until(1, b"\\x04", timeout=timeout, data_consumer=data_consumer)\r\n        if not data.endswith(b"\\x04"):\r\n            raise QuecpythonError("timeout waiting for first EOF reception")\r\n        data = data[:-1]\r\n\r\n        # wait for error output\r\n        data_err = self.read_until(1, b"\\x04", timeout=timeout)\r\n        if not data_err.endswith(b"\\x04"):\r\n            raise QuecpythonError("timeout waiting for second EOF reception")\r\n        data_err = data_err[:-1]\r\n\r\n        # return normal and error output\r\n        return data, data_err\r\n\r\n    def exec_raw_no_follow(self, command):\r\n        if isinstance(command, bytes):\r\n            command_bytes = command\r\n        else:\r\n            command_bytes = bytes(command, encoding="utf8")\r\n\r\n        # check we have a prompt\r\n        data = self.read_until(1, b">")\r\n        if not data.endswith(b">"):\r\n            raise QuecpythonError("could not enter raw repl")\r\n\r\n        # write command\r\n        for i in range(0, len(command_bytes), 256):\r\n            self.serial.write(command_bytes[i: min(i + 256, len(command_bytes))])\r\n            time.sleep(0.1)\r\n        self.serial.write(b"\\x04")\r\n\r\n        # check if we could exec command\r\n        data = self.serial.read(2)\r\n        if data != b"OK":\r\n            raise QuecpythonError("could not exec command (response: %r)" % data)\r\n\r\n    def exec_raw(self, command, timeout=10, data_consumer=None):\r\n        self.exec_raw_no_follow(command)\r\n        return self.follow(timeout, data_consumer)\r\n\r\n    def eval(self, expression):\r\n        ret = self.exec_("print({})".format(expression))\r\n        ret = ret.strip()\r\n        return ret\r\n\r\n    def exec_(self, command, data_consumer=None):\r\n        ret, ret_err = self.exec_raw(command, data_consumer=data_consumer)\r\n        if ret_err:\r\n            raise QuecpythonError("exception", ret, ret_err)\r\n        return ret\r\n\r\n    def execfile(self, filename):\r\n        with open(filename, "rb") as f:\r\n            pyfile = f.read()\r\n            print(pyfile)\r\n        return self.exec_(pyfile)\r\n\r\n    def fs_ls(self, src):\r\n        cmd = (\r\n                "import uos\\nfor f in uos.ilistdir(%s):\\n"\r\n                " print(\'{:12} {}{}\'.format(f[3]if len(f)>3 else 0,f[0],\'/\'if f[1]&0x4000 else \'\'))"\r\n                % (("\'%s\'" % src) if src else "")\r\n        )\r\n        self.exec_(cmd, data_consumer=stdout_write_bytes)\r\n\r\n    def fs_cat(self, src, chunk_size=256):\r\n        cmd = (\r\n                "with open(\'%s\') as f:\\n while 1:\\n"\r\n                "  b=f.read(%u)\\n  if not b:break\\n  print(b,end=\'\')" % (src, chunk_size)\r\n        )\r\n        self.exec_(cmd, data_consumer=stdout_write_bytes)\r\n\r\n    def fs_get(self, src, dest, chunk_size=256):\r\n        self.exec_("f=open(\'%s\',\'rb\')\\nr=f.read" % src)\r\n        with open(dest, "wb") as f:\r\n            while True:\r\n                data = bytearray()\r\n                self.exec_("print(r(%u))" % chunk_size, data_consumer=lambda d: data.extend(d))\r\n                assert data.endswith(b"\\r\\n\\x04")\r\n                data = eval(str(data[:-3], "ascii"))\r\n                if not data:\r\n                    break\r\n                f.write(data)\r\n        self.exec_("f.close()")\r\n\r\n    def fs_put(self, src, dest, chunk_size=256):\r\n        self.exec_("f=open(\'%s\',\'wb\')\\nw=f.write" % dest)\r\n        with open(src, "rb") as f:\r\n            while True:\r\n                data = f.read(chunk_size)\r\n                if not data:\r\n                    break\r\n                if sys.version_info < (3,):\r\n                    self.exec_("w(b" + repr(data) + ")")\r\n                else:\r\n                    self.exec_("w(" + repr(data) + ")")\r\n        self.exec_("f.close()")\r\n\r\n    def fs_mkdir(self, dir):\r\n        self.exec_("import uos\\nuos.mkdir(\'%s\')" % dir)\r\n\r\n    def fs_rmdir(self, dir):\r\n        self.exec_("import uos\\nuos.rmdir(\'%s\')" % dir)\r\n\r\n    def fs_rm(self, src):\r\n        self.exec_("import uos\\nuos.remove(\'%s\')" % src)\r\n\r\n\r\nsetattr(Quecpython, "exec", Quecpython.exec_)\r\n\r\n\r\ndef execfile(filename, device="COM24", baudrate=115200):\r\n    qpy = Quecpython(device, baudrate)\r\n    qpy.enter_raw_repl()\r\n    output = qpy.execfile(filename)\r\n    stdout_write_bytes(output)\r\n    qpy.exit_raw_repl()\r\n    qpy.close()\r\n\r\n\r\ndef filesystem_command(qpy, args):\r\n    def fname_remote(src):\r\n        if src.startswith(":"):\r\n            src = src[1:]\r\n        return src\r\n\r\n    def fname_cp_dest(src, dest):\r\n        src = src.rsplit("/", 1)[-1]\r\n        if dest is None or dest == "":\r\n            dest = src\r\n        elif dest == ".":\r\n            dest = "./" + src\r\n        elif dest.endswith("/"):\r\n            dest += src\r\n        return dest\r\n\r\n    cmd = args[0]\r\n    args = args[1:]\r\n    try:\r\n        if cmd == "cp":\r\n            srcs = args[:-1]\r\n            dest = args[-1]\r\n            if srcs[0].startswith("./") or dest.startswith(":"):\r\n                op = qpy.fs_put\r\n                fmt = "cp %s :%s"\r\n                dest = fname_remote(dest)\r\n            else:\r\n                op = qpy.fs_get\r\n                fmt = "cp :%s %s"\r\n            for src in srcs:\r\n                src = fname_remote(src)\r\n                dest2 = fname_cp_dest(src, dest)\r\n                print(fmt % (src, dest2))\r\n                op(src, dest2)\r\n        else:\r\n            op = {\r\n                "ls": qpy.fs_ls,\r\n                "cat": qpy.fs_cat,\r\n                "mkdir": qpy.fs_mkdir,\r\n                "rmdir": qpy.fs_rmdir,\r\n                "rm": qpy.fs_rm,\r\n            }[cmd]\r\n            if cmd == "ls" and not args:\r\n                args = [""]\r\n            for src in args:\r\n                src = fname_remote(src)\r\n                print("%s :%s" % (cmd, src))\r\n                op(src)\r\n    except QuecpythonError as er:\r\n        print(str(er.args[2], "ascii"))\r\n        qpy.exit_raw_repl()\r\n        qpy.close()\r\n        sys.exit(1)\r\n\r\ndef main():\r\n    import argparse\r\n    cmd_parser = argparse.ArgumentParser(description="Run scripts on the EC100Y.")\r\n    cmd_parser.add_argument(\r\n        "-d",\r\n        "--device",\r\n        default=os.environ.get("EC100Y_DEVICE", "COM24"),\r\n        help="the serial device of the EC100Y",\r\n    )\r\n    cmd_parser.add_argument(\r\n        "-b",\r\n        "--baudrate",\r\n        default=os.environ.get("EC100Y_BAUDRATE", "115200"),\r\n        help="the baud rate of the serial device",\r\n    )\r\n    cmd_parser.add_argument("-c", "--command", help="program passed in as string")\r\n    cmd_parser.add_argument(\r\n        "-w",\r\n        "--wait",\r\n        default=0,\r\n        type=int,\r\n        help="seconds to wait for USB connected board to become available",\r\n    )\r\n    cmd_parser.add_argument(\r\n        "-t",\r\n        "--runtimeout",\r\n        default=None,\r\n        type=int,\r\n        help="kill thread after runtimout without no data",\r\n    )\r\n    group = cmd_parser.add_mutually_exclusive_group()\r\n    group.add_argument(\r\n        "--follow",\r\n        action="store_true",\r\n        help="follow the output after running the scripts [default if no scripts given]",\r\n    )\r\n    group.add_argument(\r\n        "--no-follow",\r\n        action="store_true",\r\n        help="Do not follow the output after running the scripts.",\r\n    )\r\n    cmd_parser.add_argument(\r\n        "-f", "--filesystem", action="store_true", help="perform a filesystem action"\r\n    )\r\n    cmd_parser.add_argument("files", nargs="*", help="input files")\r\n    args = cmd_parser.parse_args()\r\n    # open the connection to the qpyoard\r\n    try:\r\n        qpy = Quecpython(args.device, args.baudrate, args.wait)\r\n    except QuecpythonError as er:\r\n        print(er)\r\n        sys.exit(1)\r\n\r\n    # run any command or file(s)\r\n    if args.command is not None or args.filesystem or len(args.files):\r\n        # we must enter raw-REPL mode to execute commands\r\n        # this will do a soft-reset of the board\r\n        try:\r\n            qpy.enter_raw_repl()\r\n        except QuecpythonError as er:\r\n            print(er)\r\n            qpy.close()\r\n            sys.exit(1)\r\n\r\n        def execbuffer(buf):\r\n            try:\r\n                if args.no_follow:\r\n                    qpy.exec_raw_no_follow(buf)\r\n                    ret_err = None\r\n                else:\r\n                    ret, ret_err = qpy.exec_raw(\r\n                        buf, timeout=args.runtimeout, data_consumer=stdout_write_bytes\r\n                    )\r\n            except QuecpythonError as er:\r\n                print(er)\r\n                qpy.close()\r\n                sys.exit(1)\r\n            except KeyboardInterrupt:\r\n                sys.exit(1)\r\n            if ret_err:\r\n                qpy.exit_raw_repl()\r\n                qpy.close()\r\n                stdout_write_bytes(ret_err)\r\n                sys.exit(1)\r\n\r\n        # do filesystem commands, if given\r\n        if args.filesystem:\r\n            filesystem_command(qpy, args.files)\r\n            del args.files[:]\r\n\r\n        # run the command, if given\r\n        if args.command is not None:\r\n            execbuffer(args.command.encode("utf-8"))\r\n\r\n        # run any files\r\n        for filename in args.files:\r\n            with open(filename, "rb") as f:\r\n                pyfile = f.read()\r\n                execbuffer(pyfile)\r\n\r\n        # exiting raw-REPL just drops to friendly-REPL mode\r\n        qpy.exit_raw_repl()\r\n\r\n    # if asked explicitly, or no files given, then follow the output\r\n    if args.follow or (args.command is None and not args.filesystem and len(args.files) == 0):\r\n        try:\r\n            ret, ret_err = qpy.follow(timeout=args.runtimeout, data_consumer=stdout_write_bytes)\r\n        except QuecpythonError as er:\r\n            print(er)\r\n            sys.exit(1)\r\n        except KeyboardInterrupt:\r\n            sys.exit(1)\r\n        if ret_err:\r\n            qpy.close()\r\n            stdout_write_bytes(ret_err)\r\n            sys.exit(1)\r\n\r\n    # close the connection to the qpyoard\r\n    qpy.close()\r\n\r\n\r\nif __name__ == "__main__":\r\n    main()'
f = open(r'F:\projecttest\LTE-open\LTE_OPEN_PY\weifuzhitong\uart_api_test.py','rb')
uart_api_file_data = f.read()

def uart_api_file_produce(file_data):
    # 生成工具
    name = "uart_api_test.py"
    with open(name, "wb+") as f:
        f.write(file_data)
        f.close()
#uart_api_file_produce(uart_api_file_data)

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
        #self.at_log = common_log.LogTools.at_log_put

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
        print('[DOS_Cmd]%s' % (str(cmd)))
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
                print('[DOS_Recv]%s' % str(nextline))

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

class uart_read_write(object):

    def __init__(self,uart1_port,usb_port,baudrate):
        """ None """
        if type(uart1_port) is not serial.serialwin32.Serial:
            self.uart1_port = serial.Serial(uart1_port,int(baudrate),timeout=1)
        # if type(usb_port) is not serial.serialwin32.Serial:
        #     self.usb_port = serial.Serial(usb_port, int(baudrate), timeout=0.1)
        self.usb_port = usb_port
        self.dos = DosCmd()
        self.baudrate = baudrate

    def uart1(self,a):
        while 1:
            data = self.uart1_port.read(1024)
            print(len(data))
            if len(data):
                print('[uart_rev_from_module]%s' % (data.decode()))
                self.uart1_port.write(data)
            else:
                pass

    def module_api(self):
        cmd = f'QuecPyComTools.exe -d {self.usb_port} -b {self.baudrate} ./uart_api_test.py'
        self.dos.commands(cmd,'',9999999999)

    def run(self):
        print('-----------------Test Start-----------------')
        t = threading.Thread(target=self.uart1,args=('1',))
        t.setDaemon(True)
        t.start()
        self.module_api()
        while 1:
            pass


if __name__ == "__main__":
    cfg_name = 'EC100Y_OPEN_PY_UART_READ_WRITE'
    cfg_setting = {
                   'uart1_port': 'COM3',
                    'usb_port': 'COM6',
                    'baudrate': '115200',
                   }
    conf = configparser.ConfigParser()
    set_v = settingtools.build_setting(cfg_setting, cfg_name)
    uart1_port = set_v['uart1_port']
    usb_port = set_v['usb_port']
    baudrate = set_v['baudrate']

    U = uart_read_write(uart1_port,usb_port,baudrate)
    U.run()

