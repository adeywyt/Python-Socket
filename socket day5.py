# Python套接字GET请求：
import socket
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect(("webcode.me",80))
    s.sendall(b"GET / HTTP/1.1\r\nHost: webcode.me\r\nAccept: text/html\r\nConnection: close\r\n\r\n")
    # 使用 GET 请求读取webcode.me的主页.
    while True:
        data=s.recv(1024)
        if not data:
            break
        print(data.decode())