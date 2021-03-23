'''
@Author: Randy
@Date: 2020-11-27
@LastEditTime: 2020-11-27
@Description: API stress for log
@FilePath: log_debug_info_warning_error_critical_stress.py
'''

import log
import utime

interval = 7200 #运行持续时长

runtimes = 0
print('[start] log_debug_info_warning_error_critical_stress:;')
start_time = utime.time()
log_list = [log.CRITICAL, log.ERROR, log.WARNING, log.INFO,log.DEBUG,log.NOTSET] #CRITICAL>ERROR>WARNING>INFO>DEBUG>NOTSET

log_obj = log.getLogger("test")
while 1:
    duration = utime.time()-start_time
    if duration > interval:
        print('[end] log_debug_info_warning_error_critical_stress,runtimes:%s;'%runtimes)
        runtimes = 0
        break
    try:
        for i in log_list:
            log.basicConfig(i)
            log_obj.debug("Test message: %d(%s)", 100, "foobar")
            log_obj.info("Test message2: %d(%s)", 100, "foobar")
            log_obj.warning("Test message3: %d(%s)", 100, "foobar")
            log_obj.error("Test message3: %d(%s)", 100, "foobar")
            log_obj.critical("Test message3: %d(%s)", 100, "foobar")
    except Exception as e:
        print('runtimes:%s,log_debug_info_warning_error_critical_stress::[error]%s||result_api:: False;'% (runtimes,e))
    if duration%600 == 0:
        print('keep running... current duration: %sH current runtime:%s;'%(duration/3600,runtimes))
        utime.sleep(1)
    runtimes += 1