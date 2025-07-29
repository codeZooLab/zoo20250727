#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 UDP应用  广播接收

"""

from socket import *
import sys

try:
    s = socket(AF_INET, SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    s.bind(("0.0.0.0",4444))

    print("等待接收广播消息...")
    while True:
        try:
            msg, addr = s.recvfrom(1024)
            print(f"收到消息来自 {addr}: {msg.decode()}")
        except KeyboardInterrupt:
            print("程序已中断")
            break
        except Exception as e:
            print(f"发生错误: {e}")
            break
finally:
    s.close()
    print("套接字已关闭")