# Python 套接字 HEAD 请求:
import socket
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s: # 创建用于 IPv4 的 TCP 套接字.
    s.connect(("webcode.me",80))  # 主机名和端口
    s.sendall(b"HEAD / HTTP/1.1\r\nHost: webcode.me\r\nAccept: text/html\r\n\r\n")
    # 方法将数据发送到套接字.向webcode.me发送 HEAD 请求
    print(str(s.recv(1024),"utf-8"))
