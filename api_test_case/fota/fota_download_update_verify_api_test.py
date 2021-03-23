'''
@Author: Pawn
@Date: 2020-07-28
@LastEditTime: 2020-07-28
@Description: example for module Fota
@FilePath: example_fota.py
'''


import fota
from misc import Power
import utime
import uos

delta_bin = ''  # 差分包名称

def run():
    fota_obj = fota()  # 创建Fota对象
    file_size = uos.stat(delta_bin)[6]  # 获取文件总字节数
    with open('/usr'+delta_bin, "rb")as f:   # rb模式打开.bin文件
        while 1:
            c = f.read(1024)   # read
            if not c:
                break
            fota_obj.write(c, file_size)  # 写入.bin文件数据

    print("flush start...")
    print("flush verify...")
    res = fota_obj.verify()  # 校验
    print("flush verify...2")
    if res != 0:
        print("verify error")
        return
    # print("flush power_reset...")
    # utime.sleep(2)
    # Power.powerRestart()   # 重启模块


if __name__ == '__main__':
    print("run start...")
    run()
