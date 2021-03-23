#!/usr/bin/env python 
# -*- coding: utf-8 -*-
'''
-------------------------------------------------------------------------------
脚本名称:  exception_handling
需求来源:
	异常捕获
测试目的：
	:用来捕获异常问题点.
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

import sys
import traceback
import wrapper_library_ec100y.common_log as common_log

def my_error(printdebug=True):
	"""
	异常捕获
	:param printdebug: debug模式
	:return: res /func执行结果
	"""
	log = common_log.LogTools().log_put
	def inner1(f):
		def inner2(*args, **kwargs):
			try:
				res = f(*args,**kwargs)
			except Exception as err:
				if printdebug:
					info = sys.exc_info()[2].tb_frame.f_back
					temp = "\n{}\nERROR_filename:{}" \
					       "\nMian_lines:{}\n" \
					       "ERROR_funcation:{}\nError:{}\n详细：{}{}"
					log(temp.format(str('ERROR').center(108, '#'),
					                      info.f_code.co_filename,
					                      info.f_lineno, f.__name__,
					                      repr(err),
					                      traceback.format_exc(),
					                      str('#').center(108, '#')),True)
				else:
					temp = "\n{}\nERROR：{}{}"
					log(temp.format(str('ERROR').center(108, '#'),
					                      traceback.format_exc(),
					                      str('#').center(108, '#')),True)
				res = 0
			return res
		
		return inner2
	
	return inner1
