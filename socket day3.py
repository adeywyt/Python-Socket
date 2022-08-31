# Python TCP套接字实例[1]:
import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # 创建用于 IPv4 的 TCP 套接字.TCP是socket.SOCK_STREAM不是socket.SOCK_DGRAM
    host = "time.nist.gov"  # 工作时间服务器的主机名
    port = 13   # 端口号

    s.connect((host, port))  # 使用connect()连接到远程套接字.
    s.sendall(b'')
    # sendall()方法将数据发送到套接字.套接字必须连接到远程套接字.它继续从字节发送数据.直到发送完所有数据或发生错误为止.
    print(str(s.recv(4096), 'utf-8'))
    """
    我们打印接收到的数据.recv()方法从套接字接收最多缓冲区大小个字节。.
    当没有数据可用时，它将阻塞，直到至少一个字节可用或直到远端关闭为止. 
    当远端关闭并读取所有数据时，它将返回一个空字节字符串.
    """