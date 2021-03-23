# coding: utf-8
"""
@Author: trent.zhang
@Date: 2020-10-12
@LastEditTime: 2020-10-12 20:24:08
@Description: example for module umqtt
@FilePath: mqtt_client_send_rev_stress.py
"""
'''
-------------------------------------------------------------------------------
脚本逻辑:
    1.aLiYun接口稳定性
    2.接口包含MQTTClient, connect&disconnect,connect&subscribe&publish&disconnect,set_callback&subscribe&publish&wait_msg
    3.输出异常返回结果
脚本统计:
    1.接口函数调用崩溃log
测试前准备:
    无
-------------------------------------------------------------------------------
'''
from umqtt import MQTTClient
import utime
client_id = '12345|securemode=3,signmethod=hmacsha1,timestamp=399|'
server = "Rie7JR259d6.iot-as-mqtt.cn-shanghai.aliyuncs.com"
port = '1883'
user = 'lte_test&Rie7JR259d6'
password = 'b51165935b48d1e620a6912f5738ee8761ef16ba'
state = 0
keepalive = 60
ssl_params = """
                -----BEGIN CERTIFICATE-----
                MIIDdTCCAl2gAwIBAgILBAAAAAABFUtaw5QwDQYJKoZIhvcNAQEFBQAwVzELMAkG
                A1UEBhMCQkUxGTAXBgNVBAoTEEdsb2JhbFNpZ24gbnYtc2ExEDAOBgNVBAsTB1Jv
                b3QgQ0ExGzAZBgNVBAMTEkdsb2JhbFNpZ24gUm9vdCBDQTAeFw05ODA5MDExMjAw
                MDBaFw0yODAxMjgxMjAwMDBaMFcxCzAJBgNVBAYTAkJFMRkwFwYDVQQKExBHbG9i
                YWxTaWduIG52LXNhMRAwDgYDVQQLEwdSb290IENBMRswGQYDVQQDExJHbG9iYWxT
                aWduIFJvb3QgQ0EwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDaDuaZ
                jc6j40+Kfvvxi4Mla+pIH/EqsLmVEQS98GPR4mdmzxzdzxtIK+6NiY6arymAZavp
                xy0Sy6scTHAHoT0KMM0VjU/43dSMUBUc71DuxC73/OlS8pF94G3VNTCOXkNz8kHp
                1Wrjsok6Vjk4bwY8iGlbKk3Fp1S4bInMm/k8yuX9ifUSPJJ4ltbcdG6TRGHRjcdG
                snUOhugZitVtbNV4FpWi6cgKOOvyJBNPc1STE4U6G7weNLWLBYy5d4ux2x8gkasJ
                U26Qzns3dLlwR5EiUWMWea6xrkEmCMgZK9FGqkjWZCrXgzT/LCrBbBlDSgeF59N8
                9iFo7+ryUp9/k5DPAgMBAAGjQjBAMA4GA1UdDwEB/wQEAwIBBjAPBgNVHRMBAf8E
                BTADAQH/MB0GA1UdDgQWBBRge2YaRQ2XyolQL30EzTSo//z9SzANBgkqhkiG9w0B
                AQUFAAOCAQEA1nPnfE920I2/7LqivjTFKDK1fPxsnCwrvQmeU79rXqoRSLblCKOz
                yj1hTdNGCbM+w6DjY1Ub8rrvrTnhQ7k4o+YviiY776BQVvnGCv04zcQLcFGUl5gE
                38NflNUVyRRBnMRddWQVDf9VMOyGj/8N7yy5Y0b2qvzfvGn9LhJIZJrglfCm7ymP
                AbEVtQwdpf5pLGkkeB6zpxxxYu7KyJesF12KwvhHhm4qxFYxldBniYUr+WymXUad
                DKqC5JlR3XC321Y9YeRq4VzW9v493kHMB65jUr9TU/Qr6cf9tveCX4XSQRjbgbME
                HMUfpIBvFSDJ3gyICh3WZlXi/EjJKSZp4A==
                -----END CERTIFICATE-----
                """
path = "/Rie7JR259d6/lte_test/update"
data = 'hello'
last_date = 'aliyun disconnect'
topic = "/Rie7JR259d6/lte_test/update"   # 主题
msg = "hell world"
last_will = 'aliyun disconnect'
interval = 7200   # 运行持续时长


def sub_cb(topic, msg):
    """
    回调消息
    :param topic:
    :param msg:
    :return:
    """
    global state
    print("subscribe recv;")

    if data == msg:
        pass
    else:
        print('subscribe recv:[diff]%s'%msg)
    state = 1


def api_stress():
    print('[start] mqtt_api_stress: MQTTClient;')
    start_time = utime.time()
    m = 1
    while 1:
        duration = utime.time() - start_time
        if duration > interval:
            print('[end] mqtt_api_stress: MQTTClient,runtimes: %s;' % m)
            break
        if duration % 100 == 0:
            print('keep running... current duration: %sH,runtimes: %s;' % (duration/3600, m))
        try:
            c = MQTTClient(client_id, server, port=port, user=user, password=password, keepalive=keepalive, ssl=False,
                               ssl_params={})
            c = MQTTClient(client_id, server, port=port, user=user, password=password, keepalive=keepalive, ssl=True,
                           ssl_params={})
            utime.sleep(1)
        except Exception as e:
            print('runtimes:%s,MQTTClient:: %s||result_api:: False;' % (m,e))
        m += 1

    print('[start] mqtt_api_stress: MQTTClient&connect&disconnect;')
    start_time = utime.time()
    m = 1
    while 1:
        duration = utime.time() - start_time
        if duration > interval:
            print('[end] mqtt_api_stress: MQTTClient&connect&disconnect,runtimes: %s;' % m)
            break
        if duration % 100 == 0:
            print('keep running... current duration: %sH,runtimes: %s;' % (duration/3600, m))
        try:
            c.connect(clean_session=True)
            c.disconnect()
            c.connect(clean_session=False)
            c.disconnect()
            utime.sleep(1)
        except Exception as e:
            c.disconnect()
            print('runtimes:%s,connect&disconnect:: %s||result_api:: False;' % (m,e))
        m += 1

    print('[start] mqtt_api_stress: connect&subscribe&publish&disconnect;')
    start_time = utime.time()
    m = 1
    while 1:
        duration = utime.time() - start_time
        if duration > interval:
            print('[end] mqtt_api_stress: connect&subscribe&publish&disconnect,runtimes: %s;' % m)
            break
        if duration % 100 == 0:
            print('keep running... current duration: %sH,runtimes: %s;' % (duration/3600, m))
        try:
            c.connect(clean_session=False)
            c.subscribe(topic)
            c.publish(topic, msg)
            c.disconnect()
            c.connect(clean_session=True)
            c.subscribe(topic)
            c.publish(topic, msg)
            c.disconnect()
        except Exception as e:
            print('runtimes:%s,connect&subscribe&publish&disconnect:: %s||result_api:: False;' % (m,e))
        m += 1

    print('[start] mqtt_api_stress: set_callback&subscribe&publish&wait_msg;')
    start_time = utime.time()
    c.connect(clean_session=True)
    m = 1
    while 1:
        duration = utime.time() - start_time
        if duration > interval:
            print('[end] mqtt_api_stress: set_callback&subscribe&publish&wait_msg,runtimes: %s;' % m)
            break
        if duration % 100 == 0:
            print('keep running... current duration: %sH,runtimes: %s;' % (duration/3600, m))
        try:
            c.set_callback(sub_cb)
            c.subscribe(topic)
            c.publish(topic, msg)
        except Exception as e:
            print('runtimes:%s,set_callback&subscribe&publish&wait_msg:: %s||result_api:: False;' % (m,e))
        while True:
            # 等待服务器直到服务器无待处理消息，该函数是阻塞函数
            c.wait_msg()
            if state == 1:
                break
            else:
                print('runtimes:%s,wait_msg:: %s||result_api:: False;'% (m,state))
        m += 1
    c.disconnect()


if __name__ == '__main__':
    api_stress()
