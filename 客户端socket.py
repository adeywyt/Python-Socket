import socket  # 导入 socket 模块

s = socket.socket()  # 创建 socket 对象
host = socket.gethostname()  # 获取本地主机名
port = 12345  # 设置端口号

s.connect((host, port))   # 地址和端口
data=s.recv(1024)
print(data.decode())  # bytes解码
s.close()  # 关闭连接