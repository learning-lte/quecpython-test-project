# coding: utf-8
"""
@Author: trent.zhang
@Date: 2020-10-12
@LastEditTime: 2020-10-12 20:24:08
@Description: example for module umqtt
@FilePath: mqtt_client_send_rev_api_test.py
"""
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

def sub_cb(topic, msg):
    """
    回调消息
    :param topic:
    :param msg:
    :return:
    """
    global state
    print("subscribe recv:")
    print(topic, msg)

    if data == msg:
        pass
    else:
        print(msg)
    state = 1


# client_id 连接到代理时使用的唯一客户端ID字符串。
# server 远程服务器的主机名或IP地址。
# \port**（可选）要连接的服务器主机的网络端口。 默认为1883，请注意，MQTT over SSL / TLS的默认端口是8883。
# \user**（可选）在服务器上注册的用户名。
# \password**（可选）在服务器上注册的密码。
# \keepalive**（可选）客户端的keepalive超时值。 默认为60秒。
# \ssl**（可选）是否使能 SSL/TLS 支持。
# \ssl_params**（可选）SSL/TLS 参数。
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
        for a in range(2):
            if a == 0:
                ssl = True
            else:
                ssl = False
            c = MQTTClient(client_id, server, port=port, user=user, password=password, keepalive=keepalive, ssl=ssl,
                           ssl_params={})
            for i in range(2):
                if i == 0:
                    retain = True
                else:
                    retain = False
            try:
                c.set_last_will(path, last_will, retain=retain, qos=0)  # retain = True boker会一直保留消息，默认False
                c.set_callback(sub_cb)
                print('MQTTClient,set_last_will,set_callback::pass||result_api:: Ture;')
            except Exception as e:
                print('MQTTClient,set_last_will,set_callback::[error]%s||result_api: False;'%e)
            list = [
                    'c.connect(clean_session=True)',
                    'c.subscribe(topic)',
                    'c.publish(topic, msg)'
                ]
            for i in list:
                api_test(i)
            while True:
                # 等待服务器直到服务器无待处理消息，该函数是阻塞函数
                c.wait_msg()
                if state == 1:
                    print('wait_msg::pass||result_api:: Ture;')
                    break
                else:
                    pass
            try:
                c.disconnect()
                print('disconnect::pass||result_api:: Ture;')
            except Exception as e:
                print('disconnect::%s||result_api:: False;'%e)
