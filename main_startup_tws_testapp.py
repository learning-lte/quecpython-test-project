import argparse
import os,time,json
import xlwt
import xlrd
from xlutils.copy import copy as xl_copy
import configparser
import glob
import re
from tapp_constructor import constructor, auto_handler, app_exception, log
"""
从tapp_constructor中导入模块     constructor
                                auto_handler
                                app_exception
                                log
"""
# 自定义初始化业务或收尾类，继承SetOperation类，重写run方法
# 初始化业务 在设备升级之后，测试之前执行
# 初始化业务 默认不生效，实例化后，调用ebable()生效
class  MyInitializeOperation(constructor.SetOperation):
    def run(self, **params):
        import threading
        main_device = constructor.main_device       # 主设备 auto_handler.TestDevice 类实例
        device_adb_id = main_device.adb_id
        atmf_path = auto_handler.search_file_from_dir('atmf', os.getcwd())  # 查找atmf路径
        code = os.system(r'adb -s %s push %s /data' % (device_adb_id, atmf_path))   # push atmf
        if code != 0:
            raise app_exception.TestFail('push atmf failed, error code: %s' % code)
        log.app_log.info('atmf push success')        # INFO日志记录
        code = os.system(r'adb -s %s shell chmod 777 /data/atmf' % device_adb_id)   # chmod atmf
        if code != 0:
            raise app_exception.TestFail('atmf change mode failed, error code: %s' % code)
        log.app_log.info('atmf change mode success')        # INFO日志记录
        # 启动atmf阻塞，使用子线程启动
        atmf_start_th = threading.Thread(target=os.system, args=(r'adb -s %s shell /data/atmf' % device_adb_id,))
        atmf_start_th.setDaemon = True
        atmf_start_th.start()
        log.app_log.info('atmf started')        # INFO日志记录


# class MyTestOperation(constructor.TestOperation):   # TestOperation,自定义测试业务类继承该类，重写run方法
#     def run(self, **params):
#         try:
#             """
#             App执行测试业务会传入参数case_setting, dict类型
#             """
#             case_setting = params['case_setting']   # 取得case_setting
#             case_id = case_setting['tr_temp_id']   # case_id,上报case信息用该id
#             """
#             constructor 提供下列属性供使用
#             """
#             main_device = constructor.main_device       # 主设备 auto_handler.TestDevice 类实例
#             minor_device = constructor.minor_device     # 辅设备 auto_handler.TestDevice 类实例，无辅设备则为None
#             devices = constructor.devices         # list类型，含 主设备 辅设备（无辅设备则不含）
#             task_record = constructor.task_record       # 任务记录 auto_handler.TestRecord 类实例
#             original_setting = constructor.original_setting     # Monotor启动App的参数源数据，dict类型
#             main_task_id = constructor.main_task_id     # Monotor启动App的task_id  本次测试任务的唯一标识(上报业务状态不能用此id)
#             main_device_config  = main_device.config   # 设备（测试资源）的配置,数据格式如下
#             """
#             main_device_config的数据格式:
#             {'adb_id': '', 'baud_rate': 115200, 'chipPlatform': 'MDM9240-1', 'debug': 'COM', 'hardwareType': 'EG06ELA',
#             'sim_card_type': '3',
#             'sim_info': [{'sim_operator': 'CMCC', 'slot_number': 1}, {'sim_operator': 'CT', 'slot_number': 2}, {'sim_operator': 'None', 'slot_number': 3}],
#             'switcher': 'COM15', 'uart': 'COM23', 'upgrade': 'COM39', 'usbat': 'COM37', 'usbmodem': 'COM50',
#             'version_type': '0', 'version_upgrade': '0', 'wiring_method': '0'}
#             """
#             """
#             类提供以下方法：
#             upload_steplog      上传TWS中的Steplog,展现给测试人员，当前case的执行的步骤
#             upload_operation_status   上传状态，不建议使用。
#             log_info    记录info日志        # 不建议使用 log.app_log.info
#             log_error   记录error日志       # 不建议使用 log.app_log.error
#             get_test_timestamp  获取测试时间戳
#             note_casestep_pass      记录一行PASS的caselog       # 不建议使用 ah.auto_handler.save_standard_report()
#             note_casestep_fail      记录一行FAIL的caselog       # 不建议使用 ah.auto_handler.save_standard_report()
#             commit_operation_progress   上传进度        # 不建议使用 upload_operation_status
#             commit_operation_status     上传状态        # 不建议使用 upload_operation_status
#             """
#             self.upload_steplog('Start test XXXXX')     # 上传TWS中的Steplog,展现给测试人员，当前case的执行的步骤
#             self.log_info('Start test XXXXX')   # App log 记录 info 级别
#             self.upload_steplog('Start phase I - XXX')
#             pass    # 自定义业务
#             self.commit_operation_progress(30)  # 上传测试进度 30%(针对本case,TWS上的进度会根据case条数和case进度换算总进度)
#             self.note_casestep_pass()   # 记录一行PASS的excel log  所有标题均为空，结果为PASS，测试时间为执行此行代码的时间
#             time.sleep(1)
#             test_time = self.get_test_timestamp()       # 获取当前时间戳
#             time.sleep(5)
#             pass    # 自定义业务
#             self.note_casestep_pass(test_time,    # 记录一行PASS的excel log ,测试时间为5秒前的test_time
#                                     ATCommand='按标准的QAT log的表头传参',
#                                     WaitResult='想写啥写啥',
#                                     Timeout='不想写就不写',
#                                     Runtimes='所有的表头都不是必传的',
#                                     CheckedInfo='传不传随你',
#                                     Notes='上一次调用note_casestep_pass啥都不传也行')
#             self.upload_steplog('Phase II - XXX')
#             self.commit_operation_progress(60)  # 上传测试进度 30%
#             self.note_casestep_fail()   # 记录一行FAIL的excel log  所有标题均为空，结果为PASS，测试时间为执行此行代码的时间
#             time.sleep(1)
#             test_time = self.get_test_timestamp()       # 获取当前时间戳
#             time.sleep(5)
#             self.upload_steplog('I am test.')    # 自定义业务
#             self.note_casestep_fail(test_time,    # 记录一行FAIL的excel log ,测试时间为5秒前的test_time
#                                     ATCommand='传参与上面一致')
#             self.commit_operation_progress(100)     # 上传测试进度 100%
#             self.commit_operation_status(status='2')        # 上传状态码'2'，代表正常结束
#             # self.upload_operation_status(task_id=case_id,         # 不建议再用
#             #                              status='2',
#             #                              report_path='report_path',
#             #                              task_info='task_info')
#
#             self.log_info('Test Over')        # App log 记录 info 级别
#             # log.app_log.info('INFO LOG')        # 不建议再用
#         except Exception as e:
#             self.log_error(repr(e))       # App log 记录 error 级别
#             self.commit_operation_status(status='3',        # 上传状态码'3'，代表异常，最好将错误信息也上传
#                                          task_info=str(e))
#             # log.app_log.error('ERROR LOG')        # 不建议再用
#             # self.upload_operation_status(task_id=case_id,         # 不建议再用
#             #                              status='3',
#             #                              report_path='report_path',
#             #                              task_info=str(e))

class PythonTestOperation(constructor.TestOperation):   # TestOperation,自定义测试业务类继承该类，重写run方法
    case_index = 0

    def run(self, **params):
        try:
            """
            App执行测试业务会传入参数case_setting, dict类型
            """
            case_setting = params['case_setting']   # 取得case_setting
            case_id = case_setting['tr_temp_id']   # case_id,上报case信息用该id
            app_name = case_setting['summary']

            """
            constructor 提供下列属性供使用
            """
            main_device = constructor.main_device       # 主设备 auto_handler.TestDevice 类实例
            minor_device = constructor.minor_device     # 辅设备 auto_handler.TestDevice 类实例，无辅设备则为None
            devices = constructor.devices         # list类型，含 主设备 辅设备（无辅设备则不含）
            task_record = constructor.task_record       # 任务记录 auto_handler.TestRecord 类实例
            original_setting = constructor.original_setting     # Monotor启动App的参数源数据，dict类型
            main_task_id = constructor.main_task_id     # Monotor启动App的task_id  本次测试任务的唯一标识(上报业务状态不能用此id)
            main_device_config  = main_device.config   # 设备（测试资源）的配置,数据格式如下
            if self.case_index == 0:
                script_context = eval(case_setting['script_context'])  # script_context
                if re.search('(\d+)', str(main_device_config['baud_rate'])):
                    script_context['baudrate'] = main_device_config['baud_rate']
                else:
                    script_context['baudrate'] = 115200
                if re.search('COM(\d+)',main_device_config['uart']):
                    script_context['uart_port'] = main_device_config['uart']
                else:
                    script_context['uart_port'] = ''
                if re.search('COM(\d+)', main_device_config['debug']):
                    script_context['debug_port'] = main_device_config['debug']
                else:
                    script_context['debug_port'] = ''
                if re.search('COM(\d+)', main_device_config['usbat']):
                    script_context['at_port'] = main_device_config['usbat']
                else:
                    script_context['at_port'] = ''
                # if re.search('COM(\d+)', main_device_config['com1']):
                #     script_context['cdc_port'] = main_device_config['com1']
                # else:
                #     script_context['cdc_port'] = ''
                SettingTools().build_setting(str(script_context))
            """
            main_device_config的数据格式:
            {'adb_id': '', 'baud_rate': 115200, 'chipPlatform': 'MDM9240-1', 'debug': 'COM', 'hardwareType': 'EG06ELA', 
            'sim_card_type': '3', 
            'sim_info': [{'sim_operator': 'CMCC', 'slot_number': 1}, {'sim_operator': 'CT', 'slot_number': 2}, {'sim_operator': 'None', 'slot_number': 3}],
            'switcher': 'COM15', 'uart': 'COM23', 'upgrade': 'COM39', 'usbat': 'COM37', 'usbmodem': 'COM50', 
            'version_type': '0', 'version_upgrade': '0', 'wiring_method': '0'}
            """
            """
            类提供以下方法：
            upload_steplog      上传TWS中的Steplog,展现给测试人员，当前case的执行的步骤
            upload_operation_status   上传状态，不建议使用。
            log_info    记录info日志        # 不建议使用 log.app_log.info
            log_error   记录error日志       # 不建议使用 log.app_log.error
            get_test_timestamp  获取测试时间戳
            note_casestep_pass      记录一行PASS的caselog       # 不建议使用 ah.auto_handler.save_standard_report()
            note_casestep_fail      记录一行FAIL的caselog       # 不建议使用 ah.auto_handler.save_standard_report()
            commit_operation_progress   上传进度        # 不建议使用 upload_operation_status
            commit_operation_status     上传状态        # 不建议使用 upload_operation_status
            """
            self.upload_steplog(f'Start test {app_name}')  # 上传TWS中的Steplog,展现给测试人员，当前case的执行的步骤
            self.log_info(f'Start test {app_name}')  # App log 记录 info 级别
            time.sleep(1)
            test_time = self.get_test_timestamp()  # 获取当前时间戳
            time.sleep(5)
            self.commit_operation_progress(10)  # 上传测试进度 30%(针对本case,TWS上的进度会根据case条数和case进度换算总进度)
            # self.upload_steplog(f'I am test {app_name}')  # 自定义业务
            if self.case_index == 0:
                os.system('main_startup.exe')
            self.commit_operation_progress(90)  # 上传测试进度 30%(针对本case,TWS上的进度会根据case条数和case进度换算总进度)
            excel = glob.glob('RESULT*.xls')[0]
            autopython_result_list = []
            autopython_info_list = []
            rb = xlrd.open_workbook(excel, formatting_info=True)
            sheet = rb.sheet_by_index(0)  # 读取sheet
            for i in range(1,sheet.nrows):
                test_result = sheet.cell(i,3).value
                test_info = sheet.cell(i, 2).value
                if test_result.upper() != ' N/A':
                    autopython_result_list.append(test_result)
                    autopython_info_list.append(test_info)
            if autopython_result_list[self.case_index].upper() == ' TRUE':
                self.note_casestep_pass(Notes=autopython_info_list[self.case_index])  # 记录一行PASS的excel log  所有标题均为空，结果为PASS，测试时间为执行此行代码的时间
            elif autopython_result_list[self.case_index].upper() == ' FALSE':
                self.note_casestep_fail(
                    Notes=autopython_info_list[self.case_index])  # 记录一行FAIL的excel log  所有标题均为空，结果为PASS，测试时间为执行此行代码的时间
            self.commit_operation_progress(100)     # 上传测试进度 100%
            self.commit_operation_status(status='2')        # 上传状态码'2'，代表正常结束
            self.case_index += 1
            # self.upload_operation_status(task_id=case_id,         # 不建议再用
            #                              status='2',
            #                              report_path='report_path',
            #                              task_info='task_info')

            self.log_info('Test Over')        # App log 记录 info 级别
            # log.app_log.info('INFO LOG')        # 不建议再用
        except Exception as e:
            self.log_error(repr(e))       # App log 记录 error 级别
            self.commit_operation_status(status='3',        # 上传状态码'3'，代表异常，最好将错误信息也上传
                                         task_info=str(e))
            # log.app_log.error('ERROR LOG')        # 不建议再用
            # self.upload_operation_status(task_id=case_id,         # 不建议再用
            #                              status='3',
            #                              report_path='report_path',
            #                              task_info=str(e))

class SettingTools(constructor.TestOperation):

    def setting_write(self):
        """
        向Func_setting.cfg写测试参数
        :return: conf，conf_path #conf RawConfigParser方法变量，conf_path 配置文件路径
        """
        conf_path = "Func_setting.cfg"
        conf = configparser.RawConfigParser()
        return conf, conf_path

    def build_setting(self, msg, cfg_name='QuecPython'):
        try:
            setting = eval(msg)
        except Exception as e:
            self.log_error('TestAPP is incorrect setting!! info:%s'%e)
            exit(0)
        conf, conf_path = self.setting_write()
        conf.add_section(cfg_name)
        for i in setting.keys():
            conf.set(cfg_name, i, setting[i])
        with open(conf_path, 'w+') as f:
            conf.write(f)
        # if "" in setting.values():
        #     print('please setting "Func_setting1111.cfg"')
        #     sys.exit(0)
        # else:
        return setting

# class BinTestOperation(constructor.TestOperation):   # TestOperation,自定义测试业务类继承该类，重写run方法
#     def run(self, **params):
#         try:
#             """
#             App执行测试业务会传入参数case_setting, dict类型
#             """
#             case_setting = params['case_setting']   # 取得case_setting
#             case_id = case_setting['tr_temp_id']   # case_id,上报case信息用该id
#             """
#             constructor 提供下列属性供使用
#             """
#             main_device = constructor.main_device       # 主设备 auto_handler.TestDevice 类实例
#             minor_device = constructor.minor_device     # 辅设备 auto_handler.TestDevice 类实例，无辅设备则为None
#             devices = constructor.devices         # list类型，含 主设备 辅设备（无辅设备则不含）
#             task_record = constructor.task_record       # 任务记录 auto_handler.TestRecord 类实例
#             original_setting = constructor.original_setting     # Monotor启动App的参数源数据，dict类型
#             main_task_id = constructor.main_task_id     # Monotor启动App的task_id  本次测试任务的唯一标识(上报业务状态不能用此id)
#             main_device_config  = main_device.config   # 设备（测试资源）的配置,数据格式如下
#             """
#             main_device_config的数据格式:
#             {'adb_id': '', 'baud_rate': 115200, 'chipPlatform': 'MDM9240-1', 'debug': 'COM', 'hardwareType': 'EG06ELA',
#             'sim_card_type': '3',
#             'sim_info': [{'sim_operator': 'CMCC', 'slot_number': 1}, {'sim_operator': 'CT', 'slot_number': 2}, {'sim_operator': 'None', 'slot_number': 3}],
#             'switcher': 'COM15', 'uart': 'COM23', 'upgrade': 'COM39', 'usbat': 'COM37', 'usbmodem': 'COM50',
#             'version_type': '0', 'version_upgrade': '0', 'wiring_method': '0'}
#             """
#             """
#             类提供以下方法：
#             upload_steplog      上传TWS中的Steplog,展现给测试人员，当前case的执行的步骤
#             upload_operation_status   上传状态，不建议使用。
#             log_info    记录info日志        # 不建议使用 log.app_log.info
#             log_error   记录error日志       # 不建议使用 log.app_log.error
#             get_test_timestamp  获取测试时间戳
#             note_casestep_pass      记录一行PASS的caselog       # 不建议使用 ah.auto_handler.save_standard_report()
#             note_casestep_fail      记录一行FAIL的caselog       # 不建议使用 ah.auto_handler.save_standard_report()
#             commit_operation_progress   上传进度        # 不建议使用 upload_operation_status
#             commit_operation_status     上传状态        # 不建议使用 upload_operation_status
#             """
#             self.upload_steplog('Start test XXXXX')     # 上传TWS中的Steplog,展现给测试人员，当前case的执行的步骤
#             self.log_info('Start test XXXXX')   # App log 记录 info 级别
#             self.upload_steplog('Start phase I - XXX')
#             pass    # 自定义业务
#             self.commit_operation_progress(30)  # 上传测试进度 30%(针对本case,TWS上的进度会根据case条数和case进度换算总进度)
#             self.note_casestep_pass()   # 记录一行PASS的excel log  所有标题均为空，结果为PASS，测试时间为执行此行代码的时间
#             time.sleep(1)
#             test_time = self.get_test_timestamp()       # 获取当前时间戳
#             time.sleep(5)
#             pass    # 自定义业务
#             self.note_casestep_pass(test_time,    # 记录一行PASS的excel log ,测试时间为5秒前的test_time
#                                     ATCommand='按标准的QAT log的表头传参',
#                                     WaitResult='想写啥写啥',
#                                     Timeout='不想写就不写',
#                                     Runtimes='所有的表头都不是必传的',
#                                     CheckedInfo='传不传随你',
#                                     Notes='上一次调用note_casestep_pass啥都不传也行')
#             self.upload_steplog('Phase II - XXX')
#             self.commit_operation_progress(60)  # 上传测试进度 30%
#             self.note_casestep_fail()   # 记录一行FAIL的excel log  所有标题均为空，结果为PASS，测试时间为执行此行代码的时间
#             test_time = self.get_test_timestamp()       # 获取当前时间戳
#             time.sleep(5)
#             self.upload_steplog('I am test.')    # 自定义业务
#             self.note_casestep_fail(test_time,    # 记录一行FAIL的excel log ,测试时间为5秒前的test_time
#                                     ATCommand='传参与上面一致')
#             self.commit_operation_progress(100)     # 上传测试进度 100%
#             self.commit_operation_status(status='2')        # 上传状态码'2'，代表正常结束
#             # self.upload_operation_status(task_id=case_id,         # 不建议再用
#             #                              status='2',
#             #                              report_path='report_path',
#             #                              task_info='task_info')
#
#             self.log_info('Test Over')        # App log 记录 info 级别
#             # log.app_log.info('INFO LOG')        # 不建议再用
#         except Exception as e:
#             self.log_error(repr(e))       # App log 记录 error 级别
#             self.commit_operation_status(status='3',        # 上传状态码'3'，代表异常，最好将错误信息也上传
#                                          task_info=str(e))
#             # log.app_log.error('ERROR LOG')        # 不建议再用
#             # self.upload_operation_status(task_id=case_id,         # 不建议再用
#             #                              status='3',
#             #                              report_path='report_path',
#             #                              task_info=str(e))

ID = {'task_id': '1353520258765297415',
      'version_path': '\\\\192.168.11.252\\quectel\\Project\\Module Project Files\\LTE Project\\ASR1802S\\EC200-TCN-DA\\Release',
      'version_name': 'EC600SCNAAR01A02V03M16_OCPU_PY',
      'case_addr': 'https://stres.quectel.com:8139/quectel1/M00/02/17/wKgXZmA-4miARYauAAADOO2R6Oc99.json?attname=Modem_Test-20201209195011.json',
      'name_group': 'Maxton_Test', 'app_name': 'testapp_rdBETA-v1209.exe',
      'app_url': 'https://stres.quectel.com:8139/quectel1/M00/00/A8/wKgXZl_QQE2AbyqSAR4N3gwN6xU785.exe?attname=testapp_rdBETA-v1209.exe',
      'res': [{'version_type': '2', 'version_upgrade': '0', 'wiring_method': '0',
               'hardwareType': 'EC600SCNAA', 'chipPlatform': 'ASR1601', 'baud_rate': 115200, 'adb_id': '',
               'uart': 'COM3', 'usbat': 'COM64', 'usbmodem': 'COM66', 'upgrade': 'COM1', 'switcher': 'COM',
               "sim_card_type": "3",
        "sim_info": [{
            "sim_operator": "CMCC",
            "slot_number": 1
        }],}]}

# tmp = {
# "app_url": "Modem",
# "Runtimes": "1",
# "uart_port": "COM3",
# "debug_port": "COM4",
# "cdc_port": "COM63",
# "at_port": "COM64",
# "baudrate": "115200",
# "test_list": "",
# "stress_list": "",
# "function_list": "function_test_case\\modem_function_test.py",
# "runtype": "function_list",
# "tooltype": "0"
# }
# SettingTools().build_setting(json.dumps(tmp))
# my_app = constructor.TestApp(json.dumps(ID))   # TestApp类，初始化参数是启动app的参数，默认的测试是标准的测试流程
# # bin_operation = BinTestOperation()
# python_operation = PythonTestOperation()
# # my_app.AUTO_BIN_OPERATION = bin_operation        # bin业务
# my_app.AUTO_PYTHON_OPERATION = python_operation        # python业务
# my_app.start()      # 执行测试


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get Test Setting')
    parser.add_argument('--m', dest='test_setting', type=str)
    args = parser.parse_args()
    my_app = constructor.TestApp(**vars(args))   # TestApp类，初始化参数是启动app的参数，默认的测试是标准的测试流程
    # print(vars(args))
    my_operation = PythonTestOperation()
#     # my_initialize_operation = MyInitializeOperation()
#     bin_operation = BinTestOperation()
#     """
#     app中的业务 修改为你的业务
#     请选择修改，未修改的按默认测试业务执行
#     """
#     # my_app.INITIALIZE_OPERATION = my_initialize_operation
#     # my_app.INITIALIZE_OPERATION.enable()    # 初始化业务默认是关闭的，调用enable使生效
#     my_app.UPGRADE_OPERATION = my_operation       # 升级业务
    # my_app.AUTO_QAT_OPERATION = my_operation           # QAT业务
#     # my_app.AUTO_PERL_OPERATION = my_operation       # perl业务
#     my_app.AUTO_BIN_OPERATION = bin_operation        # bin业务
#     # my_app.AUTO_LP_OPERATION = my_operation     # lp业务
    my_app.AUTO_PYTHON_OPERATION = my_operation     # python业务
#     # my_app.AUTO_AUDIO_OPERATION = my_operation     # audio业务
#     """
#     disable升级业务，App的标准流程中的升级流程就不再执行
#     测试业务不提供disable功能
#     """
    my_app.UPGRADE_OPERATION.disable()
    my_app.start()      # 执行测试