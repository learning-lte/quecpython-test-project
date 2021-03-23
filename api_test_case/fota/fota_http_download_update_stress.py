'''
@Author: Randy
@Date: 2020-11-14
@LastEditTime: 2020-11-14
@Description: example for module Fota
@FilePath: fota_http_download_update_stress.py
'''


import fota
import request
from misc import Power
import modem
import uos
import utime
utime.sleep(10)
url = 'http://quec-pro-oss.oss-cn-shanghai.aliyuncs.com/fota/214/fbf_dfota.bin'  # 固件包下载地址


response = request.get(url)  # 获取固件包文件
print(response)
for i in range(30):
    print('############wait 30s############')
    utime.sleep(1)
utime.sleep(30)
with open('/usr/fota.bin','wb') as f:   # 生成固件包文件
    f.write(response.content)

fota_obj = fota() #创建fota对象
with open('/usr/fota.bin', 'rb') as f: # 读取固件包数据
    while 1:
        c = f.read(1024)  # read
        if not c:
            break
        fota_obj.write(c)  # 写入.bin文件数据
fota_obj.flush() # 读取缓存数据
res = fota_obj.verify() # 固件包校验
print(res)
if not res:
    print('fota update end')
    uos.remove('fota.bin')  # 删除固件包，释放存储空间（此步可不执行）
    utime.sleep(2)
    print("flush power_reset...")
    # Power.powerRestart()  # 重启模块
