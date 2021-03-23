'''
@Author: Randy
@Date: 2020-11-09
@LastEditTime: 2020-11-09
@Description: Out Of Memory Test
@FilePath: out_of_memory_thread_mqtt_tts_fs_tcp_uart_stress.py
'''
'''
-------------------------------------------------------------------------------
脚本逻辑:
    1.mqtt收发、tts&audio播放、fs读写、tcp数传、uart读写
    2.多线程分别运行步骤1中的程序
    3.长时间运行至少48H
脚本统计:
    1.接口函数调用崩溃log
测试前准备:
    无
备注：
    1.当前版本暂无结束线程的接口，无法结束线程
    2.本脚本测试无业务功能程序调用的以基本print消息代替，共运行16个线程
-------------------------------------------------------------------------------
'''
import audio
import urandom
import _thread
import utime
import ujson
import uos
a = 0
lock = _thread.allocate_lock()

def mqtt():
    from umqtt import MQTTClient
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
    topic = "/Rie7JR259d6/lte_test/update"  # 主题
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
        print("subscribe recv:pass;")
        if data == msg:
            pass
        else:
            print("subscribe recv:%s;"%msg)
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
        utime.sleep(1)



    list = [
        'c.connect(clean_session=True)',
        'c.subscribe(topic)',
        'c.publish(topic, msg)',
    ]
    try:
        print('nihao1')
        c = MQTTClient(client_id, server, port=port, user=user, password=password, keepalive=keepalive, ssl=False,
                       ssl_params={})
        c.set_last_will(path, last_will, retain=False, qos=0)  # retain = True boker会一直保留消息，默认False
        c.set_callback(sub_cb)
        print('MQTTClient,set_last_will,set_callback::pass||result_api: Ture;')
        a = 0
        while 1:
            a += 1
            if a % 1000 == 0:
                print('------------ mqtt Runtime: %s---------------;' % a)
            try:
                c.connect(clean_session=True)
                c.subscribe(topic)
                c.publish(topic, msg)
                c.disconnect()
                print('[memory] free heap: %s;' % (_thread.get_heap_size()))
            except Exception as e:
                c.disconnect()
                print('------------ mqtt Runtime: %s---------------' % a)
                print('disconnect::[error]%s||result_api: False;'%e)
            utime.sleep_ms(500)
    except Exception as e:
        print('MQTTClient,set_last_will,set_callback::[error]%s||result_api:: False;'%e)
        c.disconnect()
    print('############mqtt quit#############;')

def uart():
    from machine import UART
    uart = UART(UART.UART1, 115200, 8, 0, 1, 0)
    text = 'Starta123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a123456789a1234567891234567891234567END'
    uart.write(text.encode())
    a = 0
    try:
        while 1:
            a += 1
            if a % 1000 == 0:
                print('------------ uart Runtime: %s---------------;' % a)
            try:
                #print('[uart_rev]' + str(uart.any()))
                uart.read(int(uart.any()))
                uart.write(text.encode())
                #print('[uart_write]')
            except Exception as e:
                print('------------ uart Runtime: %s---------------;' % a)
                print('uart r&w::[error]%s||result_api:: False;' % e)
            utime.sleep_ms(100)
    except Exception as e:
        print('############uart quit#############;')

def tcp():
    import usocket
    # 创建一个socket实例
    sock = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM)
    # 解析域名
    print(usocket.getaddrinfo('220.180.239.212', 8305))
    sockaddr = usocket.getaddrinfo('220.180.239.212', 8305)[0][-1]
    a = 0
    try:
        # 建立连接
        sock.connect(sockaddr)
        # 向服务端发送消息
        # ret=sock.send('GET /News HTTP/1.1\r\nHost: 220.180.239.212\r\nAccept-Encoding: deflate\r\nConnection: keep-alive\r\n\r\n')
        send_data = "\
            -----BEGIN CERTIFICATE-----\n\
            -----END CERTIFICATE-----\n\
            "
        while 1:
            a += 1
            if a % 1000 == 0:
                print('------------ tcp Runtime: %s---------------;' % a)
            try:
                ret = sock.send(send_data)
                #print('send %d bytes' % ret)
                # 接收服务端消息
                data1 = ''
                while 1:
                    data = sock.recv(4096)
                    data1 += data.decode()
                    if len(data1) == ret:
                        break
                #print('recv %s bytes:' % len(data1))
            except Exception as e:
                print('------------ tcp Runtime: %s---------------;' % a)
                print('tcp send&recv::[error]%s||result_api:: False;' % e)
            utime.sleep(20)
    except Exception as e:
        sock.close()
        print('------------ tcp Runtime: %s---------------;' % a)
        print('tcp connect&close::[error]%s||result_api:: False;' % e)
        print('############tcp quit#############;')

def tts():

    TTS = audio.TTS(2)
    a = 0
    while 1:
        a += 1
        if a % 1000 == 0:
            print('------------ tts Runtime: %s---------------;' % a)
        try:
            TTS.play(urandom.randint(0, 4), urandom.randint(0, 1), urandom.randint(1, 3), "移远通信万物互联移远通信万物互联移远通信万物互联"
                                                                                          "移远通信万物互联移远通信万物互联移远通信万物互联"
                                                                                          "移远通信万物互联移远通信万物互联移远通信万物互联")
            TTS.play(urandom.randint(0, 4), urandom.randint(0, 1), urandom.randint(1, 3),
                     'abcdefghi0123456789abcdefghi0123456789'
                     'abcdefghi0123456789abcdefghi0123456789'
                     'abcdefghi0123456789abcdefghi0123456789'
                     'abcd1234')  # 128字节数据
        except Exception as e:
            print('------------ tts Runtime: %s---------------;' % a)
            print('############tts quit#############;')
            print('play::[error]%s||result_api:: False;' % e)
        utime.sleep(5)

def fs():
    fileName = '/usr/test.txt'
    # strInfo = {'IMEI': '866327040075699', 'sid': '1595318579505h', 'funCode': '0d', 'data': '0101', 'cmd': 210}
    strInfo = bytearray(1030)
    a = 0
    while 1:
        try:
            while 1:
                a += 1
                if a % 1000 == 0:
                    print('------------ fs Runtime: %s---------------;' % a)

                try:
                    f = open(fileName, 'w')
                except:
                    print('fs open file exception;')
                    continue
                try:
                    f.write(ujson.dumps({'msg': strInfo}))
                    f.close()
                    uos.statvfs('/')
                    #print('fs write successful')
                except:
                    print('fs write fail;')
                    if f:
                        f.close()
                utime.sleep_ms(10)
                try:
                    f = open(fileName, 'r')
                except:
                    print('fs open file exception;')
                    continue
                try:
                    lineText = f.readline()
                    f.close()
                    #print('fs read successful')
                except:
                    if f:
                        f.close()
                utime.sleep_ms(10)
        except Exception as e:
            print('------------ fs Runtime: %s---------------;' % a)
            print('############fs quit#############;')
            print('fs r&w::[error]%s||result_api:: False;' % e)

def th_func(delay, id):
    a = 0

    while True:
        a += 1
        th_id = _thread.get_ident()  # 获取当前线程号
        if a % 100 == 0:
            print('[thread %d id %s] runtimes: %s;' % (id, th_id, a))
            print('[memory] free heap: %s;'%(_thread.get_heap_size()))
        utime.sleep(delay)

try:
    _thread.stack_size()  # 返回创建新线程使用的堆栈大小（以字节为单位）
    _thread.start_new_thread(fs, ())
    _thread.start_new_thread(tts, ())
    _thread.start_new_thread(tcp, ())
    _thread.start_new_thread(uart, ())
    #_thread.start_new_thread(mqtt, ())
    for i in range(5,16):
        a = _thread.start_new_thread(th_func, (i, i+1))
        print(a,type(a))

except Exception as error:
    print('############thread quit#############;')
    print('thread::[error] %s||result_api:: False;'%error)

#反复创建、删除线程
#当前版本暂无结束线程的接口，无法结束线程