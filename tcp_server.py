"""
TCP服务端
接收客户端消息并反馈
"""
from socket import *

socket_s = socket()  # 创建套接字

socket_s.bind(("0.0.0.0", 7776))  # 绑定地址及端口

socket_s.listen(7)  # 设置监听(参数无所谓)

while True:
    # 阻塞等待处理连接
    print("Waitting for Connect...")
    try:
        connect, addr = socket_s.accept()
        print("Connect from ", addr)
    except KeyboardInterrupt:
        print("Server exit")
        break
    except Exception as e:
        print(e)
        continue

    while True:
        # 接收消息
        data = connect.recv(1024)
        if not data:
            break
        print("收到：", data.decode())
        connect.send(b'OK')
    connect.close()

socket_s.close()
