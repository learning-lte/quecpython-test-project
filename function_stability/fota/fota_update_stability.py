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
import modem
import dataCall
import request

# 参数配置区  # 运行时将文件名修改为main.py 开机即可自动运行
url_a_b = ''  # 差分包a_b的下载地址，url为空时不进行在线下载
url_b_a = ''  # 差分包b_a的下载地址，url为空时不进行在线下载
fw_a = ''  # 当前版本号，注意不带V
fw_b = ''  # 目标版本号，注意不带V
delta_bin_a_b = ''  # 差分包a_b名称
delta_bin_b_a = ''  # 差分包b_a名称


def run():
    fota_obj = fota()  # 创建Fota对象
    fw = modem.getDevFwVersion()
    if fw == fw_a:
        delta_bin = delta_bin_a_b
        if url_a_b != '' and url_b_a != '':
            url = url_a_b
    elif fw == fw_b:
        delta_bin = delta_bin_b_a
        if url_a_b != '' and url_b_a != '':
            url = url_b_a
    else:
        print("fw version is wrong,please check...")
        return
    if url_a_b != '' and url_b_a != '': # 判断是否需要在线下载
        response = request.get(url)  # 获取固件包文件
        with open(delta_bin, 'wb') as f:  # 生成固件包文件
            f.write(response.content)
        f.close()
        response.close()
    if delta_bin not in uos.listdir():
        print("delta_bin is not exist,please check...")
        return
    file_size = uos.stat(delta_bin)[6]  # 获取文件总字节数
    with open(delta_bin, "rb")as f:   # rb模式打开.bin文件
        while 1:
            c = f.read(1024)   # read
            if not c:
                break
            fota_obj.write(c,file_size)  # 写入.bin文件数据

    print("flush start...")
    print("flush verify...")
    res = fota_obj.verify()  # 校验
    print("flush verify...2")
    if res != 0:
        print("verify error")
        return
    print("flush power_reset...")
    utime.sleep(2)
    Power.powerRestart()   # 重启模块


if __name__ == '__main__':
    while 1:
        b = dataCall.getInfo(1, 0)
        if list(b)[2][0] == 1:
            break
        utime.sleep(1)
    utime.sleep(10)
    print("run start...")
    run()