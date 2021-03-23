#!/usr/bin/env python 
# -*- coding: utf-8 -*-
'''
-------------------------------------------------------------------------------
脚本名称: off_the_card_processing
需求来源:  
	无
测试目的：
	针对测试过程中掉卡的处理
修改记录:       
 初始版本V1.0 2019/12/6 loren.jia
脚本逻辑:    
    cfun0/1切换后查询
脚本统计: 
       
测试前准备:   
     
#-------------------------------------------------------------------------------
'''
import datetime
import re
import time
import serial
import wrapper_library_ec100y.common_function as common_function
import wrapper_library_ec100y.common_log as common_log
import wrapper_library_ec100y.common_log_queue_dict as common_log_queue_dict
import wrapper_library_ec100y.exception_handling as exception_handling
import wrapper_library_ec100y.port_work as p_w


def cmd_at(at_port_opened,command,at_result,timeout=5):
	"""
		串口的写与读
		:param command: str类型，写入的AT命令。
		:param timeout: int类型，设置超时时间，超时退出。
		:param at_port_open: object类型，是一个已经打开的串口对象，对该串口进行读写
		:param at_result: str类型，期望AT命令的结果，匹配退出。
		:return: dict类型，re_data_dict，记录串口读取的数据内容一些必要参数
	"""
	
	LOG = common_log.LogTools()
	LOG.at_log_put('[send]%s' % command)
	at_command = (command + "\r\n").encode("utf-8")
	p_w.at_write(at_port_opened,at_command)
	at_start_time = datetime.datetime.now()
	_data_buffer = ''
	_log = ''
	i = 0
	time_flag = 0
	re_data_dict = {}
	while 1:
		at_port_data = p_w.at_read(at_port_opened,size=1024)
		at_end_time = datetime.datetime.now()
		at_time = common_function.duration(at_start_time, at_end_time)
		
		if at_time - time_flag > 1:
			common_log.LogTools().log().error(f'等待{at_time}秒，无回应')
			time_flag = at_time
		if at_time > int(timeout):
			if len(_log) == 0:
				i += 1
				p_w.at_write(at_port_opened,b'+++')
				time.sleep(1)
				p_w.at_write(at_port_opened,at_command)
				LOG.at_log_put('[send]%s' % command)
				if i > 5:
					while True:
						i += 1
						p_w.at_write(at_port_opened,b"AT\r\n")
						LOG.at_log_put('[send]AT')
						at_port_data = p_w.at_read(at_port_opened,size=1024)
						if len(at_port_data) == 0:
							time.sleep(2)
							if i > 20:
								data = str('模块异常,AT不通，保留现场')
								LOG.abnormal_log_put(data)
								re_data_dict['result'] = False
								re_data_dict['re_data'] = _log
								while True:
									time.sleep(2)
									DICT = common_log_queue_dict.DictObject()
									if DICT.setting()['module']['STOP'] == 0:
										return re_data_dict
						else:
							break
			else:
				# self.log.write_at_log(at_log1)
				re_data_dict['result'] = False
				re_data_dict['re_data'] = _log
				return re_data_dict
		
		at_data_replace = _data_buffer + \
		                  str(at_port_data).replace('b\'', '') \
			                  .replace('\'', '')
		_log += at_data_replace
		at_result_temp = at_data_replace.split(r'\r\n')
		_data = at_result_temp[:-1]
		_data_buffer = at_result_temp[-1]
		if _data:
			result = 0
			for a in _data:
				a = a.replace('\\r', '')
				LOG.at_log_put('[recv]%s' % a)
				c_list = a
				if re.search('RDY', c_list):
						notes = '模块异常重启一次'
						LOG.abnormal_log_put(notes)
				if re.search(at_result, c_list):
						# 匹配到指定的response后结束循环
						result = 1
						re_data_dict['result'] = True
				elif re.search('ERROR', c_list):
						result = 2
						re_data_dict['result'] = False
						LOG.abnormal_log_put("%s 执行返回 %s"% (command, c_list))
				
			if result != 0:
					re_data_dict['re_data'] = _log
					return re_data_dict
					
def cfun(port):
	'''
	CFUN 切换找卡
	:param port: AT执行口
	:return: True/False
	'''
	LOG = common_log.LogTools()
	for i in range(0,3):
		LOG.at_log_put('[send] AT+CFUN=0')
		cmd_at(port, 'AT+CFUN=0', 'OK', timeout=5)
		time.sleep(2)
		LOG.at_log_put('[send] AT+CFUN=1')
		cmd_at(port, 'AT+CFUN=1', 'OK', timeout=5)
		time.sleep(5)
		LOG.at_log_put('[send] AT+CPIN?')
		result = cmd_at(port, 'AT+CPIN?', 'OK', timeout=5)
		if result['result']:
			LOG.at_log_put('CFUN 切换后SIM卡加载正常')
			return True
		time.sleep(2)
	else:
		LOG.at_log_put('连续3次 CFUN 切换后SIM卡加载依旧失败')
		return False
	
if __name__ == "__main__":
	common_log.LogTools().set_project('TTTT')
	port = serial.Serial('COM16',115200,timeout=0.1)
	l = cfun(port)
	print(l)