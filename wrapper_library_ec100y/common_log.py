#!/usr/bin/env python 
# -*- coding: utf-8 -*-
'''
-------------------------------------------------------------------------------
脚本名称:  common_log
需求来源:
    log日志记录功能以及信息的传递
测试目的：
    log日志记录功能以及信息的传递
修改记录:
    初始版本V1.0 2019/8/25 loren.jia
脚本逻辑:
    使用logging模块，设置logging，创建一个FileHandler，并对输出消息的格式进行设置，
    将其添加到logger，然后将日志写入到指定的文件中。同时信息队列话
脚本统计:
    ClassFoo: LogTools
    functionBar(): set_project -> 设置压力项目名称
            log_put -> log日志输出与信息传递
            at_log_put -> AT LOG的日志输出与信息传递
            abnormal_log_put -> 异常log日志输出与信息传递
            log -> log日志输出
            at_log -> at log日志输出
            result_log -> result log日志输出
测试前准备:
    无
-------------------------------------------------------------------------------
'''

import collections
import os
import logging
import logging.handlers
import re
import sys
import time
import wrapper_library_ec100y.common_log_queue_dict as common_log_queue_dict
import wrapper_library_ec100y.common_function as common_function
#import wrapper_library_ec100y.rabbitmq_producer as rabbitmq_producer
import datetime
testitem = None
print = common_function.my_print
sf = True

class LogTools(object):
    """
        定义一些私有变量，使用@classmethod装饰这些私有变量

        Attributes:
        __now：当前时间
        __log：log日志 默认为空
        __at_log：at log日志 默认为空
        __result_log：result log日志 默认为空

        set_project -> 设置压力项目名称
        log_put -> log日志输出与信息传递
        at_log_put -> AT LOG的日志输出与信息传递
        abnormal_log_put -> 异常log日志输出与信息传递
        log -> log日志输出
        at_log -> at log日志输出
        result_log -> result log日志输出
    """

    __now = common_function.time_format()
    __log = None
    __log_file = ''
    __at_log = None
    __at_log_file = ''
    __abnormal_log = None
    __abnormal_log_file = ''
    __LTE_A_debug_log = None
    __LTE_A_debug_log_file = ''
    __result_log = None
    __result_log_file = ''
    __project = None
    __isinstance = None

    def __new__(cls, *args, **kwargs):
        if cls.__isinstance is None:
            cls.__isinstance = object.__new__(cls)
            return cls.__isinstance
        else:
            return cls.__isinstance
        
    def __init__(cls):
       pass
    @classmethod
    def get_logger(cls,project,logger_name,now,log_file='log',level=logging.DEBUG,debug=True):
        '''
            设置logging，创建一个FileHandler，并对输出消息的格式进行设置，
            将其添加到logger
            %(name)s  Logger的名字
            %(levelno)s  数字形式的日志级别
            %(levelname)s  文本形式的日志级别
            %(pathname)s  调用日志输出函数的模块的完整路径名，可能没有
            %(filename)s  调用日志输出函数的模块的文件名
            %(module)s   调用日志输出函数的模块名
            %(funcName)s  调用日志输出函数的函数名
            %(lineno)d   调用日志输出函数的语句所在的代码行
            %(created)f  当前时间，用UNIX标准的表示时间的浮 点数表示
            %(relativeCreated)d  输出日志信息时的，自Logger创建以 来的毫秒数
            %(asctime)s  字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
            %(thread)d  线程ID。可能没有
            %(threadName)s  线程名。可能没有
            %(process)d  进程ID。可能没有
            %(message)s  用户输出的消息
        :param project: str类型，压力测试项
        :param logger_name:str类型，logger名称
        :param log_file: str类型，all log的log名称，默认为log
        :param level: object类型，log日志的配置等级，默认DEBUG
        :return: logger
        '''

        base_dir = os.getcwd()
        log_path = base_dir+"\\debuglog\\"

        folder = os.path.exists(log_path)

        if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
            os.makedirs(log_path)  # makedirs 创建文件时如果路径不存在会创建这个路径
        else:
            pass

        formatter = logging.Formatter('[%(asctime)s] %(message)s')
        logger = logging.getLogger(logger_name)
        logger.setLevel(level)

        filename = '%s_%s_%s.log'%(log_path +project,log_file,str(now))
        streamHandler = logging.StreamHandler()
        FileHandler = logging.handlers.RotatingFileHandler(filename,
                                                           maxBytes=1024 * 1024 * 20,
                                                           backupCount=10,
                                                           encoding="utf-8",
                                                           mode="w")
        streamHandler.setFormatter(formatter)
        FileHandler.setFormatter(formatter)
        logger.propagate = False
        if logger.handlers:

            logger.handlers = []
            logger.removeHandler(logger.handlers)

        if debug:
            logger.addHandler(streamHandler)
        logger.addHandler(FileHandler)
        return logger,filename

    @classmethod
    def get_atlogger(cls,
                     project,
                     logger_name,
                     now,
                     level=logging.DEBUG):
        '''
        设置logging，创建一个FileHandler，并对输出消息的格式进行设置，
        :param project: str类型，压力测试项
        :param logger_name:str类型，logger名称
        :param log_file: str类型，all log的log名称，默认为log
        :param level: object类型，log日志的配置等级，默认DEBUG
        :return: logger
        '''
        setting = common_log_queue_dict.DictObject().setting()

        try:
            if setting[testitem]['LogPath'] == "" :


                base_dir = os.getcwd()
                log_path = base_dir + "\\log\\log_" + project + "\\"
                folder = os.path.exists(log_path)
                if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
                    os.makedirs(log_path)  # makedirs 创建文件时如果路径不存在会创建这个路径
                else:
                    pass
            else:
                path = setting[testitem]['LogPath']
                log_path = path + "\\log_" + project + "\\"
                folder = os.path.exists(log_path)
                if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
                    os.makedirs(log_path)  # makedirs 创建文件时如果路径不存在会创建这个路径
                else:
                    pass


        except:
            base_dir = os.getcwd()
            log_path = base_dir +"\\log\\log_"+project+"\\"
            folder = os.path.exists(log_path)
            if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
                os.makedirs(log_path)  # makedirs 创建文件时如果路径不存在会创建这个路径
            else:
                pass
        formatter = logging.Formatter('[%(asctime)s]%(message)s')
        logger = logging.getLogger(logger_name)
        logger.setLevel(level)
        filename = '%s_%s.log'%(log_path+logger_name,str(now))
        FileHandler = logging.handlers.RotatingFileHandler(filename,
                                                           maxBytes=20 * 1024 * 1024,
                                                           backupCount=10,
                                                           encoding="utf-8",
                                                           mode='w')
        FileHandler.setFormatter(formatter)
        logger.propagate = False
        # streamHandler.setFormatter(formatter)
        if logger.handlers:
            # print(logger.handlers)
            logger.handlers = []
            logger.removeHandler(logger.handlers)
            # print(logger.handlers)
        logger.addHandler(FileHandler)
        # logger.addHandler(streamHandler)
        return logger , filename

   
    @classmethod
    def project(cls):
        """
        暂无介绍
        :return: 无
        """
        pass

    @classmethod
    def log(cls):
        """
        log日志写入方法
        :return: logger
        """
        now = common_function.time_format()
        try:
            if int(os.path.getsize(cls.__log_file)) > 10240000*5:
                cls.__log, cls.__log_file = cls.get_logger(cls.__project,
                                                           "log",
                                                           now)
                #rabbitmq_producer.log_path.append(cls.__log_file)
        except:
            pass
        return cls.__log

    @classmethod
    def LTE_A_debug_log(cls):
        """
        LTE_A_debug log日志写入方法
        :return: logger
        """
        now = common_function.time_format()
        if int(os.path.getsize(cls.__LTE_A_debug_log_file)) > 1024000 * 20:
            log_name = 'LTE_A_debug_log'
            cls.__LTE_A_debug_log, cls.__LTE_A_debug_log_file = cls.get_atlogger(cls.__project,
                                                               log_name,
                                                               now)
            #rabbitmq_producer.log_path.append(cls.__LTE_A_debug_log_file)
        return cls.__LTE_A_debug_log

    @classmethod
    def at_log(cls):
        """
        at log日志写入方法
        :return: logger
        """
        now = common_function.time_format()
        if int(os.path.getsize(cls.__at_log_file)) > 1024000*5:
            try:
                par = common_log_queue_dict.DictObject().parameter()
                runtimes = par['Runtimes']
                log_name = f'at_log(Runtimes~{runtimes})'
            except:
                log_name = 'at_log'


            cls.__at_log, cls.__at_log_file = cls.get_atlogger(cls.__project,
                                                               log_name,
                                                               now)
            #rabbitmq_producer.log_path.append(cls.__at_log_file)
        return cls.__at_log

    @classmethod
    def abnormal_log(cls):
        """
        at log日志写入方法
        :return: logger
        """
        now = common_function.time_format()
        if int(os.path.getsize(cls.__abnormal_log_file)) > 1024000*5:
            a,b= cls.get_atlogger(cls.__project, "abnormal_log",now)
            cls.__abnormal_log, cls.__abnormal_log_file = a,b
            #rabbitmq_producer.log_path.append(cls.__abnormal_log_file)
        return cls.__abnormal_log

    @classmethod
    def result_log(cls):
        """
        result log 日志写入方法
        :return: logger
        """
        now = common_function.time_format()
        if int(os.path.getsize(cls.__result_log_file)) > 1024000*5:
            a,b= cls.get_atlogger(cls.__project, "result_log", now)
            cls.__result_log, cls.__result_log_file = a,b
            #rabbitmq_producer.log_path.append(cls.__result_log_file)
        return cls.__result_log

    @classmethod
    def set_project(cls, value,debug=True):
        """
        logger初始化

        :param value: str类型，与log日志命名的一部分
        :return: 无
        """
        setting = common_log_queue_dict.DictObject().setting()
        try:
            mdm = setting['module']['MDM']
        except Exception:
            mdm = "LTE_A"
        cls.__project = value
        now = common_function.time_format()
        if not sf:
            debug = False
        cls.__log,cls.__log_file = cls.get_logger(value,"log",now,debug=debug)
        cls.__at_log,cls.__at_log_file = cls.get_atlogger(value,
                                                          "at_log",
                                                          now)
        cls.__abnormal_log,cls.__abnormal_log_file = cls.get_atlogger(value,
                                                                      "abnormal_log",
                                                                      now)
        cls.__result_log,cls.__result_log_file = cls.get_atlogger(value,
                                                                  "result_log",
                                                                  now)
        if mdm == 'LTE_A':
            cls.__LTE_A_debug_log, cls.__LTE_A_debug_log_file = cls.get_atlogger(value,
                                                           "LTE_A_debug_log",
                                                           now)
        #rabbitmq_producer.log_path.append(cls.__log_file)
        #rabbitmq_producer.log_path.append(cls.__at_log_file)
        #rabbitmq_producer.log_path.append(cls.__abnormal_log_file)
        #rabbitmq_producer.log_path.append(cls.__result_log_file)
        #rabbitmq_producer.log_path.append(cls.__LTE_A_debug_log_file)
        return

    @classmethod
    def log_put(cls,_str,mde=True):
        """
        log 日志 写入和 log信息的序列化
        :param str:  str类型，需要写入的log数据
        :return: 无
        """

        try:
            setting = common_log_queue_dict.DictObject().setting()
            fail_txt = setting['module']['fail_stop_txt']
            if fail_txt == "":
                pass
            else:
                if re.search(fail_txt, _str):
                    log_msg = common_log_queue_dict.SignalObject().log_msg()
                    log_msg.put('复现问题脚本暂停')
                    time.sleep(8)
                    while True:
                        time.sleep(2)
                        DICT = common_log_queue_dict.DictObject()
                        if DICT.setting()['module']['STOP'] == 0:
                            break
        except:
            pass

        if mde:
            cls.log().debug(_str)

        else:
            pass
        return

    @classmethod
    def LTE_A_debug_log_put(cls, _str):
        """
        异常 log 日志 写入和异常 log信息的序列化
        :param str: str类型，需要写入的异常 log 数据
        :return:
        """
        line = sys._getframe().f_back.f_lineno
        file_name = str(sys._getframe(1).f_code.co_filename)
        file_name = (file_name.rsplit("/")[-1]).rsplit('\\')[-1]
        try:
            setting = common_log_queue_dict.DictObject().setting()
            debug_able = setting['module']['debug_able']
        except Exception as e:
            # print(e)
            debug_able = True
        # runtimes = common_log_queue_dict.DictObject().parameter()['Runtimes']
        # _str1 = f'[log] [{file_name}:{line}] Runtimes:{runtimes}>>>{_str}'
        cls.log_put(_str)

        # if debug_able:
        #     _str1 = f'[log] [{file_name}:{line}] Runtimes:{runtimes}>>>{_str}'
        # else:
        #     _str1 = f'Runtimes:{runtimes}>>>{_str}'
        _str1 = f'[LTE-A_debuglog] {_str}'
        LTE_A_debug_log_msg = common_log_queue_dict.SignalObject.LTE_A_debug_log_msg()
        cls.LTE_A_debug_log().info(_str1)
        LTE_A_debug_log_msg.put(_str1)
        return

    @classmethod
    def at_log_put(cls,_str,mde=True):
        """
        at log 日志 写入和at log信息的序列化
        :param str:  str类型，需要写入的at log数据
        :return: 无
        """
        # if type(_str) == str:
        #     MySqlT.sqlQ.put(["atlog", f"[{str(datetime.datetime.now())[0:19]}] {_str}"])
        line = sys._getframe().f_back.f_lineno
        file_name = str(sys._getframe(1).f_code.co_filename)
        file_name = (file_name.rsplit("/")[-1]).rsplit('\\')[-1]
        try:
            setting = common_log_queue_dict.DictObject().setting()
            debug_able = setting['module']['debug_able']
        except Exception as e:
            # print(e)
            debug_able = True
        _str1 = f'[atlog] [{file_name}:{line}] {_str}'
        cls.log_put(_str1,mde)
        if debug_able:
            pass
        else:
            _str1 = f'{_str}'

        cls.at_log().info(_str1)

        return

    @classmethod
    def abnormal_log_put(cls,_str,mde=True):
        """
        异常 log 日志 写入和异常 log信息的序列化
        :param str: str类型，需要写入的异常 log 数据
        :return:
        """

        line = sys._getframe().f_back.f_lineno
        file_name = str(sys._getframe(1).f_code.co_filename)
        file_name = (file_name.rsplit("/")[-1]).rsplit('\\')[-1]
        try:
            setting = common_log_queue_dict.DictObject().setting()
            debug_able = setting['module']['debug_able']
        except Exception as e:
            # print(e)
            debug_able = True
        runtimes = common_log_queue_dict.DictObject().parameter()['Runtimes']
        _str1 = f'[log] [{file_name}:{line}] Runtimes:{runtimes}>>>{_str}'
        cls.log_put(_str1, mde)

        if debug_able:
            _str1 = f'[log] [{file_name}:{line}] Runtimes:{runtimes}>>>{_str}'
        else:
            _str1 = f'Runtimes:{runtimes}>>>{_str}'
        abnormal_log_msg = common_log_queue_dict.SignalObject.abnormal_log_msg()
        cls.abnormal_log().error(_str1)
        cls.at_log().error(_str1)
        sys.stdout.write("\r"+_str1+"\n")
        abnormal_log_msg.put(_str1)
        return

    @classmethod
    def result_log_put(cls,_dict,mde=True):
        """
        根据传入字典的key与value，写入result log中
        :param _dict: dict类型
        :return: None
        """
        flag = 0
        data_hander = ""
        if int(os.path.getsize(cls.__result_log_file)) > 1024000*5:
            flag = 1
        if flag == 1:
            for i in _dict.keys():
                data_hander += (str('\t' + str(i).center(20, ' ')))
            cls.result_log().info(data_hander)
            # MySqlT.sqlQ.put(["resultlog", f"[{str(datetime.datetime.now())[0:19]}] {data_hander}"])
        line = sys._getframe().f_back.f_lineno
        file_name = str(sys._getframe(1).f_code.co_filename)
        file_name = (file_name.rsplit("/")[-1]).rsplit('\\')[-1]
        if type(_dict) == dict:
            list_1 = []
            data_format = ""
            for i in _dict.values():
                list_1.append(i)
                data_format += (str('\t' + str(i).center(20, ' ')))
            # log_msg = common_log_queue_dict.SignalObject.log_msg()
            cls.result_log().info(data_format)

            try:
                setting = common_log_queue_dict.DictObject().setting()
                debug_able = setting['module']['debug_able']
            except:
                debug_able = True

            _str1 = f'[log] [{file_name}:{line}] {data_format}'
            cls.log_put(_str1, mde)
            if debug_able:
                _str1 = f'[log] [{file_name}:{line}] {data_format}'

            else:
                _str1 = f'{data_format}'
            # cls.at_log().info(_str1)

            data_chat_list = common_log_queue_dict.DictObject().data_chart()

            key = _dict['Runtimes']
            data_chat_list[key] = list_1
            print(common_log_queue_dict.DictObject().data_chart())

        else:
            cls.log().error("传入参数类型错误，期望是一个有序的字典类型")
        return







