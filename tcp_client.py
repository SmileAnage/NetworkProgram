"""
TCP客户端
向服务端发送信息
"""
from socket import *

socket_s = socket()  # 创建套接字

socket_s.connect(("127.0.0.1", 7776))  # 设置服务端地址及端口(请求连接)

while True:
    data = input('Mag>>')
    if not data:
        break
    socket_s.send(data.encode())
    data = socket_s.recv(1024)
    print("Server:", data.decode())

socket_s.close()
