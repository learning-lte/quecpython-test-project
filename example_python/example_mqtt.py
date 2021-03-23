'''
@Author: Baron
@Date: 2020-04-24
@LastEditTime: 2020-04-24 17:06:08
@Description: example for module umqtt
@FilePath: example_mqtt.py
'''
from umqtt import MQTTClient
import utime

state = 0

def sub_cb(topic, msg):
	global state
	print("subscribe recv:")
	print(topic, msg)
	state = 1

# 创建一个mqtt实例
c = MQTTClient("umqtt_client", "mq.tongxinmao.com", '18830')
# 设置消息回调
c.set_callback(sub_cb)
#建立连接
c.connect()
# 订阅主题
c.subscribe(b"/public/TEST/quecpython")
print("Connected to mq.tongxinmao.com, subscribed to /public/TEST/quecpython topic" )
# 发布消息
c.publish(b"/public/TEST/quecpython", b"my name is Pawn!")
print("Publish topic: /public/TEST/quecpython, msg: my name is Quecpython")

while True:
	c.wait_msg()  # 阻塞函数，监听消息
	if state == 1:
		break

# 关闭连接	
c.disconnect()