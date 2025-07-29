#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
 UDP应用  广播发送

"""

from socket import *
from time import sleep

dest = ('127.0.0.1', 4444)

try:
    s = socket(AF_INET, SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

    data = """
        aaaa
    """

    try:
        while True:
            sleep(2)
            s.sendto(data.encode(), dest)
            print("数据已发送")
    except KeyboardInterrupt:
        print("程序已中断")
    finally:
        s.close()
except Exception as e:
    print(f"发生错误: {e}")