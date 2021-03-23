# UART使用demo

from machine import UART


# /*
# * 参数1：端口 （0：QL_DEBUG_UART_PORT  1：QL_BT_UART_PORT  2：QL_MAIN_UART_PORT  3：QL_USB_CDC_PORT）
# * 参数2：波特率 （300~3686400）//常用的波特率都支持
# * 参数3：data bits  （5~8）
# * 参数4：Parity  （0：NONE  1：EVEN  2：ODD）
# * 参数5：stop bits （1~2）
# * 参数6：flow control （0: FC_NONE  1：FC_HW）
# */

uart = UART(3, 115200, 8, 0, 1, 0)  # 初始化

uart.write("Hello") # 发送数据

uart.any() # 获取接受的数据个数

uart.read(5) # 读取5个收到的数据
