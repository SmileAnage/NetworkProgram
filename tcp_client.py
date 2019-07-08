"""
    ＴＣＰ客户端
"""
from socket import *

# 创建套接字
s = socket()

# 设置服务端地址及端口(请求连接)
s.connect(("176.136.7.22", 7777))

# 选择打开二进制文件
file_name = input("Please enter file name:")
file_ = open(file_name, "rb")

# 向服务器发送文件
while True:
    # 先读取本地文件
    data = file_.read()
    if not data:
        break
    # 将读取的文件发送服务端
    s.send(data)
    print("Put OK!")

# 关闭套接字及文件
file_.close()
s.close()
