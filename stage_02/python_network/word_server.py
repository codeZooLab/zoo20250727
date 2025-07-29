#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
通过客户端输入单词 查找字典注释
"""

from socket import *
from stage_02.python_network.linux_file_io import find_word

sockfd = socket(AF_INET,SOCK_DGRAM)
sockfd.bind(('127.0.0.1',5555))
while True:
    data,addr = sockfd.recvfrom(1024)
    print("接收单词",data.decode())
    re = find_word(data.decode())
    sockfd.sendto(re.encode(),addr)

sockfd.close()

