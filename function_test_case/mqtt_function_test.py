"""
@Author: trent.zhang
@Date: 2020-12-16
@LastEditTime: 2020-12-18
@Description: example for module umqtt
@FilePath: mqtt_function_test.py
"""
from umqtt import MQTTClient  # 导入的功能模块
import sys
import dataCall
import net
import utime
from aLiYun import aLiYun
from TenCentYun import TXyun


class MQTTFunctionTest(object):

    def __init__(self):
        pass

    def MQTT_01_001(self):  # 待执行函数
        '''
        :return: 模块开机自动拨号注网
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                a = dataCall.getInfo(1, 0)
                info.append(a)
                b = net.csqQueryPoll()
                info.append(b)
                if a[2][0] == 1 or b != 99:
                    result = True
                else:
                    dataCall.start(1, 0, "3gnet.mnc001.mcc460.gprs", "", "", 0)
                    utime.sleep(2)
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info,result

    def MQTT_01_002(self):  # 待执行函数
        '''
        :return: 连接mqtt服务器
        '''
        runflag = 1
        if runflag:
            try:
                ip = "220.180.239.212"
                port = "8306"
                client_id = "TEST"
                path = 'Q1MQTT/sample/a'
                # --------------valid code--------------

                def sub_cb(topic, msg):
                    global state
                    # print("subscribe recv:")
                    global m
                    m = (topic, msg)
                    # print(info)
                    state = 1
                c = MQTTClient(client_id, ip, port)
                c.connect()
                c.set_callback(sub_cb)
                c.subscribe(path)
                c.publish(path, b"hello")

                while True:
                    c.wait_msg()
                    if state == 1:
                        c.disconnect()
                        info = m
                        result = True
                        break

                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def MQTT_02_001(self):  # 待执行函数
        '''
        :return: 无认证连接mqtt服务器
        '''
        runflag = 1
        if runflag:
            try:
                client_id = '12345|securemode=3,signmethod=hmacsha1,timestamp=707|'
                server = "Rie7JR259d6.iot-as-mqtt.cn-shanghai.aliyuncs.com"
                port = '1883'
                user = 'lte_test&Rie7JR259d6'
                password = '5b27fc4c011361964b922761953815e568172861'
                path = "/Rie7JR259d6/lte_test/update"  # MQTT服务器订阅地址
                keepalive = 60

                def sub_cb(topic, msg):
                    global state
                    global m
                    m = (topic, msg)
                    state = 1
                c = MQTTClient(client_id, server, port=port, user=user, password=password, keepalive=keepalive,
                               ssl=False, ssl_params={})
                c.connect()
                c.set_callback(sub_cb)
                c.subscribe(path)
                c.publish(path, b"hello")
                while True:
                    c.wait_msg()
                    if state == 1:
                        c.disconnect()
                        info = m
                        result = True
                        break
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def MQTT_03_001(self):  # 待执行函数
        '''
        :return: 与阿里云服务器建立SSL 单项认证连接
        '''
        runflag = 1
        if runflag:
            try:
                client_id = '12345|securemode=3,signmethod=hmacsha1,timestamp=707|'
                server = "Rie7JR259d6.iot-as-mqtt.cn-shanghai.aliyuncs.com"
                port = '1883'
                user = 'lte_test&Rie7JR259d6'
                password = '5b27fc4c011361964b922761953815e568172861'
                path = "/Rie7JR259d6/lte_test/update"  # MQTT服务器订阅地址
                keepalive = 60

                def sub_cb(topic, msg):
                    global state
                    global m
                    m = (topic, msg)
                    state = 1

                c = MQTTClient(client_id, server, port=port, user=user, password=password, keepalive=keepalive,
                               ssl=True, ssl_params={})
                c.connect()
                c.set_callback(sub_cb)
                c.subscribe(path)
                c.publish(path, b"hello")
                while True:
                    c.wait_msg()
                    if state == 1:
                        c.disconnect()
                        info = m
                        result = True
                        break
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def MQTT_04_001(self):  # 待执行函数
        '''
        :return: 与阿里云服务器建立SSL 双向认证连接
        '''
        runflag = 1
        if runflag:
            try:
                clientID = "GPS_Tracker"
                url = "a1ivzljzs9abgg-ats.iot.eu-central-1.amazonaws.com"  # "arn:aws:iot:eu-central-1:566412340147:thing/gps_tracker" # "broker.emqx.io"
                port = '8883'  # 1883 is without SSL
                certificate_content = """
                             -----BEGIN CERTIFICATE-----
                             MIIDWTCCAkGgAwIBAgIUTq9lhB6NaBXcIKpqd20rmVShMcMwDQYJKoZIhvcNAQEL
                             BQAwTTFLMEkGA1UECwxCQW1hem9uIFdlYiBTZXJ2aWNlcyBPPUFtYXpvbi5jb20g
                             SW5jLiBMPVNlYXR0bGUgU1Q9V2FzaGluZ3RvbiBDPVVTMB4XDTIwMTIwNDEwMDQw
                             N1oXDTQ5MTIzMTIzNTk1OVowHjEcMBoGA1UEAwwTQVdTIElvVCBDZXJ0aWZpY2F0
                             ZTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBANopX64+Y9eH1UcRBpu4
                             s1V9918VNHMXO+8U6WgfRp844/wX0VwH8urO6kpcGOaMXL0FHWlz/zng5y+YSdlY
                             4nC8O2Q+5kZrFUnbdGlj0PsLj4FvKoPcHEgDCF3/nBUf4dd6zEEIJWHFuasY68Gm
                             XZE+tSrAfb724Qk7e6pnL6oRlHzjsPSBQ26BXuO9bcAjDNHljfnUi3rVN6Ve3jfs
                             TqhuuAw1fO/9+/S3xxVuBPojh6fO8a1ez0oRkBLhkoucnSlTXXe1A8WPbJSyaXR9
                             ZCwbF5kPEjIuj3U9/ENhWwsfCeJjV9kyWbyLykI2tY/xpdpzzZVWpwIZRuevOPMI
                             wf8CAwEAAaNgMF4wHwYDVR0jBBgwFoAUhwr1pnkoTno7djgTER6bHlgqrLswHQYD
                             VR0OBBYEFPyxw3mbH1jLsHZcFRumceWyw4prMAwGA1UdEwEB/wQCMAAwDgYDVR0P
                             AQH/BAQDAgeAMA0GCSqGSIb3DQEBCwUAA4IBAQBTpYRUkpNtSUbwniZpF0/C7i/p
                             6Q6XC4eICDprP1E/AhNJiCEHtQT5AD//zkRpFITUePSEoKNh9bvhqijTy4Dmz+EZ
                             ysjN2dILjea51qqjhSR8S8JlU09/vcI6W3P3335Mmlk1oQXkDiYvtQEK/PrtLobp
                             fwcbyRvsR+oWE1cCAvo6gJywCp+BnNQpc1qSl8cvs26ju9FezRZFkJTcd24vQwDQ
                             gmMICssHt8FYWnVibQJiSHQ+iDxONJykHC9S7XtGpbDZRPlxd92vLurpxyb6jiUF
                             4qI2ZAFxOzI60RSfalghxIvQofMSQ6X3eFfwyA0fbcAisrySgueWMYplzz1Z
                             -----END CERTIFICATE-----
                             """
                private_content = """
                             -----BEGIN RSA PRIVATE KEY-----
                             MIIEpAIBAAKCAQEA2ilfrj5j14fVRxEGm7izVX33XxU0cxc77xTpaB9Gnzjj/BfR
                             XAfy6s7qSlwY5oxcvQUdaXP/OeDnL5hJ2VjicLw7ZD7mRmsVSdt0aWPQ+wuPgW8q
                             g9wcSAMIXf+cFR/h13rMQQglYcW5qxjrwaZdkT61KsB9vvbhCTt7qmcvqhGUfOOw
                             9IFDboFe471twCMM0eWN+dSLetU3pV7eN+xOqG64DDV87/379LfHFW4E+iOHp87x
                             rV7PShGQEuGSi5ydKVNdd7UDxY9slLJpdH1kLBsXmQ8SMi6PdT38Q2FbCx8J4mNX
                             2TJZvIvKQja1j/Gl2nPNlVanAhlG56848wjB/wIDAQABAoIBAQChDVwaKOrSCO/V
                             B+el++NAIL8GjYPr1uIi7IAmorgjAP+lcfvXgfK9j0T84iJryIEJ9YWx/LUVCEgD
                             JdyWvHxmFz+NELY0lAbiQEUfLFXxjqZBOkzbjRm/u6VopzOVkLTLu1agR6A5Hpuj
                             iME6c1Otzuo1hmcOG/kjNKtlr8lLNVOFPt+ZT13Owg3xZxRyjIdFy4G27/lUatsv
                             HOzBB4C/8WtkzR1qTXFWV7vzTSHTv5PNcHpeFnLVpIU2pC7swa1y6xHFsi/8Zcz4
                             fNibYc8ROks/OVzFvlO2/Qr/nKScQwmCz3GfSaFuTuYeMs08PG5wTWxeRNdoAWwl
                             Q+db8cuRAoGBAPx+b7w3G8AFK9+TVLGTifj3TDNhP6GvAdR2VoOnTFz30B0gh4vB
                             UO7QBV8jTqKYkjNoOWLPhFrJElgsGPq6aTmjPhW8fZo56lUdBc3APWAVytbw+eWx
                             +JtRbwDYg/Dcx4ZNjOq2yvRN5Lr2alco+5tvmEbjdItsmCrdAh/L8he5AoGBAN0w
                             5KV4KjfQQwAaTMFZ4Z4NHddEoDFm2E4hMfnhxs9jnoIU+cKvZ3+o1kTmrqrqVKUp
                             0cj5GXGLqZLXwQtq0iIKVPv0kyDvSYCFJEQUEuu8ewkoiCpEbx0Ptpw7xMWYN888
                             2SeDL7N9hPyRzZa5EuKuT+qDH2NuN5M4VbbAJRN3AoGAflxQUuNJcfmkkUlMU2pA
                             3GX2rqf2jlXlFoz6kvyAzO4AKvOCokBm3n0gkxI6Ykj0seFxBrBPzpdeJN48yg3M
                             Z1n40iv4t9xQF7RkmSmiDZoaXyNODNPaVPCWGthAf6Qd/mqFIVnFjCoHVEHJykDq
                             Wkmo7aEbTENWi+z7CSqpx5ECgYEAsipw8gwBzaVWYp3Ml63DeyDLmZswgbp6nyxD
                             6ih/kIuIoPUuXTAWaRDhTuyVYxyPg95UmdJ0OS6rL5nUaFLp4ft6itxtKok0Jm6Y
                             ULHur63JWQ4p6AnpinoeuGe4TwUWZzp3HEmiQazoUt1KwY5f9PE9dAOcY+XipBYr
                             jKHm+28CgYBGYm0a6Pps0L8Nov/l05qCYNpfry7zPmDOaUzyx13CyFAZ2dENJrbn
                             uN+JZFs9qlgxl0ovuUIFPGONI9F5Em9AC46J5cslpXubBFTk2l20x1ZAfbAbyzzp
                             rDBpq9KnBy8OV2KqWMj6/4cmH7qdxMzi0IkVy4cImdyPNGr7TQpnDg==
                             -----END RSA PRIVATE KEY-----
                             """

                def sub_cb(topic, msg):
                    global state
                    global m
                    print(m)
                    m = (topic, msg)
                    state = 1

                c = MQTTClient(clientID, url, port, ssl=True,
                               ssl_params={"cert": certificate_content, "key": private_content})
                c.set_callback(sub_cb)
                c.connect()
                c.subscribe(b"test/gps_tracker")
                c.publish(b"test/gps_tracker", b"my name is Quecpython!")
                while True:
                    c.wait_msg()  # Blocking Functions, Listening to Messages
                    if state == 1:
                        info = m
                        result = True
                        c.disconnect()
                        break
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def MQTT_05_001(self):  # 待执行函数
        '''
        :return: info 执行log,result 执行结果
        '''
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = 'xxxx'
                if info == '864430010001091':
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def MQTT_05_002(self):  # 待执行函数
        '''
        :return: info 执行log,result 执行结果
        '''
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = 'xxxx'
                if info == '864430010001091':
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def MQTT_05_003(self):  # 待执行函数
        '''
        :return: info 执行log,result 执行结果
        '''
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = 'xxxx'
                if info == '864430010001091':
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def MQTT_06_001(self):  # 待执行函数
        '''
        :return: info 执行log,result 执行结果
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                productKey = "Rie7JR259d6"  # 产品标识
                productSecret = None
                DeviceName = "lte_test"  # 设备名称
                DeviceSecret = "JAM0IQkcj0Fk2ytuGkJq5HFnWHNj3MAW"  # 设备密钥（一型一密认证此参数传入None）
                topic = "/Rie7JR259d6/lte_test/update"
                clientID = "12345"  # 自定义字符（不超过64）
                msg = "hell world"
                ali = aLiYun(productKey, productSecret, DeviceName, DeviceSecret)
                ali.setMqtt(clientID, clean_session=False, keepAlive=300)
                info = []

                def sub_cb(topic, msg):
                    m = (topic, msg)
                    info.append(m)
                ali.setCallback(sub_cb)
                ali.subscribe(topic)
                ali.publish(topic, msg, qos=0)
                ali.start()
                utime.sleep(2)
                ali.disconnect()
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def MQTT_06_002(self):  # 待执行函数
        '''
        :return: info 执行log,result 执行结果
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                productKey = "a1zdILSO5Vl"  # 产品标识
                productSecret = None
                DeviceName = "shalqin05"  # 设备名称
                DeviceSecret = "87421bdd823f05995add73a4655d29b4"  # 设备密钥（一型一密认证此参数传入None）
                topic = "/ota/device/request/a1zdILSO5Vl/shalqin05"
                clientID = "12345"  # 自定义字符（不超过64）
                msg = "hell world"
                ali = aLiYun(productKey, productSecret, DeviceName, DeviceSecret)
                ali.setMqtt(clientID, clean_session=False, keepAlive=300)
                info = []

                def sub_cb(topic, msg):
                    m = (topic, msg)
                    info.append(m)
                ali.setCallback(sub_cb)
                ali.subscribe(topic)
                ali.publish(topic, msg, qos=0)
                ali.start()
                utime.sleep(2)
                ali.disconnect()
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def MQTT_07_001(self):  # 待执行函数
        '''
        :return: info 执行log,result 执行结果
        '''
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def MQTT_07_002(self):  # 待执行函数
        '''
        :return: info 执行log,result 执行结果
        '''
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def MQTT_07_003(self):  # 待执行函数
        '''
        :return: info 执行log,result 执行结果
        '''
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def MQTT_07_004(self):  # 待执行函数
        '''
        :return: info 执行log,result 执行结果
        '''
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def MQTT_07_005(self):  # 待执行函数
        '''
        :return: info 执行log,result 执行结果
        '''
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def MQTT_08_001(self):  # 待执行函数
        '''
        :return: 腾讯云动态注册关闭
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                productID = "1U49Z5U39T"  # 产品标识
                devicename = "ec100y_01"  # 设备名称
                devicePsk = "IHadNUAMUuiRA1Tow6xQ3A=="  # 设备密钥（一型一密认证此参数传入None）
                ProductSecret = None  # 产品密钥（一机一密认证此参数传入None）
                topic = "1U49Z5U39T/ec100y_01/data"
                msg = "hell world"

                def sub_cb(topic, msg):  # 云端消息响应回调函数    
                    print("subscribe recv:")
                    print(topic, msg)

                tenxun = TXyun(productID, devicename, devicePsk, ProductSecret)  # 创建连接对象
                tenxun.setMqtt()
                tenxun.setCallback(sub_cb)
                tenxun.subscribe(topic)
                tenxun.publish(topic, msg)
                tenxun.start()
                utime.sleep(2)
                tenxun.disconnect()
                info = 'None'
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def MQTT_08_002(self):  # 待执行函数
        '''
        :return: 腾讯云动态注册开启
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                productID = "1U49Z5U39T"  # 产品标识
                devicename = "ec100y_01"  # 设备名称
                devicePsk = "IHadNUAMUuiRA1Tow6xQ3A=="  # 设备密钥（一型一密认证此参数传入None）
                ProductSecret = None  # 产品密钥（一机一密认证此参数传入None）
                topic = "1U49Z5U39T/ec100y_01/data"
                msg = "hell world"

                def sub_cb(topic, msg):  # 云端消息响应回调函数    
                    print("subscribe recv:")
                    print(topic, msg)

                tenxun = TXyun(productID, devicename, devicePsk, ProductSecret)  # 创建连接对象
                tenxun.setMqtt()
                tenxun.setCallback(sub_cb)
                tenxun.subscribe(topic)
                tenxun.publish(topic, msg)
                tenxun.start()
                utime.sleep(2)
                tenxun.disconnect()
                info = 'None'
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def MQTT_09_001(self):  # 待执行函数
        '''
        :return: info 执行log,result 执行结果
        '''
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def MQTT_09_002(self):  # 待执行函数
        '''
        :return: info 执行log,result 执行结果
        '''
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def MQTT_09_003(self):  # 待执行函数
        '''
        :return: info 执行log,result 执行结果
        '''
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def MQTT_09_004(self):  # 待执行函数
        '''
        :return: info 执行log,result 执行结果
        '''
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def MQTT_09_005(self):  # 待执行函数
        '''
        :return: info 执行log,result 执行结果
        '''
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def MQTT_10_001(self):  # 待执行函数
        '''
        :return: mqtt同一设备订阅多个主题
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                client_id = '12345|securemode=3,signmethod=hmacsha1,timestamp=707|'
                server = "Rie7JR259d6.iot-as-mqtt.cn-shanghai.aliyuncs.com"
                port = '1883'
                user = 'lte_test&Rie7JR259d6'
                password = '5b27fc4c011361964b922761953815e568172861'
                keepalive = 60
                ssl = False
                path1 = "/Rie7JR259d6/lte_test/update"  # MQTT服务器订阅地址
                path2 = "/Rie7JR259d6/lte_test/test_topic"
                path3 = "/Rie7JR259d6/lte_test/update1128"
                list = []

                def sub_cb(topic, msg):
                    global state
                    m = (topic, msg)
                    list.append(m)
                    state = len(list)

                c = MQTTClient(client_id, server, port=port, user=user, password=password, keepalive=keepalive, ssl=ssl,
                               ssl_params={})
                c.connect()
                c.set_callback(sub_cb)
                c.subscribe(path1)
                c.subscribe(path2)
                c.subscribe(path3)
                li = [path1, path2, path3]
                for i in li:
                    c.publish(i, b"hello")
                while True:
                    c.wait_msg()
                    if state == 3:
                        c.disconnect()
                        break
                info = list
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def MQTT_10_002(self):  # 待执行函数
        '''
        :return: aLiYun同一设备订阅多个主题
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                productKey = "Rie7JR259d6"  # 产品标识
                productSecret = None  # 产品密钥（一机一密认证此参数传入None）
                DeviceName = "lte_test"  # 设备名称
                DeviceSecret = 'JAM0IQkcj0Fk2ytuGkJq5HFnWHNj3MAW'  # 设备密钥（一型一密认证此参数传入None）
                # 创建aliyun连接对象
                ali = aLiYun(productKey, productSecret, DeviceName, DeviceSecret)
                # 设置mqtt连接属性
                clientID = "mqttText"  # 自定义字符（不超过64）
                ali.setMqtt(clientID, clean_session=False, keepAlive=300)
                topic1 = '/Rie7JR259d6/lte_test/test_topic'
                topic2 = '/Rie7JR259d6/lte_test/update'
                topic3 = '/Rie7JR259d6/lte_test/update1128'
                msg = "hello world"
                list2 = []

                def sub_cb(topic, msg):
                    a = (topic, msg)
                    list2.append(a)

                ali.setCallback(sub_cb)
                ali.subscribe(topic1)
                ali.subscribe(topic2)
                ali.subscribe(topic3)
                list1 = [topic1, topic2, topic3]
                for i in list1:
                    ali.publish(i, msg)
                ali.start()
                utime.sleep(2)
                ali.disconnect()
                info = list2
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def MQTT_10_003(self):  # 待执行函数
        '''
        :return: 腾讯云同一设备订阅多个主题
        '''
        runflag = 1
        if runflag:
            try:
                # --------------valid code--------------
                productID = "XAVDBW7LR7"  # 产品标识
                devicename = "lte01"  # 设备名称
                devicePsk = "JKlkG8zJIcwMwo1aeF1E/Q=="  # 设备密钥（一型一密认证此参数传入None）
                ProductSecret = None  # 产品密钥（一机一密认证此参数传入None）
                tenxun = TXyun(productID, devicename, devicePsk, ProductSecret)  # 创建连接对象
                topic1 = 'XAVDBW7LR7/lte01/control'
                topic2 = 'XAVDBW7LR7/lte01/data'
                topic3 = 'XAVDBW7LR7/lte01/data'
                msg = "hello world"

                def sub_cb(topic, msg):  # 云端消息响应回调函数
                    print(topic, msg)

                tenxun.setMqtt()
                tenxun.setCallback(sub_cb)
                tenxun.subscribe(topic1)
                tenxun.subscribe(topic2)
                tenxun.subscribe(topic3)
                list3 = [topic1, topic2, topic3]
                for i in list3:
                    tenxun.publish(i, msg)
                tenxun.start()
                utime.sleep(2)
                tenxun.disconnect()
                info = 'None'
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def MQTT_11_001(self):  # 待执行函数
        '''
        :return: 建立mqtt连接
        '''
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def MQTT_11_002(self):  # 待执行函数
        """
        阿里云两个设备连接同一服务端
        A设备订阅Y主题
        B设备订阅Y主题
        服务端推送Y主题消息
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def MQTT_11_003(self):  # 待执行函数
        """
        MQTT两个设备连接同一服务端
        A设备订阅Y主题
        B设备订阅Y主题
        服务端推送Y主题消息
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def MQTT_11_004(self):  # 待执行函数
        """
        阿里云两个设备连接同一服务端
        A设备订阅X主题
        B设备订阅Y主题
        服务端推送Y主题消息
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def MQTT_11_005(self):  # 待执行函数
        """
        阿里云两个设备连接同一服务端
        A设备订阅Y主题
        B设备订阅Y主题
        服务端推送Y主题消息
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def MQTT_12_001(self):  # 待执行函数
        """
        移动GSM网络下查看MQTT&阿里云连接状态
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def MQTT_12_002(self):  # 待执行函数
        """
        auto模式下放屏蔽5min拿出模块找网正常，
        查看MQTT&阿里云&腾讯云连接状态（移动，联通，电信均测试）
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def MQTT_12_003(self):  # 待执行函数
        """
        auto模式下放屏蔽10min拿出模块找网正常，
        查看MQTT&阿里云&腾讯云连接状态（移动，联通，电信均测试）
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def MQTT_12_004(self):  # 待执行函数
        """
        auto模式下放屏蔽20min拿出模块找网正常，
        查看MQTT&阿里云&腾讯云连接状态(移动，联通，电信均测试)
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def MQTT_13_001(self):  # 待执行函数
        """
        1.模块建立mqtt连接
        2.模块进入休眠模式
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def MQTT_13_002(self):  # 待执行函数
        """
        1.模块建立阿里云连接
        2.模块进入休眠模式
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def MQTT_13_003(self):  # 待执行函数
        """
        1.模块建立腾讯云连接
        2.模块进入休眠模式
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def MQTT_13_004(self):  # 待执行函数
        """
        1.模块建立mqtt连接
        2.进行TTS播放
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def MQTT_13_005(self):  # 待执行函数
        """
        1.建立阿里云连接
        2.进行TTS播放
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def MQTT_13_006(self):  # 待执行函数
        """
        1.建立腾讯云连接
        2.进行TTS播放
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def MQTT_14_001(self):  # 待执行函数
        """
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def MQTT_14_002(self):  # 待执行函数
        """
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def MQTT_14_003(self):  # 待执行函数
        """
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def MQTT_14_004(self):  # 待执行函数
        """
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def MQTT_14_005(self):  # 待执行函数
        """
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def MQTT_14_006(self):  # 待执行函数
        """
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def MQTT_14_007(self):  # 待执行函数
        """
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def MQTT_15_001(self):  # 待执行函数
        """
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def MQTT_16_001(self):  # 待执行函数
        """
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def MQTT_16_002(self):  # 待执行函数
        """
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def MQTT_16_003(self):  # 待执行函数
        """
        :return:
        """
        runflag = 0
        if runflag:
            try:
                # --------------valid code--------------
                info = []
                if info:
                    result = True
                else:
                    result = False
                # --------------valid code--------------
            except BaseException as e:
                info = e
                result = False
        else:
            info = 'N/A'
            result = 'N/A'
        return info, result

    def method(self): # 必备函数
        '''
        返回类中除内置方法外的所有方法名
        :return:
        '''
        return (list(filter(lambda m: not m.startswith("__") and not m.endswith("__") and callable(getattr(self, m)),
                            dir(self))))

    def run(self): # 必备函数
        '''
        主执行函数
        :return:
        '''
        case_list = []
        for i in self.method():  # 遍历类中方法
            if 'MQTT' in i:  # 注意修改此为testcase名称
                case_list.append(i)  # 筛选出testcase
        case_list.sort()  # testcase排序
        for i in case_list:
            a, b = getattr(self, i)()  # 遍历执行case
            print('%s:: %s||result_case:: %s;' % (i, a, b))   # 输出执行log供外部框架解析
            utime.sleep(3)


if __name__ == '__main__':
    MQTTFunctionTest().run()
