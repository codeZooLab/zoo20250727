#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
tcp_client.py  tcp客户端流程
重点代码
"""

from socket import *
from time import sleep

# 创建tcp套接字
sockfd = socket()  # 默认参数-->tcp套接字

# 连接服务端程序
server_addr = ('localhost',8888)
sockfd.connect(server_addr)

# 发送接收消息
while True:
    data = input("Msg:")
    # data为空退出循环
    if not data:
        break
    sleep(0.1)  # 防止粘包控制发送速度 或者添加消息边界由服务端二次处理
    sockfd.send(data.encode()) # 发送字节串
    data = sockfd.recv(1024)
    print("Server:",data.decode())

# 关闭套接字
sockfd.close()