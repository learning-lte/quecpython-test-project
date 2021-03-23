'''
@Author: Randy
@Date: 2020-09-08
@LastEditTime: 2020-09-08
@Description: API test for UART
@FilePath: uart_write_read_compare_api_test.py
'''

from machine import UART
import utime
#--------参数配置区------------
data = '1234567890'
#--------------------
print('send data: %s'%data)
buadrate = [4800,9600,19200,38400,57600,115200,230400]
# UART0 - DEBUG PORT
# UART1 – BT PORT
# UART2 – MAIN PORT
# UART3 – USB CDC PORT
print('please open your debug port and wait 10s')
utime.sleep(10)
try:
    for m in buadrate: #波特率4800、9600、19200、38400、57600、115200、230400等
        uart = UART(UART.UART0, m, 8, 0, 1, 0)
        uart.write(data)
        a = uart.any()
        uart.read(a)
        uart.close()
        utime.sleep(1)
        print('UART0: ok,result_api: True')
except Exception as e:
    print('[error]'+str(e))
    print('UART0_api: Flase')

print('please open your UART1 port and wait 10s')
utime.sleep(10)
try:
    for m in buadrate:  # 波特率4800、9600、19200、38400、57600、115200、230400等
        uart = UART(UART.UART1, m, 8, 0, 1, 0)
        uart.write(data)
        a = uart.any()
        uart.read(a)
        uart.close()
        utime.sleep(1)
        print('UART1: ok,result_api: True')
except Exception as e:
    print('[error]'+str(e))
    print('UART1_api: Flase')

print('start write to MAIN port and wait 10s')
utime.sleep(10)
try:
    for m in buadrate: #波特率4800、9600、19200、38400、57600、115200、230400等
        uart = UART(UART.UART2, m, 8, 0, 1, 0)
        uart.write(data)
        a = uart.any()
        uart.read(a)
        uart.close()
        utime.sleep(1)
        print('UART2: ok,result_api: True')
except Exception as e:
    print('[error]'+str(e))
    print('UART2_api: Flase')

print('start write to CDC port and wait 10s')
utime.sleep(10)
try:
    for m in buadrate: #波特率4800、9600、19200、38400、57600、115200、230400等
        uart = UART(UART.UART3, m, 8, 0, 1, 0)
        uart.write(data)
        a = uart.any()
        uart.read(a)
        uart.close()
        utime.sleep(1)
        print('UART3: ok,result_api: True')
except Exception as e:
    print('[error]'+str(e))
    print('UART3_api: Flase')