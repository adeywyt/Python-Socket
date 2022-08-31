# socket.SOCK_STREAM用于为 TCP 创建套接字，而socket.SOCK_DGRAM为 UDP 创建套接字。
# Python UDP套接字实例[1]:

import socket

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:  # 创建用由IPv4的数据报套接字.
    message = b"" # 我们发送空消息,QOTD服务通过向套接字发送任意数据来工作,它只是用引号引起来.为了通过TCP/UDP进行通信.我们使用二进制字符串。
    adder = ("djxmmx.net", 17)   # 传递地址和端口.
    s.sendto(message, adder)     # 使用sendto()发送数据
    data, address = s.recvfrom(1024)  # 返回内容(data)和地址(adder)
    print(data.decode())  # 解码后的数据输出
