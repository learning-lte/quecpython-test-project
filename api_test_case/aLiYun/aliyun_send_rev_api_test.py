# coding: utf-8
"""
@Author: Trent
@Date: 2020-10-13
@LastEditTime: 2020-10-13
@Description: api test for module aLiYun
@FilePath: aliyun_send_rev_stress.py
"""
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
keepAlive = 60


# 回调函数
def sub_cb(topic, msg):
    """
    消息回调
    :param topic:
    :param msg:
    :return:
    """
    print("subscribe recv:;")
    #print(topic, msg)


def api_test(api):
    """
    模块连接阿里云
    :param sub_cb:
    :return:
    """
    result1 = 'error'
    try:
        result1 = eval(api)
    except Exception as err:
        print('[error]' + str(err)+';')
    if result1 != 'error':
        result2 = True
    else:
        result2 = False
    print('%s:: %s||result_api:: %s;' % (api, result1, result2))
    utime.sleep(0.05)


if __name__ == '__main__':
    ali = aLiYun(productKey, productSecret, DeviceName, DeviceSecret)  # 创建aliyun连接对象
    for a in range(2):
        if a == 0:
            clean_session = True
            print('clean_session = Ture;')
        else:
            clean_session = False
            print('clean_session = Fales;')
        ali.setMqtt(clientID, clean_session=clean_session, keepAlive=keepAlive)  # 设置mqtt连接属性
        ali.setCallback(sub_cb)
        list = [
            'ali.subscribe(topic)',
            'ali.publish(topic, msg)',
        ]
        for i in list:
            api_test(i)
    try:
        ali.start()
        utime.sleep(1)
        print('aliYun.start::||result_api: Ture;')
        ali.disconnect()
        print('aliYun.close::||result_api: Ture;')
        utime.sleep(1)
    except Exception as e:
        print('aliYun.start::[error]%s||result_api:: False;'%e)
        try:
            ali.disconnect()
        except:
            pass
