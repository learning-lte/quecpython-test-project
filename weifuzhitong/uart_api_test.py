from machine import UART
uart = UART(UART.UART1, 115200, 8, 0, 1, 0)
uart.write(b'abcdefghijklmnopqrstuvwxwz1234567890')

def print(data):
    uart.write(data.encode())
while 1:
    if uart.any():
        print(str(uart.any()))
        data = uart.read(uart.any())
        print('[module_rev_from_uart]%s'%(data.decode()))
        uart.write(b'abcdefghijklmnopqrstuvwxwz1234567890')