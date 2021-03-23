'''
@Author: Baron
@Date: 2020-06-17
@LastEditTime: 2020-06-17 17:06:08
@Description: example for module ntptime
@FilePath: example_ntptime.py
'''
import ntptime

# 设置ntp服务
ntptime.host='pool.ntp.org'

# 同步ntp服务时间
ntptime.settime()