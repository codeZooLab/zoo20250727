#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
将一个文件从客户端发送到服务端
* 文件可能是文本文件也可能是二进制文件
"""

from socket import *

s = socket()
s.bind(('127.0.0.1',6666))
s.listen(5)

c,addr = s.accept()
print("Connect from",addr)

# recv内容，写入本地文件
# 本地文件以wb

# 打开文件
f = open('bb.py','wb')

# 循环接收内容写入本地
while True:
    data = c.recv(1024)  # bytes
    if not data:
        break
    f.write(data)

f.close()
c.close()
s.close()