"""
@Author: trent.zhang
@Date: 2020-09-10
@LastEditTime: 2020-09-10 10:06:08
@Description: example for module usocket
@FilePath: socket_write_read_recv_stress.py
"""
import usocket
import utime

HOST = '220.180.239.212'
PORT = 8305
BUFSIZE = 1024
ADDR = (HOST, PORT)
msg = 'hello'


def soket_udp():
    """
    模块做服务端以udp方式发送数据
    :return:
    """
    try:
        client = usocket.socket(usocket.AF_INET, usocket.SOCK_DGRAM)
        client.sendto(msg.encode('utf-8'), ADDR)
        data, server_addr = client.recvfrom(BUFSIZE)
        if data:
            print('.sendto(),.recvfrom()::pass||result_api:: True;')
        else:
            print('.sendto(),.recvfrom()::fail||result_api:: False;')
        client.close()
    except Exception as e:
        print('socket::%s||udp_socket:: False;'%e)


def soket_tcp(api):
    """
    模块做服务端以TCP方式发送数据
    :return:
    """

    result1 = 'error'
    try:
        result1 = eval(api)
    except Exception as err:
        print('[error]'+str(err)+';')
    if result1 != 'error':
        result2 = True
    else:
        result2 = False
    print('%s:: %s||result_api:: %s;' % (api, result1, result2))
    utime.sleep(0.05)


if __name__ == '__main__':
    soket_udp()
    list_api = [
        "client.send('12345')",
        "client.sendall('1234567890')",
        "client.recv(BUFSIZE)",
        "client.settimeout(20)",
        "client.read(2)",
        "client.readline(1)",
        "client.write('123456')",
        "usocket.getaddrinfo('www.tongxinmao.com', 80)",
        'client.close()'
    ]
    client = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM)
    client.connect(ADDR)
    for i in list_api:
        soket_tcp(i)
