"""
    ＴＣＰ服务端
"""
from socket import *

# 创建套接字
s = socket()

# 绑定地址及端口
s.bind(("176.136.7.22", 7777))

# 设置监听(参数无所谓)
s.listen(7)

# 等待处理客户端连接请求
print("Waiting for connect...")
connfd, addr = s.accept()
print("Connect from", addr)

# 接收的东西根据格式改命名
fw = open("get.jpg", "wb")

# 接收消息
while True:
    data = connfd.recv(1024)
    if not data:
        break
    # 将接收的消息写入文件
    fw.write(data)

# 关闭套接字及文件
fw.close()
s.close()
