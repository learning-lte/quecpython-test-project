'''
@Author: Randy
@Date: 2020-09-23
@LastEditTime: 2020-09-23
@Description: API test for log
@FilePath: log_debug_info_warning_error_critical_api_test.py
'''

import log
import utime

log_level = log.INFO  #CRITICAL>ERROR>WARNING>INFO>DEBUG>NOTSET

def api_test(api):
    result1 = 'error'
    try:
        result1 = eval(api)
    except Exception as err:
        print('[error]'+str(err)+';')
    if result1 != 'error':
        result2 = True
    else:
        result2 = False
    print('%s:: %s||result_api:: %s;'%(api,result1,result2))
    utime.sleep(1)

api_list = [
    'log.basicConfig(log.INFO)',
    'log_obj.debug("Test message: %d(%s)", 100, "foobar")',
    'log_obj.info("Test message2: %d(%s)", 100, "foobar")',
    'log_obj.warning("Test message3: %d(%s)")',
    'log_obj.error("Test message4")',
    'log_obj.critical("Test message5")',
            ]

log_obj = log.getLogger("test")
for i in api_list:
    api_test(i)