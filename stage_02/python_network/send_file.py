#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from socket import *
from time import sleep

s = socket()
s.connect(('127.0.0.1',6666))

# 读取文件，循环发送
f = open('/stage_02/python_network/aa.py', 'rb')
while True:
    # 边读取边发送
    data = f.read(1024)
    if not data:
        break
    sleep(0.5)
    s.send(data)

f.close()
s.close()