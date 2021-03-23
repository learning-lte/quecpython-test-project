#!/usr/bin/env python 
# -*- coding: utf-8 -*-
'''
-------------------------------------------------------------------------------
脚本名称:  common_log_queue_dict
需求来源:
    主要定义一些公用的信息队列对象与数据字典对象
测试目的：
    定义一些公用的信息队列对象与数据字典对象
修改记录:
    初始版本V1.0 2019/8/23 loren.jia
脚本逻辑:
    队列对象(SignalObject)：主要用来传递消息
    字典对象(DictObject)：主要用来存储一些关键的参数
    ClassFoo: SignalObject，DictObject
    functionBar(): None
脚本统计:
    无
测试前准备:
    无
-------------------------------------------------------------------------------
'''

import collections
import queue

class SignalObject(object):
    """
        定义一些私有变量队列object，使用@classmethod装饰这些私有变量
        
        __q: log日志信息队列  -> 使用S.q()调用
        __p: 运行次数信息队列 -> 使用S.p()调用
        __abnormal: 异常信息队列 -> 使用S.abnormal()调用
        __data_log_msg：数据信息队列 -> 使用S.data_log_msg()调用
        __at_log_msg：at log 日志信息队列 -> 使用S.at_log_msg()调用
    """
    __log_msg = queue.Queue()
    __p = queue.Queue()
    __abnormal_log_msg = queue.Queue()
    __LTE_A_debug_log_msg = queue.Queue()
    __data_log_msg = queue.Queue()
    __at_log_msg = queue.Queue(maxsize=0)
    __isinstance = None
    
    def __new__(cls, *args, **kwargs):
        if cls.__isinstance is None:
            cls.__isinstance = object.__new__(cls)
            return cls.__isinstance
        else:
            return cls.__isinstance
    
    @classmethod
    def log_msg(cls):
        """
        序列 log_msg
        :return: queue
        """
        return cls.__log_msg
    
    @classmethod
    def p(cls):
        """
        序列 p
        :return: queue
        """
        return cls.__p
    
    @classmethod
    def abnormal_log_msg(cls):
        """
        序列 abnormal_log_msg
        :return: queue
        """
        return cls.__abnormal_log_msg

    @classmethod
    def LTE_A_debug_log_msg(cls):
        """
        序列 LTE_A_debug_log_msg
        :return: queue
        """
        return cls.__LTE_A_debug_log_msg

    @classmethod
    def data_log_msg(cls):
        """
        序列 data_log_msg
        :return: queue
        """
        return cls.__data_log_msg
    
    @classmethod
    def at_log_msg(cls):
        """
        序列 at_log_msg
        :return: queue
        """
        return cls.__at_log_msg
    
    
        
class DictObject(object):
    """
        定义一些私有变量数据字典，使用@classmethod装饰这些私有变量
        
        __info：重要参数存储字典 -> 使用S.info()调用
        __parameter：result log数据存储有序字典 -> 使用S.parameter()调用
        __statistics: result log 数据统计存储字典 -> 使用 S.statistics()调用
    """
    
    __info = {}
    __parameter = {}
    __statistics = {}
    __setting = {}
    __data_chart_list = {}
    __memory_dict = {}
    __isinstance = None
    
    def __new__(cls, *args, **kwargs):
        if cls.__isinstance is None:
            cls.__isinstance = object.__new__(cls)
            return cls.__isinstance
        else:
            return cls.__isinstance
    
    @classmethod
    def info(cls):
        """
        字典 info
        :return: info{}
        """
        return cls.__info
    
    @classmethod
    def parameter(cls):
        """
        自定 parameter
        :return: parameter{}
        """
        return cls.__parameter
    
    @classmethod
    def statistics(cls):
        """
        自定 parameter
        :return: parameter{}
        """
        return cls.__statistics
    
    @classmethod
    def setting(cls):
            """
            自定 parameter
            :return: parameter{}
            """
            return cls.__setting
    
    @classmethod
    def data_chart(cls):
            """
            自定 data_chart_list
            :return: data_chart_list[]
            """
            return cls.__data_chart_list
    
    @classmethod
    def memory_dict(cls):
        """
        自定 data_chart_list
        :return: data_chart_list[]
        """
        return cls.__memory_dict
