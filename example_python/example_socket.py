'''
@Author: Baron
@Date: 2020-04-24
@LastEditTime: 2020-04-26 09:56:08
@Description: example for module usocket
@FilePath: example_socket.py
'''
# 导入usocket模块
import usocket

# 创建一个socket实例
sock = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM)
# 解析域名
sockaddr=usocket.getaddrinfo('www.tongxinmao.com',80)[0][-1]
# 建立连接
sock.connect(sockaddr)
# 向服务端发送消息
ret=sock.send('GET /News HTTP/1.1\r\nHost: www.tongxinmao.com\r\nAccept-Encoding: deflate\r\nConnection: keep-alive\r\n\r\n')
print('send %d bytes' % ret)
#接收服务端消息
data=sock.recv(256)
print('recv %s bytes:' % len(data))
print(data.decode())

# 关闭连接
sock.close()
