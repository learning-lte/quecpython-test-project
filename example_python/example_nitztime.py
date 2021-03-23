'''
@Author: Baron
@Date: 2020-06-17
@LastEditTime: 2020-06-17 17:06:08
@Description: example for module ntptime
@FilePath: example_ntptime.py
'''
import net

# 获取当前基站时间
i = net.nitzTime()
print(i)
print('test done')