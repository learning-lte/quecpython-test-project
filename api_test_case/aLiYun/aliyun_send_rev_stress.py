# coding: utf-8
"""
@Author: Trent
@Date: 2020-10-20
@LastEditTime: 2020-10-20
@Description: api test for module aLiYun
@FilePath: aLiYun_send_rev_stress.py
"""
'''
-------------------------------------------------------------------------------
脚本逻辑:
    1.aLiYun接口稳定性
    2.接口包含aLiYun&setMqtt,setCallback&subscribe&publish
    3.输出异常返回结果
脚本统计:
    1.接口函数调用崩溃log
测试前准备:
    无
-------------------------------------------------------------------------------
'''
from aLiYun import aLiYun
import utime

productKey = "Rie7JR259d6"     # 产品标识
# productSecret = "fnE27f4ijuSWi0Pz"  # 产品密钥（一机一密认证此参数传入None）
productSecret = None
DeviceName = "lte_test"     # 设备名称
DeviceSecret = "JAM0IQkcj0Fk2ytuGkJq5HFnWHNj3MAW"   # 设备密钥（一型一密认证此参数传入None）
# DeviceSecret = None   # 设备密钥（一型一密认证此参数传入None）
msg = "hell world"
clientID = "12345"  # 自定义字符（不超过64）
topic = "/Rie7JR259d6/lte_test/update"  # 主题
interval = 60  # 运行时长
start_time = utime.time()
keepAlive = 60


# 回调函数
def sub_cb(topic, msg):
    """
    消息回调
    :param topic:
    :param msg:
    :return:
    """
    print("subscribe recv:")
    print(topic, msg)


def api_stress():
    print('aLiYun_api_stress for 2H: aLiYun&setMqtt')
    m = 1
    start_time = utime.time()
    while 1:
        print('Runtimes: %s' % m)
        duration = utime.time() - start_time
        if duration > interval:
            break
        if duration % 100 == 0:
            print('keep running... current duration: %s,runtimes: %s' % (duration, m))
        try:
            ali = aLiYun(productKey, productSecret, DeviceName, DeviceSecret)  # 创建aliyun连接对象
            ali.setMqtt(clientID, clean_session=False, keepAlive=keepAlive)  # 设置mqtt连接属性
            utime.sleep(1)
            ali.setMqtt(clientID, clean_session=True, keepAlive=keepAlive)
            utime.sleep(1)
            ali.disconnect()
        except Exception as e:
            try:
                ali.disconnect()
            except:
                pass
            print('aLiYun&setMqtt[%s]: %s,result_api: False;' % (m, e))
        utime.sleep(1)
        m += 1

    print('aLiYun_api_stress for 2H: setCallback&subscribe&publish')
    m = 1
    start_time = utime.time()
    while 1:
        print('Runtimes: %s'%m)
        ali.setMqtt(clientID, clean_session=True, keepAlive=keepAlive)
        duration = utime.time() - start_time
        if duration > interval:
            break
        if duration % 100 == 0:
            print('keep running... current duration: %s,runtimes: %s' % (duration, m))
        try:
            ali.setCallback(sub_cb)
            utime.sleep(1)
            ali.subscribe(topic)
            utime.sleep(1)
            ali.publish(topic, msg)
            utime.sleep(1)
        except Exception as e:
            print('setCallback&subscribe&publish[%s]: %s,result_api: False;' % (m, e))
        try:
            ali.start()
            utime.sleep(1)
            print('setCallback,start，result_api: Ture;')
        except Exception as e:
            print('start[%s]: %s,result_api: False;' % (m, e))
        try:
            ali.disconnect()
        except:
            pass
        utime.sleep(1)
        m += 1

if __name__ == '__main__':
    api_stress()
